from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .models import Item
from .forms import NewItemForm, EditItemForm

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    related_items = Item.objects.filter(category=item.category).exclude(pk=item_id)
    return render(request=request,
                  template_name="item/detail.html",
                  context={
                    "item": item,
                    "related_items": related_items
                    })

@login_required
def new_item(request):
    if request.method == "POST":
      form = NewItemForm(request.POST, request.FILES)
      if form.is_valid():
          item = form.save(commit=False)
          item.created_by = request.user
          item.save()
          return redirect("item:detail", item_id=item.id)
    else:
        form = NewItemForm()
    return render(request=request,
                  template_name="item/form.html",
                  context={
                      "form": form,
                      "route": '/item/new/',
                      })

@login_required
def delete(request, pk):
    if request.user != Item.objects.get(pk=pk).created_by:
        messages.error(request, "You are not authorized to delete this item.")
        return redirect("/dash/")
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect("/dash/")

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.user != Item.objects.get(pk=pk).created_by:
        messages.error(request, "You are not authorized to edit this item.")
        return redirect("/dash/")
    
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item:detail", item_id=item.id)
    else:
        form = EditItemForm(instance=item)
    
    return render(request=request,
                  template_name="item/form.html",
                  context={
                      "form": form,
                        "route": '/item/edit/' + str(pk) + '/',
                      })
