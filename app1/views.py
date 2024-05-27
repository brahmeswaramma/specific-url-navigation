from django.shortcuts import render

# Create your views here.
def bus(request):
    return render(request,'bus.html')