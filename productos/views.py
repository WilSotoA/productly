from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import ProductoForm
from .models import Producto


# Create your views here.
def index(req):
    productos = Producto.objects.all().values()
    return render(req, "index.html", context={"productos": productos})


def detail(req, id):
    producto = get_object_or_404(Producto, id=id)
    return render(req, "detail.html", context={"producto": producto})


def form(req):
    if req.method == "POST":
        form = ProductoForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/products")
    else:
        form = ProductoForm()
    return render(req, "form.html", {"form": form})
