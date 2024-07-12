from django.shortcuts import get_object_or_404, render

from .models import Item

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    related_items = Item.objects.filter(category=item.category).exclude(pk=item_id)
    return render(request=request,
                  template_name="item/detail.html",
                  context={
                    "item": item,
                    "related_items": related_items
                    })
