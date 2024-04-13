from django.shortcuts import render

# Create your views here.
def kidstodo(request):
    return render(request,'aikidsapp/aikids_items.html')