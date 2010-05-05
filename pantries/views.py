from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from pantries.models import Pantry, Content

def index(request):
    if not request.user.is_authenticated():
        return HttpResponse("Not log in.")
    else:
        pantries = get_list_or_404(Pantry, owner=request.user)
        return render_to_response('pantries/index.html', {'pantries': pantries, 'user': request.user})

def show(request, pantry_id):
    if not request.user.is_authenticated():
        return HttpResponse("Not log in.")
    else:
        pantry = get_object_or_404(Pantry, owner=request.user, pk=pantry_id)
        contents = pantry.content_set.all()
        return render_to_response('pantries/show.html', {'pantry': pantry, 'contents': contents})
