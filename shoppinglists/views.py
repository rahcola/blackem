from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.template import RequestContext
from pantries.models import Pantry, Content
from products.models import Category, Product
from shoppinglists.models import Shoppinglist, Item, ShoppinglistForm, ItemForm

@login_required
def detail(request, shoppinglist_id):
    """Detailed view of the shoppinglist.

    List all items and give forms to check them as bought. Bought items are
    added to the pantry of this shoppinglist.

    """
    CheckItemFormSet = modelformset_factory(Item, extra=0, fields=('bought',))
    if request.method == 'POST':
        formset = CheckItemFormSet(request.POST)
        if formset.is_valid():
            for form in formset.forms:
                if form.cleaned_data['bought']:
                    item = get_object_or_404(Item,
                                             pk=form.cleaned_data['id'].pk,
                                             shoppinglist__pantry__owner=request.user)
                    if not item.bought:
                        try:
                            content = Content.objects.get(
                                product=item.product,
                                pantry=item.shoppinglist.pantry
                            )
                            content.amount += item.amount
                        except ObjectDoesNotExist:
                            content = Content(pantry=item.shoppinglist.pantry,
                                              product=item.product,
                                              amount=item.amount)
                        content.save()
                    item.delete()

    list = get_object_or_404(Shoppinglist,
                             pantry__owner=request.user,
                             pk=shoppinglist_id)
    formset = CheckItemFormSet(queryset=Item.objects.filter(shoppinglist=list))
    return render_to_response('shoppinglists/shoppinglist_detail.html',
                              {'items': zip(list.item_set.all(), formset.forms),
                               'formset': formset,
                               'list': list,
                               'logged': True},
                                context_instance=RequestContext(request))

@login_required
def new(request):
    """Create a new shoppinglist or render the appropriate form.
    
    Shoppinglist are always bound to a single pantry, to which bough items are
    added.
    
    """
    if request.method == 'POST':
        form = ShoppinglistForm(request.POST, my_user=False)
        if form.is_valid():
            pantry = get_object_or_404(Pantry,
                                       pk=form.cleaned_data['pantry'].id)
            list = Shoppinglist(name=form.cleaned_data['name'],
                                pantry=pantry)
            list.save()
            return redirect('blackem.users.views.home')
    else:
        form = ShoppinglistForm(my_user=request.user)
    return render_to_response('shoppinglists/shoppinglist_form.html',
                              {'form': form,
                               'logged': True},
                              context_instance=RequestContext(request))

@login_required
def delete(request, shoppinglist_id):
    """Delete the shoppinglist.

    User can only delete their own shoppinglists.

    """
    Shoppinglist.objects.filter(pk=shoppinglist_id,
                                pantry__owner=request.user).delete()
    return redirect('blackem.users.views.home')

def add_item(request, shoppinglist_id, category_id=False, product_id=False):
    """Add item to shoppinglist.

    Product to add is prompted in three steps:
    1. Ask for a category.
    2. Ask for a product in choosen category.
    3. Ask for an amount for the choosen product.

    User can only add items to their own shoppinglists.

    """
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            shoppinglist = get_object_or_404(
                Shoppinglist,
                pk=shoppinglist_id,
                pantry__owner=request.user
            )
            product = get_object_or_404(Product, pk=product_id)
            try:
                item = Item.objects.get(shoppinglist=shoppinglist,
                                        product=product)
                item.amount += form.cleaned_data['amount']
            except ObjectDoesNotExist:
                item = Item(shoppinglist=shoppinglist,
                            product=product,
                            amount=form.cleaned_data['amount'],
                            bought=False)
            item.save()
        return redirect('shoppinglists.views.detail', shoppinglist_id)

    response_dict = {'shoppinglist_id': shoppinglist_id,
                     'categories': Category.objects.all(),
                     'logged': False}
    if category_id:
        response_dict.update(
            {'category_id': category_id,
             'category': Category.objects.get(pk=category_id),
             'products': Product.objects.filter(categories__pk=category_id)}
        )
    if product_id:
        response_dict.update(
            {'form': ItemForm(),
             'product': Product.objects.get(pk=product_id),
             'product_id': product_id}
        )
    return render_to_response('shoppinglists/item_form.html',
                              response_dict,
                              context_instance=RequestContext(request))

def delete_item(request, shoppinglist_id, item_id):
    """Delete the item from the shoppinglist.

    User can only delete items from their own shoppinglists.

    """
    Item.objects.filter(pk=item_id,
                        shoppinglist__pantry__owner=request.user).delete()
    return redirect('shoppinglists.views.detail', shoppinglist_id)
