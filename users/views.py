from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from pantries.models import Pantry

@login_required
def home(request):
    pantries = Pantry.objects.filter(owner=request.user)
    return render_to_response('users/home.html', {'pantries': pantries})
