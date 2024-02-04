from django.shortcuts import render

# Create your views here.
def inde(request):
    return render(request,'base.html')
