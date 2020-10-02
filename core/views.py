from django.shortcuts import render


def index(request):
    title = 'Home'
    return render(request, 'landing_page.html', {'title': title})


def sitemaps(request):
    return request(request, 'sitemap.xml')


def product_home(request):
    return render(request, 'product/landing_page/product_home.html')


def login(request):
    return render(request, 'product/landing_page/login.html')


# company

def about_us(request):
    return render(request, 'index/company/about-us.html')


def life_apeed(request):
    return render(request, 'index/company/life@apeed.html')


def clients(request):
    return render(request, 'index/company/clients_say.html')

# Services

def automation_testing(request):
    return render(request,'index/services/automation/automation-testing.html')


