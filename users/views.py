from django.shortcuts import render , redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request ,f'Welcome {username}, user accaunt created')
            return redirect("food:index")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {"form":form})
