from django.shortcuts import render,get_object_or_404
from .models import Product
# Create your views here.
def baidu(request):
    return render(request,"baidu.html")

def index(request):
    products = Product.objects.all()  # 获取所有产品
    return render(request, 'index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})