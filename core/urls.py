from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import ContactSitemap
from . import views
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .views import *

sitemaps = {
    'static': ContactSitemap,
}
urlpatterns = [
    path('', index),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    path('product/', views.product_home, name='product'),
    path('login/', views.login, name='login'),

    # company

    path('about-us/', about_us, name='about-us'),
    path('life-apeed/', life_apeed, name='life-apeed'),
    path('clients/', clients, name='clients'),

    # services
    path('service/<id>', service, name='services'),

    # ------------------------------ # Hire Us #  --------------------------------------
    path('hireus/<id>', hireus, name='hireus'),

    path('hireus/<id>', hireus, name='hireus'),

    # ------------------------------ # Contact Us #  --------------------------------------

    path('contact-us/', contact_us, name='contact-us'),

    # ------------------------------ # Portfolio #  --------------------------------------

    path('portfolio/', portfolio, name='portfolio'),

    # ------------------------------ # career #  --------------------------------------

    path('career/', career, name='career'),

    # ------------------------------ # Blog #  --------------------------------------
    path('blog/', blog, name='blog'),

    # ------------------------------ # Get In Touch #  --------------------------------------

    path('contact-request/', contact_request, name='contact-request'),

]
