from django.urls import path
from main.views import (
    show_main, create_item, show_xml, show_json, show_json_by_id,
    show_xml_by_id, register, login_user, logout_user, increment_amount,
    decrement_amount, remove_item, edit_item, get_item_json, add_item_ajax
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increment-amount/<int:id>/', increment_amount, name='increment_amount'),
    path('decrement-amount/<int:id>/', decrement_amount, name='decrement_amount'),
    path('remove-item/<int:id>/', remove_item, name='remove_item'),
    path('edit-item/<int:id>/', edit_item, name='edit_item'),
    path('get-item', get_item_json, name='get_item_json'),
    path('create-item-ajax', add_item_ajax, name='add_item_ajax')
]