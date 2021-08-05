from django.urls import reverse
from Category_app.models import Category
from Carts_app.models import Cart,CartItem
# def common_link(request):
#     common_link={}
#     common_link['store'] = reverse('store')
#     common_link['home'] = reverse('home')
#     # print('DEBUG common_link', common_link['store'])
#     return common_link



def categories_link(request):
    categories_link = Category.objects.all()
    return {'categories_link' : categories_link}

def quantity_in_cart(request):
    quantity = 0
    session_id = request.session.session_key
    if not session_id :
        return {'quantity': 0}
    try:
        cart = Cart.objects.get(cart_id=session_id)
    except Cart.DoesNotExist:
        pass
    try:
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    except CartItem.DoesNotExist:
        pass
    if not cart_items:
        return {'quantity': 0}
    for cart_item in cart_items:
        quantity += cart_item.quantity
    return {'quantity': quantity}