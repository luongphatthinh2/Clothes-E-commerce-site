from Store_app.models import Product
from django.http import HttpResponse
from django.shortcuts   import render

def home(request):
    products = Product.objects.all().filter(is_available=True)
    # print('DEBUG products',products)
    # for product in products:
    #     print(product.image.url)
    #     print(product.image.path)
    context ={
        'products':products
    }
    return render(request,  'home.html',context)

