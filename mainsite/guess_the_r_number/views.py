from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'guess_the_r_number/index.html')
