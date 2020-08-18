from django.shortcuts import render
from django.http import HttpResponse
def about(request):
   return render(request, 'about.html')
def blog_home(request):
    return render(request, 'blog_home.html')
def blog_single(request):
    return render(request, 'blog_single.html')
def contact(request):
    return render(request, 'contact.html')
def elements(request):
    return render(request, 'elements.html')
def index(request):
    return render(request, 'index.html')
def opening_hour(request):
    return render(request, 'opening_hour.html')
def pricing(request):
    return render(request, 'pricing.html')
def services(request):
    return render(request, 'services.html')    
