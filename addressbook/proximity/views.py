from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Contact
from .forms import ContactForm
# Create your views here.

def index(request):
    return render(request, 'proximity/index.html')


def sign_in(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            contacts = Contact.objects.filter(user=user)
            return render(request, 'proximity/home.html', context={"firstname": firstname, 'contacts': contacts})
        else:
            messages.error(request, "Invalid username or password")
            return redirect('index')
        
        
    return render(request, 'proximity/sign_in.html')

def signup(request):
    
    if request.method == "POST":
        # username = request.POST.get('username')
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
        
    return render(request, 'proximity/signup.html')

def add_contact(request):
    
    contactForm = ContactForm()
    if request.method == "POST":
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            contactForm = contactForm.save(commit=False)
            contactForm.user = request.user
            contactForm.save()
            return redirect("home")
    
    return render(request, 'proximity/add_contact.html', context={'contactForm': contactForm})
    
def sign_out(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index')

def home(request):
    
    return render(request, "proximity/home.html")