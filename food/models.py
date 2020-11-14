from django.db import models

class Item (models.Model):

    def __str__(self):      # this func show us in shell name of items when type Item.objects.all()
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()

