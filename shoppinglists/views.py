from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from pantries.models import Pantry
from products.models import Category, Product
from shoppinglists.models import Shoppinglist, Item, ShoppinglistForm, ItemForm

@login_required
def detail(request, shoppinglist_id):
    list = get_object_or_404(Shoppinglist, pantry__owner=request.user,
                             pk=shoppinglist_id)
    return render_to_response('shoppinglists/shoppinglist_detail.html',
                              {'list': list,
                               'logged': True})

@login_required
def new(request):
    if request.method == 'POST':
        form = ShoppinglistForm(request.POST, my_user=False)
        if form.is_valid():
            try:
                list = Shoppinglist(name=form.cleaned_data['name'],
                                    pantry=form.cleaned_data['pantry'])
                list.save()
                return redirect('blackem.users.views.home')
            except ObjectDoesNotExist:
                return redirect('blackem.users.views.home')
    else:
        form = ShoppinglistForm(my_user=request.user)
    return render_to_response('shoppinglists/shoppinglist_form.html',
                              {'form': form,
                               'logged': True},
                              context_instance=RequestContext(request))

@login_required
def delete(request, shoppinglist_id):
    Shoppinglist.objects.filter(pk=shoppinglist_id,
                                pantry__owner=request.user).delete()
    return redirect('blackem.users.views.home')

def add_item(request, shoppinglist_id, category_id=False, product_id=False):
    response_dict = {'shoppinglist_id': shoppinglist_id,
                     'categories': Category.objects.all(),
                     'logged': False}
    if product_id:
            if request.method == 'POST':
                form = ItemForm(request.POST)
                if form.is_valid():
                    try:
                        item = Item(shoppinglist=Shoppinglist.objects.get(
                                        pk=shoppinglist_id,
                                        pantry__owner=request.user),
                                    product=Product.objects.get(pk=product_id),
                                    amount=form.cleaned_data["amount"],
                                    bought=False)
                        item.save()
                        return redirect('shoppinglists.views.detail',
                                        shoppinglist_id)
                    except ObjectDoesNotExist:
                        return redirect('blackem.users.views.home')
            else:
                form = ItemForm()
            response_dict.update(
                {'form': form,
                 'product_id': product_id}
            )
    if category_id:
        response_dict.update(
            {'category_id': category_id,
             'products': Product.objects.filter(categories__pk=category_id)}
        )

    return render_to_response('shoppinglists/item_form.html',
                              response_dict,
                              context_instance=RequestContext(request))

def delete_item(request, shoppinglist_id, item_id):
    Item.objects.filter(pk=item_id,
                        shoppinglist__pantry__owner=request.user).delete()
    return redirect('shoppinglists.views.detail', shoppinglist_id)
