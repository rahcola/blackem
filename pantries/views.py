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
                              {'pantries': pantries,
                               'logged': True})

@login_required
def detail(request, pantry_id):
    pantry = get_object_or_404(Pantry, owner=request.user, pk=pantry_id)
    return render_to_response('pantries/pantry_detail.html',
                              {'pantry': pantry,
                               'logged': True})

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
                              {'form': form,
                               'logged': True},
                             context_instance=RequestContext(request))

@login_required
def delete(request, pantry_id):
    Pantry.objects.filter(pk=pantry_id, owner=request.user).delete()
    return redirect('blackem.users.views.home')

@login_required
def add_content(request, pantry_id, category_id=False, product_id=False):
    response_dict = {'pantry_id': pantry_id,
                     'categories': Category.objects.all(),
                     'logged': False}
    if product_id:
            if request.method == 'POST':
                form = ContentForm(request.POST)
                if form.is_valid():
                    try:
                        content = Content(pantry=Pantry.objects.get(pk=pantry_id,
                                                                    owner=request.user),
                                          product=Product.objects.get(pk=product_id),
                                          amount=form.cleaned_data["amount"])
                        content.save()
                        return redirect('pantries.views.detail', pantry_id)
                    except ObjectDoesNotExist:
                        return redirect('blackem.users.views.home')
            else:
                form = ContentForm()
            response_dict.update(
                {'form': form,
                 'product_id': product_id}
            )
    if category_id:
        response_dict.update(
            {'category_id': category_id,
             'products': Product.objects.filter(categories__pk=category_id)}
        )

    return render_to_response('pantries/content_form.html',
                              response_dict,
                              context_instance=RequestContext(request))

@login_required
def delete_content(request, pantry_id, content_id):
    Content.objects.filter(pk=content_id, pantry__owner=request.user).delete()
    return redirect('pantries.views.detail', pantry_id)

