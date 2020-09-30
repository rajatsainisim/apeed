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


def about_us(request):
    return render(request, 'index/company/about_us.html')
