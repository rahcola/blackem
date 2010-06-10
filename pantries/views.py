from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from pantries.models import Pantry, Content, PantryForm

@login_required
def index(request):
    pantries = get_list_or_404(Pantry, owner=request.user)
    return render_to_response('pantries/index.html', {'pantries': pantries, 'user': request.user})

@login_required
def show(request, pantry_id):
    pantry = get_object_or_404(Pantry, owner=request.user, pk=pantry_id)
    contents = pantry.content_set.all()
    return render_to_response('pantries/show.html', {'pantry': pantry, 'contents': contents})

@login_required
def new(request):
    if request.method == 'POST':
        print 'jee'
        form = PantryForm(request.POST)
        if form.is_valid():
            pantry = Pantry(name=request.POST['name'], owner=request.user)
            pantry.save()
            return redirect('blackem.users.views.home')
    else:
        form = PantryForm()
        return render_to_response('pantries/pantry_form.html', {'form': form},
                                 context_instance=RequestContext(request))
