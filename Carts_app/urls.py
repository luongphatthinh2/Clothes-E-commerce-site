from os import name
from . import views
from django.urls import path


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>',views.cart, name='add_to_card'),
    path('remove_from_cart/<int:product_id>/',views.cart, name='remove_from_card'),
    path('remove_whole_from_cart/<int:product_id>/',views.cart, name='remove_whole_from_card')
]