from django.db import models

class Item(models.Model):
    date_added = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()