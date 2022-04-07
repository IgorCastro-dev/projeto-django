from django.shortcuts import render

from core.models import Produto


# Create your views here.
def index(request):
    produto = Produto.objects.all()
    context = {
        "produtos":produto
    }
    return render(request,'index.html',context)

def produto(request,pk):
    prod = Produto.objects.get(id=pk)
    context = {
        "produto":prod
    }
    return render(request,'produto.html',context)