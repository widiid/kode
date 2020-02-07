from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisForm


# Create your views here.
def index(request):
    submitted = False
    if request.method == 'POST':
        form = RegisForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/registrasi?submitted=True')
    else:
        form = RegisForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'registrasi/index.html', {'form': form, 'submitted': submitted})
