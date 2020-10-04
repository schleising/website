from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'LeafletMaps/index.html')

def uk_cumulative_cases(request):
    return render(request, 'LeafletMaps/uk_cumulative_cases.html')
