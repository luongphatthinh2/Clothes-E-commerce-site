from django.shortcuts import get_object_or_404, render
from .models import Product
from Category_app.models import Category
# Create your views here.

def store(request, category_slug=None):    
    if category_slug :
        category = get_object_or_404(Category, category_name=category_slug)
        products = Product.objects.all().filter(category_id = category.id, is_available=True)
    else:        
        products = Product.objects.all().filter(is_available=True)   
    product_count = Product.objects.all().filter(is_available=True).count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    single_product = get_object_or_404(
        Product,
        slug=product_slug,
        category__category_name=category_slug
    )
    context = {
        'single_product': single_product
    }
    return render(request,'store/product_detail.html', context)