from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def get_todo_list(request):
    """Create views here."""
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo/todo_list.html", context)

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.seve()
            # name = request.POSTget('item_name')
            # done = done in request.POST
            # Item.Objects.create(name=name, done=done)
            return redirect('get_todo_list')

    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method =='POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.seve()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/etit_item.html', context)