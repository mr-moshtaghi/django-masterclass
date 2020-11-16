from django.db import models

class Item (models.Model):

    def __str__(self):      # this func show us in shell name of items when type Item.objects.all()
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500 ,default="https://s3.amazonaws.com/ODNUploads/532dfdbcc6479placeholder_food_item_2.png")

