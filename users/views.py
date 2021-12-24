from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import UserRegisterForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
        context = {
            'form': form,
        }
    return render(request, "signup.html", context)
