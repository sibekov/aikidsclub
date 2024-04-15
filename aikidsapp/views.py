from django.shortcuts import render
from .models import Item
# Create your views here.


def kidstodo(request):
    items = Item.objects.all()
    context = {
        'items':items
    }
    return render(request,'aikidsapp/aikids_items.html',context)
