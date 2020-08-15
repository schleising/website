from django.shortcuts import render

from .models import Twaat

# Create your views here.
def index(request):
    latest_twaats = Twaat.objects.order_by('-pub_date')[:5]
    context = {'latest_twaats': latest_twaats}
    return render(request, 'twatter/index.html', context)
