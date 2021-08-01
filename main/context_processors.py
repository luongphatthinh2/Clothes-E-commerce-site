from django.urls import reverse
from Category_app.models import Category

# def common_link(request):
#     common_link={}
#     common_link['store'] = reverse('store')
#     common_link['home'] = reverse('home')
#     # print('DEBUG common_link', common_link['store'])
#     return common_link



def categories_link(request):
    categories_link = Category.objects.all()
    return {'categories_link' : categories_link}