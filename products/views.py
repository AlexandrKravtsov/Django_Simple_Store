from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from products.models import Product, ProductCategory, Basket


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {
        'title': 'Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        context.update({'products': Product.objects.filter(category_id=category_id)})
    else:
        context.update({'products': Product.objects.all()})
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')

    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
