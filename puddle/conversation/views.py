from django.shortcuts import get_object_or_404, redirect, render
from item.models import Item


def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
