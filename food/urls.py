from django.urls import path 

from . import views

app_name = 'food'
urlpatterns = [
    path("", views.index, name="index"),
    # /food/1/
    path("<int:item_id>/" , views.detail , name="detail"),
    path('item/', views.item, name='item'),
    # add item
    path('add/', views.create_item, name='create_item'),
    # eddit item
    
]