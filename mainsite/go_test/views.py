from django.shortcuts import render

# Create your views here.
def go_test(request):
    return render(request, 'go_test/index.html')

def go_canvas(request):
    return render(request, 'go_test/canvas.html')
