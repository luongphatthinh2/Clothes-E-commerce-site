from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Product
from Category_app.models import Category
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def store(request, category_slug=None):    
    if category_slug : # with category filterd
        category = get_object_or_404(Category, category_name=category_slug)
        products = Product.objects.all().filter(category_id = category.id, is_available=True).order_by('product_name')
        paginator = Paginator(products, 3) # shows 3 products per page        
    else: # no category filterd  
        products = Product.objects.all().filter(is_available=True).order_by('product_name')
        paginator = Paginator(products, 3) # shows 3 products per page
   
    page_number = request.GET.get('page') # when first visit /store, the page_number is none
    page_obj = paginator.get_page(page_number)
    product_count = page_obj.object_list.count
    context = {
        'product_count': product_count,
        'page_obj': page_obj,
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

def search_product(request):
    keyword = request.GET.get('keyword') # keyword will be '' if the search field is blank
    if keyword == '' or keyword.isspace():
        return redirect(request.META['HTTP_REFERER'])
    products = Product.objects.filter(
        Q(product_name__icontains=keyword) | Q(description__icontains=keyword)
    )
    paginator = Paginator(products, 3) # shows 3 products per page
    page_number = request.GET.get('page') # when first visit /store, the page_number is none
    page_obj = paginator.get_page(page_number)
    product_count = page_obj.paginator.count
    print('DEBUG  page_obj.paginator.count ', page_obj.paginator.count)
    context = {
        'product_count': product_count,
        'page_obj': page_obj,
        'keyword':keyword
    }
    return render(request, 'store/searchResult_store.html', context)