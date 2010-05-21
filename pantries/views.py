from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from pantries.models import Pantry, Content

@login_required
def index(request):
    pantries = get_list_or_404(Pantry, owner=request.user)
    return render_to_response('pantries/index.html', {'pantries': pantries, 'user': request.user})

@login_required
def show(request, pantry_id):
    pantry = get_object_or_404(Pantry, owner=request.user, pk=pantry_id)
    contents = pantry.content_set.all()
    return render_to_response('pantries/show.html', {'pantry': pantry, 'contents': contents})
