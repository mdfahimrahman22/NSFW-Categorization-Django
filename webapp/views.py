from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method=='POST':
        print(request.POST['radio-btn-input'])
    return render(request,'index.html')