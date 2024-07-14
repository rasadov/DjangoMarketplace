from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from item.models import Item, Category

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
            "items": items,
            "categories": categories,
        })

def contact(request):
    return render(request, "core/contact.html")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            
            user = authenticate(request, username=user.get_username(), password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = SignupForm()

    return render(request, "core/signup.html", {
            "form": form,
        })

def signout(request):
    request.session.flush()
    return redirect("/")