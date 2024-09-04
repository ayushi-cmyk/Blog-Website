from django.shortcuts import render, HttpResponse
from .models import Category
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request,"index.html",{"categories": categories})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def view_details(request,id):
    detail = get_object_or_404(Category,pk=id)
    return render(request,"view.html",{"detail":detail})