from datetime import datetime, timedelta

from django.shortcuts import render

from products.models import Product
from wellcome.models import Home


# Create your views here.
def home(request):
    wellcome = Home.objects.all()
    products = Product.objects.all()
    new_date = datetime.now()
    old_flag_by_product_name = {}
    for product in products:
        created_naive = product.created.replace(tzinfo=None)  # Strip timezone info
        is_old = new_date - created_naive > timedelta(days=0.5)
        old_flag_by_product_name[product.name] = 0 if is_old else 1
    print(old_flag_by_product_name)
    context = {
        'wellcome': wellcome,
        'products': products,
        'product_name_by_old_flag': old_flag_by_product_name
    }

    return render(request, 'home.html', context)