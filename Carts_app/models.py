from Store_app.models import Product, Variation
from django.db import models

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True)    
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    variation = models.ManyToManyField(Variation)

    def __str__(self) -> str:
        return self.product.product_name

    def get_subTotal(self):
        return self.product.price * self.quantity
    def get_variation_dict(self):
        variations = self.variation.all()       
        variation_dict ={}
        for variation in variations:        
            key = variation.variation_category # variation_category in table Variation
            value = variation.variation_value # variation_value in table Variation
            variation_dict[key] = value
        return variation_dict