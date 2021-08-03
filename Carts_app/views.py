from django.http.response import HttpResponse
from django.shortcuts import render
from Store_app.models import Product
from .models import Cart, CartItem
from django.shortcuts import redirect
from django.http import JsonResponse
# Create your views here.



def _get_session_id(request): # get the session id from the current session
    session_id = request.session.session_key
    return session_id

def add_product_to_cart(request, product=None, cart=None):
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
    response_body = {
        'product_id':cart_item.product.id
    }
    return JsonResponse(response_body)

# remove 1 product in cart
def remove_product_from_cart(request, product=None, cart=None):
    cart_item = CartItem.objects.get(cart=cart, product=product, is_active=True)
    if cart_item.quantity == 1:
        return redirect(request.META['HTTP_REFERER'])
    cart_item.quantity -= 1
    cart_item.save()    
    return redirect(request.META['HTTP_REFERER'])


# remove a whole product from cart
def remove_whole_product_from_cart(request, product=None, cart=None):
    cart_item = CartItem.objects.get(cart=cart, product=product, is_active=True)   
    cart_item.delete() 
    return redirect(request.META['HTTP_REFERER'])

# cart central process
def cart(request, product_id=None):
    print('DEBUG request.path', request.resolver_match.url_name)
    session_id = _get_session_id(request)
    if not session_id:
        return HttpResponse('You need to login first. The login page will come out soon')
    try:
        cart = Cart.objects.get(cart_id=session_id)
    except Cart.DoesNotExist:
        cart = Cart(cart_id=session_id)
        cart.save()
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        pass
    url_name = request.resolver_match.url_name
    if url_name == 'add_to_card':
        return add_product_to_cart(request, product, cart)
    if url_name == 'remove_from_card':
        return remove_product_from_cart(request, product, cart)
    if url_name == 'remove_whole_from_card':
        return remove_whole_product_from_cart(request, product, cart)
    
    total = 0
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    for cart_item in cart_items:
        total += cart_item.get_subTotal()
    
    # calculate tax and grand total
    tax = (2*total)/100
    grand_total = total + tax
    context ={
        'cart_items': cart_items,
        'total': total,
        'tax':tax,
        'grand_total': grand_total
    }
    return render(request, 'store/cart.html', context)