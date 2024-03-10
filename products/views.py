from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)

# def test_context(request):
# context = {
#         'name'  : 'alex',
#         'age'   : 30,
#         'header': 'Добро пожаловать',
#         'products': [
#                 {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
#                 {'name': 'Синяя куртка The North Face', 'price': 23725.00},
#                 {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
#         ],
#         'promotion': True,
#         'products_of_promotion': [
#                 {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},
#         ]
# }
# return render(request, 'products/test_context.html', context)
