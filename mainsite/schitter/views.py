from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import Schitt

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        latest_schitts = Schitt.objects.order_by('-pub_date')[:5]
        context = {'latest_schitts': latest_schitts}
        return render(request, 'schitter/index.html', context)
    
    else:
        return HttpResponseRedirect(reverse('login'))

# Add a Schitt
def take_a_schitt(request):
    if request.user.is_authenticated:
        return render(request, 'schitter/take_a_schitt.html')
    
    else:
        return HttpResponseRedirect(reverse('login'))

# Log the latest Schitt
def log_schitt(request):
    if request.user.is_authenticated:
        print(request.user)
        new_schitt = Schitt(name_text=request.user, schitt_text=request.POST['schitt'], pub_date=timezone.now())
        new_schitt.save()
        return HttpResponseRedirect(reverse('schitter'))
    
    else:
        return HttpResponseRedirect(reverse('login'))
