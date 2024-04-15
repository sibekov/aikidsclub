from django.shortcuts import render,redirect
from .models import Item
# Create your views here.


def kidstodo(request):
    items = Item.objects.all()
    context = {
        'items':items
    }
    return render(request,'aikidsapp/aikids_items.html',context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)
        
        return redirect('kidstodo')
    return render(request,'aikidsapp/add_item.html')
