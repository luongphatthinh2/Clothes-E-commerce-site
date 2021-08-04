from .models import Cart, CartItem
from django.http.response import HttpResponse
from django.http import JsonResponse

def _get_session_id(request): # get the session id from the current session
    session_id = request.session.session_key
    return session_id

def get_cart(request):
    session_id = _get_session_id(request)
    if not session_id:
        return HttpResponse('You need to login first. The login page will come out soon')
    try:
        cart = Cart.objects.get(cart_id=session_id)
    except Cart.DoesNotExist:
        cart = Cart(cart_id=session_id)
        cart.save()
    return cart

def get_total_tax_grandTotal(cart):
    cart_items = CartItem.objects.filter(cart=cart, is_active=True) 
    total = 0
    for cart_item in cart_items:
        total += cart_item.get_subTotal()
    tax = get_tax(total)

    return {
        "total": total,
        "tax": tax,
        "grand_total": total + tax
    }

def get_tax(total):
    return (2*total)/100

def response_to_CartPage(cart, cart_item):
     # calculate total, price, and grand total the return them as JSON
    total_tax_grandTotal = get_total_tax_grandTotal(cart)
    response_body = {
        'sub_total': cart_item.get_subTotal(),
        **total_tax_grandTotal
    }
    print('DEBUG total_tax_grandTotal ', response_body)
    return JsonResponse(response_body)