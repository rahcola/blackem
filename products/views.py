from django.shortcuts import render_to_response, get_object_or_404
from products.models import Product

def index(request):
    product_list = Product.objects.all()
    return render_to_response('products/index.html', {'product_list': product_list})

def show(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    return render_to_response('products/show.html', {'product': p})

