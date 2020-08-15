from django.shortcuts import render

from .models import Schitt

# Create your views here.
def index(request):
    latest_schittss = Schitt.objects.order_by('-pub_date')[:5]
    context = {'latest_schitts': latest_schittss}
    return render(request, 'schitter/index.html', context)
