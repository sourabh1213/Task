from django.shortcuts import render
from .models import *
from login.views import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'Product' : products,
    }
    return render(request, 'home/home.html', context)

def details(request, pk):
    if request.user.is_authenticated:
        products = Product.objects.get(id=pk)
        context = {
            'Product' : products,
        }
        return render(request, 'home/detail.html', context)
    else:
        return redirect('login')

def update(request):
    edt= Product.objects.get(pk=id)
    fm = Product(request, instace = edt)
    if fm.is_valid():
        fm.save()
        messages.info(request, 'Updated Successfully')
    else:
        messages.error(request, 'Not Save')
    return details(request, {'form':fm})