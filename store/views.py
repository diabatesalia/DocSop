from django.shortcuts import render, get_object_or_404
from store.models import Product
from django.core.paginator import Paginator

def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        products = Product.objects.filter(name__icontains=item_name)
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'store/index.html', context={"products": products})

def detail(request, myid):
    product = Product.objects.get(id=myid)
    return render(request, 'store/detail.html', context={"product": product})

