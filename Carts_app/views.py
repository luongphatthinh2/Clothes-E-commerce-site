from django.shortcuts import get_object_or_404, render
from Store_app.models import Product, Variation
from .models import Cart, CartItem
from .helper_function import get_cart, get_total_tax_grandTotal, response_to_CartPage,               check_existed_variationInCart, create_VariationOfProduct

# Create your views here.   

def add_product_to_cart(request, product=None, cart=None):
    # get all the variations of the product which is currently in the cart
    cart_items = CartItem.objects.filter( 
        product=product,
        cart=cart,
        is_active=True,    
    )
    if cart_items: # there are at least 1 product in the cart
        cart_item = check_existed_variationInCart(request, cart_items)
        # print('DEBUG cart_item existed', cart_item )
        if cart_item:   # requested variation existed
            cart_item.quantity += 1
            cart_item.save()
        # else: # requested variation does not exist
        #     cart_item = create_VariationOfProduct(request, product, cart_item)    
        #     cart_item.quantity = 1
        #     cart_item.save()
    if not cart_items or not cart_item: # there is no requested products in the cart OR requested variation does not exist
        cart_item = CartItem(
            product = product,
            cart = cart,
            quantity = 1
        )
        cart_item.save()
        # print('DEBUG cart_item not existed', cart_item)
        cart_item = create_VariationOfProduct(request, product, cart_item)
        cart_item.save()

    # calculate total, price, and grand total the return them as JSON
    return response_to_CartPage(cart, cart_item)


# remove 1 product in cart
def remove_product_from_cart(request,product=None, cart=None):
    cart_items = CartItem.objects.filter(
        cart=cart, 
        product=product, 
        is_active=True)
    cart_item = check_existed_variationInCart(request, cart_items)
    if cart_item.quantity == 1:
        return remove_whole_product_from_cart(request,product,cart)
    cart_item.quantity -= 1
    cart_item.save()    
    # calculate total, price, and grand total the return them as JSON
    return response_to_CartPage(cart, cart_item)    


# remove a whole product from cart
def remove_whole_product_from_cart(request, product=None, cart=None):
    cart_items = CartItem.objects.filter(
        cart=cart, 
        product=product,
        is_active=True
    )   
    cart_item = check_existed_variationInCart(request, cart_items)
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
        return add_product_to_cart(request, product, cart)
    if url_name == 'remove_from_card':
        return remove_product_from_cart(request,product, cart)
    if url_name == 'remove_whole_from_card':
        return remove_whole_product_from_cart(request,product, cart)    

    # get all items in the cart
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)

    # ********** START DEBUG ZONE
    # cart_item_debug is one original product , we do not mention any variations in it.
    for cart_item in cart_items:
        variations = cart_item.variation.all()
        variation_dict ={}
        for variation in variations:        
            key = variation.variation_category
            value = variation.variation_value
            variation_dict[key] = value
        print('DEBUG variation_dict ', variation_dict)
    # 4 helper functions which needed to be created:
        #1. Get request parameter from url --> return dict
        #2. Turn 1 variation into a dictionary --> return dict of 1 variation
        #3. Check if a variation of a product already existed  in the cart  -->
            # --> if not exist , return False
            # --> if existed , return  the item itself
    # ********** END DEBUG ZONE
    

    # calculate total price before tax,tax and grand total
    total_tax_grandTotal = get_total_tax_grandTotal(cart)
   
    context ={
        'cart_items': cart_items,
        **total_tax_grandTotal
    }
    return render(request, 'store/cart.html', context)