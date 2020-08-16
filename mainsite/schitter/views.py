from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import Schitt

# Create your views here.
def index(request):
    latest_schitts = Schitt.objects.order_by('-pub_date')[:5]
    context = {'latest_schitts': latest_schitts}
    return render(request, 'schitter/index.html', context)

# Add a Schitt
def take_a_schitt(request):
    return render(request, 'schitter/take_a_schitt.html')

# Log the latest Schitt
def log_schitt(request):
    print(request.POST)
    # new_schitt = Schitt(name_text=request.POST['name'], schitt_text=request.POST['schitt'], pub_date=timezone.now())
    # new_schitt.save()
    return HttpResponseRedirect(reverse('index'))
