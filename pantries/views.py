from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils import simplejson
from django.http import HttpResponse
from pantries.models import Pantry, Content, PantryForm, ContentForm
from products.models import Product, Category

@login_required
def list(request):
    pantries = get_list_or_404(Pantry, owner=request.user)
    return render_to_response('pantries/pantry_list.html',
                              {'pantries': pantries})

@login_required
def detail(request, pantry_id):
    pantry = get_object_or_404(Pantry, owner=request.user, pk=pantry_id)
    return render_to_response('pantries/pantry_detail.html',
                              {'pantry': pantry})

@login_required
def new(request):
    if request.method == 'POST':
        form = PantryForm(request.POST)
        if form.is_valid():
            pantry = Pantry(name=form.cleaned_data["name"], owner=request.user)
            pantry.save()
            return redirect('blackem.users.views.home')
    else:
        form = PantryForm()
    return render_to_response('pantries/pantry_form.html',
                              {'form': form},
                             context_instance=RequestContext(request))

@login_required
def delete(request, pantry_id):
    Pantry.objects.filter(pk=pantry_id, owner=request.user).delete()
    return redirect('blackem.users.views.home')

@login_required
def add_content(request, pantry_id, category_id=False, product_id=False):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            pantry = get_object_or_404(Pantry,
                                       pk=pantry_id,
                                       owner=request.user)
            product = get_object_or_404(Product, pk=product_id)
            try:
                content = Content.objects.get(pantry=pantry, product=product)
                content.amount += form.cleaned_data['amount']
            except ObjectDoesNotExist:
                content = Content(pantry=pantry,
                                  product=product,
                                  amount=form.cleaned_data['amount'])
            content.save()
        return redirect('pantries.views.detail', pantry_id)

    response_dict = {'pantry_id': pantry_id,
                     'categories': Category.objects.all(),
                     'no_logout': True}
    if category_id:
        response_dict.update(
            {'category_id': category_id,
             'products': Product.objects.filter(categories__pk=category_id)}
        )

    if product_id:
        response_dict.update(
            {'form': ContentForm(),
             'product_id': product_id}
        )
    return render_to_response('pantries/content_form.html',
                              response_dict,
                              context_instance=RequestContext(request))

@login_required
def delete_content(request, pantry_id, content_id):
    Content.objects.filter(pk=content_id, pantry__owner=request.user).delete()
    return redirect('pantries.views.detail', pantry_id)

