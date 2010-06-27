from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from users.models import RegistrationForm
from pantries.models import Pantry
from shoppinglists.models import Shoppinglist

@login_required
def home(request):
    """Home page.

    List users pantries and shoppinglists. If user has permissions to add
    products (and categories) pass this info to the template.

    """
    admin = False
    if request.user.has_perm('products.add_product'):
        admin = True
    pantries = Pantry.objects.filter(owner=request.user)
    lists = Shoppinglist.objects.filter(pantry__owner=request.user)
    return render_to_response('users/home.html', {'pantries': pantries,
                                                  'lists': lists,
                                                  'logged': True,
                                                  'admin': admin,
                                                  'home': True})

def register(request):
    """Create the user or render the approriate form.

    Users are created without any permissions.

    """
    if request.user.is_authenticated():
        return redirect('blackem.users.views.home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blackem.users.views.home')
    else:
        form = RegistrationForm()
    return render_to_response('users/user_form.html',
                              {'form': form,
                               'logged': False},
                              context_instance=RequestContext(request))
