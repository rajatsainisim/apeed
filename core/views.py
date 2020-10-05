from django.shortcuts import render
from .models import *

def index(request):
    title = 'Home'
    services_obj = Subservices.objects.all()
    # new_obj = Subservices.objects.get()
    hire_us = Hireuseconn.objects.all()
    return render(request, 'landing_page.html', {'title': title, 'services_obj': services_obj,'hire_us':hire_us})

def sitemaps(request):
    return request(request, 'sitemap.xml')


def product_home(request):
    return render(request, 'product/index.html')


def login(request):
    return render(request, 'product/landing_page/login.html')


# company

def about_us(request):
    return render(request, 'index/company/about-us.html')


def life_apeed(request):
    return render(request, 'index/company/life@apeed.html')


def clients(request):
    return render(request, 'index/company/clients_say.html')


# ------------------------------ # Services #  --------------------------------------


def service(request):
    return render(request, 'index/services/automation/automation-testing.html')


# ------------------------------ # Hire Us #  --------------------------------------

def hireus(request,id):
    hire_us = Hireuseconn.objects.get(id=id)
    title = 'Hire Us',hire_us.title
    return render(request, 'index/hire_us/hireus.html',{'title':title,'data':hire_us})

