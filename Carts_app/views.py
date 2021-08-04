from django.shortcuts import render
from Store_app.models import Product
from .models import Cart, CartItem
from .helper_function import get_cart, get_total_tax_grandTotal, response_to_CartPage

# Create your views here.   

def add_product_to_cart(product=None, cart=None):
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem(
            product = product,
            cart = cart,
            quantity = 1
        )
        cart_item.save()
    
    # calculate total, price, and grand total the return them as JSON
    return response_to_CartPage(cart, cart_item)


# remove 1 product in cart
def remove_product_from_cart(product=None, cart=None):
    cart_item = CartItem.objects.get(cart=cart, product=product, is_active=True)
    if cart_item.quantity == 1:
        return remove_whole_product_from_cart(product,cart)
    cart_item.quantity -= 1
    cart_item.save()    

    # calculate total, price, and grand total the return them as JSON
    return response_to_CartPage(cart, cart_item)    


# remove a whole product from cart
def remove_whole_product_from_cart(product=None, cart=None):
    cart_item = CartItem.objects.get(cart=cart, product=product, is_active=True)   
    cart_item.delete() 

    # calculate total, price, and grand total the return them as JSON
    return response_to_CartPage(cart, cart_item)

# cart central process
def cart(request, product_id=None): 
    cart = get_cart(request)
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        pass
    # handle the url 
    url_name = request.resolver_match.url_name
    if url_name == 'add_to_card':
        return add_product_to_cart(product, cart)
    if url_name == 'remove_from_card':
        return remove_product_from_cart(product, cart)
    if url_name == 'remove_whole_from_card':
        return remove_whole_product_from_cart(product, cart)    

    # get all items in the cart
    cart_items = CartItem.objects.filter(cart=cart, is_active=True) 

    # calculate total price before tax,tax and grand total
    total_tax_grandTotal = get_total_tax_grandTotal(cart)
   
    context ={
        'cart_items': cart_items,
        **total_tax_grandTotal
    }
    return render(request, 'store/cart.html', context)