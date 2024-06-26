from django.shortcuts import render,redirect,get_object_or_404
from .models import Item
from .forms import ItemForm
from django.views import generic


# Create your views here.


def kidstodo(request):
    items = Item.objects.all()
    completed = len(items.filter(done=True))
    print(f'completed : {completed}')
    context = {
        'items':items,
        'completed' : completed

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


def edit_item(request, item_id):
    item = get_object_or_404(Item,id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('kidstodo')
    form = ItemForm(instance=item)
    context = {
        'form':form
    }
    return render(request,'aikidsapp/edit_item.html',context)


def toggle_item(request,item_id):
     item = get_object_or_404(Item,id=item_id)
     item.done = not item.done
     item.save()
     return redirect('kidstodo')


def delete_item(request,item_id):
     item = get_object_or_404(Item,id=item_id)
     item.delete()
     return redirect('kidstodo')