from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto


# Create your views here.
def index(req):
    productos = Producto.objects.all().values()
    return render(req, "index.html", context={"productos": productos})
