from django.shortcuts import render,redirect
from .models import Item
from .forms import ItemForm
# Create your views here.


def kidstodo(request):
    items = Item.objects.all()
    context = {
        'items':items
    }
    return render(request,'aikidsapp/aikids_items.html',context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kidstodo')
        
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request,'aikidsapp/add_item.html',context)
