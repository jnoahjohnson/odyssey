from django.shortcuts import render

# Create your views here.
def indexPageView(request):
    return render(request, 'library/index.html')