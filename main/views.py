import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from main.forms import ItemForm
from main.models import Item
from django.urls import reverse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@login_required(login_url='/login')
# Create your views here.
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'app_name': 'bicycleparts-inv',
        'name': "Username : " + request.user.username,
        'item_count': len(items),
        'items': items,
        'last_login': request.COOKIES.get('last_login')
    }

    return render(request, ["main.html", "base.html"], context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Mohon maaf, username atau password yang dimasukkan salah. Mohon untuk dicoba lagi . . .')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increment_amount(request, id):
    data = Item.objects.filter(user=request.user).get(id=id)
    data.amount += 1
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrement_amount(request,id):
    data = Item.objects.filter(user=request.user).get(id=id)
    data.amount -= 1
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def remove_item(request, id):
    data = Item.objects.filter(user=request.user).get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_item(request, id):
    # Get product berdasarkan ID
    product = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

# AJAX FUNCTIONS
def get_item_json(request):
    items = Item.objects.filter(user=request.user).all()
    return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, price=price, amount=amount, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
@require_http_methods(['DELETE'])
def remove_item_ajax(request, id):
    data = Item.objects.filter(user=request.user).filter(id=id)
    data.delete()
    return HttpResponse(b"DELETED", status=200)

@csrf_exempt
@require_http_methods(['POST'])
def edit_item_ajax(request, id):
    data = Item.objects.filter(user=request.user).get(id=id)
    form = ItemForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return HttpResponse(b"SUCCESS", status=200)
    
    return HttpResponseNotFound()