from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, SearchForm
from .models import Contact


def home(request):
    return render(request, "sampark/home.html", context={})

def index(request):
    return render(request, "sampark/index.html", context={})

def sign_in(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, 'sampark/index.html', context={"firstname": firstname})
        else:
            messages.error(request, "Invalid username or password")
            return redirect('home')
        
    return render(request, "sampark/sign_in.html", context={})

def sign_up(request):
    
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        my_user = User.objects.create_user(username, email, password1)
        my_user.first_name = firstname
        my_user.last_name = lastname
        my_user.save()
        
        messages.success(request, "Your account has been successfully created")
        
        return redirect("sign_in")
            
        
        
    return render(request, "sampark/sign_up.html", context={})

def sign_out(request):
    return render(request, "sampark/sign_out.html", context={})

def contacts(request):
    user_contacts = Contact.objects.filter(user=request.user)
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        search_term = search_form.cleaned_data['search_term']
        user_contacts = user_contacts.filter(
            models.Q(name__icontains=search_term) |
            models.Q(phone_number__icontains=search_term) |
            models.Q(email__icontains=search_term)
        )
    return render(request, 'sampark/contacts.html', {'user_contacts': user_contacts, 'search_form': search_form})


@login_required
def add_contact(request):
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('contacts')
    else:
        print("Nothing")
        form = ContactForm()
        
    return render(request, "sampark/add_contact.html", context={'form': form})

@login_required
def sign_out(request):
    logout(request)
    return redirect('home')