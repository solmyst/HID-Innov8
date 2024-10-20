# import this to require login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# import this for sending email to user
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from .models import Profile
from .backends import HidPinBackend

# Create your views here.

@login_required(login_url='login')
def homepage(request):
    return render(request, 'homepage.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            hid = form.cleaned_data.get('hid')
            pin = form.cleaned_data.get('pin')
            profile = Profile.objects.create(user=user, hid=hid, pin=pin)
            user = authenticate(request, hid=hid, pin=pin, backend='authentication.backends.HidPinBackend')
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        hid = request.POST.get('hid')
        pin = request.POST.get('pin')
        user = authenticate(request, hid=hid, pin=pin, backend='authentication.backends.HidPinBackend')
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'authentication/login.html')


# to activate user from email
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'authentication/email_activation/activation_successful.html')
    else:
        return render(request, 'authentication/email_activation/activation_unsuccessful.html')

