from django.shortcuts import render
from .models import Contact
# Create your views here.
def homeview(request):
    return render(request,'index.html')

def aboutview(request):
    return render(request,'about.html')

def portfolioview(request):
    return render(request,'portfolio.html')

def priceview(request):
    return render(request,'price.html')

def servicesview(request):
    return render(request,'services.html')

def contactview(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact(name = name,email = email,subject = subject,message=message)
        data.save()
    return render(request,'contact.html')