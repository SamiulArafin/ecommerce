from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

User = get_user_model()


def home_page(request):
    context = {
        "title": "Home Page",
        "content": "Hellow From Home Page",
        "premium_content": "Hhhhhhhhhhhhhhhh"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": "Hellow From About Page"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page",
        "content": "Hello From Contact Page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


def login_page(request):
    login_form = LoginForm(request.POST or None)

    context = {
        "loginForm": login_form
    }
    # print(request.user.is_authenticated)
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # context['loginForm'] = LoginForm
            return redirect("/")
        else:
            print("Error in Logged In")

    return render(request, "auth/login.html", context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = User.objects.create_user(username, email, password)
        print(user)
    return render(request, "auth/register.html", context)
