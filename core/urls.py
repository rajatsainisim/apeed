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

    path('automation-testing/', automation_testing, name='automation-testing'),
    path('unit-testing/', unit_testing, name='unit-testing'),
    path('codecption/', codecption, name='codecption'),
    path('cucumber/', cucumber, name='cucumber'),
    path('selenium/', selenium, name='selenium'),

    # IoT Application Services

    path('iot-application-service/', iot_application_services, name='iot-application-service'),
    path('android-custom-rom-development/', android_custom_rom_development, name='android-custom-rom-development'),
    path('geekbox-rom/', geekbox_rom, name='geekbox-rom'),
    path('raspberry-pi/', raspberry_pi, name='raspberry-pi'),

    # Mobile App Development Services

    path('mobile-app-development-services/', mobile_app_development_services, name='mobile-app-development-services'),
    path('android-app-development/', android_app_development, name='android-app-development'),
    path('ios-app-development/', ios_app_development, name='ios-app-development'),
    path('flutter-app-development/', flutter_app_development, name='flutter-app-development'),
    path('hybrid-app-development/', hybrid_app_development, name='hybrid-app-development'),

    # Web Design Services
    path('web-design-services/', web_design_services, name='web-design-services'),
    path('website-redesign/', website_redesign, name='website-redesign'),
    path('graphic-design/', graphic_design, name='graphic-design'),
    path('mobile-application-design/', mobile_application_design, name='mobile-application-design'),
    path('responsive-web-design/', responsive_web_design, name='responsive-web-design'),
    path('logo-design/', logo_design, name='logo-design'),

    # Web Development Services

    path('web-development-services/', web_development_services, name='web-development-services'),
    path('api-integration-services/', api_integration_services, name='api-integration-services'),
    path('php-development/', php_development, name='php-development'),
    path('react-js-development/', react_js_development, name='react-js-development'),
    path('python-development/', python_development, name='python-development'),
    path('magento-development/', magento_development, name='magento-development'),
    path('wordpress-development-services/', wordpress_development_services, name='wordpress-development-services'),
    path('e-commerce-website-development/', e_commerce_website_development, name='e-commerce-website-development'),
    path('full-stack-development/', full_stack_development, name='full-stack-development'),
    path('progressive-web-apps/', progressive_web_apps, name='progressive-web-apps'),

    # Web Development Frameworks

    path('web-development-frameworks/', web_development_frameworks, name='web-development-frameworks'),
    path('node-js-framework/', node_js_framework, name='node-js-framework'),
    path('angular-js-framework/', angular_js_framework, name='angular-js-framework'),
    path('yii-framework/', yii_framework, name='yii-framework'),
    path('ruby-on-rails-development/', ruby_on_rails_development, name='ruby-on-rails-development'),
    path('django-framework/', django_framework, name='django-framework'),
    path('flask-framework/', flask_framework, name='flask-framework'),
    path('spring-boot-framework/', spring_boot_framework, name='spring-boot-framework'),
    path('laravel-development/', laravel_development, name='laravel-development'),

    # Digital Marketing Services

    path('digital-marketing-services/', digital_marketing_services, name='digital-marketing-services'),
    path('orm/', orm, name='orm'),
    path('smm/', smm, name='smm'),
    path('smo/', smo, name='smo'),
    path('seo/', seo, name='seo'),

    # ERP Software Development

    path('erp-software-development/', erp_software_development, name='erp-software-development'),
    path('inventory-management/', inventory_management, name='inventory-management'),
    path('project-management/', project_management, name='project-management'),
    path('human-resource-management/', human_resource_management, name='human-resource-management'),

    # Artificial Intelligence

    path('artificial-intelligence/', artificial_intelligence, name='artificial-intelligence'),
    path('chatbot-development/', chatbot_development, name='chatbot-development'),
    path('natural-language-processing/', natural_language_processing, name='natural-language-processing'),
    path('human-and-computer-vision/', human_and_computer_vision, name='human-and-computer-vision'),
    path('machine-learning/', machine_learning, name='machine-learning'),
    path('deep-learning/', deep_learning, name='deep-learning'),
    path('robotic-process-automation/', robotic_process_automation, name='robotic-process-automation'),
    path('alexa-app-development/', alexa_app_development, name='alexa-app-development'),

    # ------------------------------ # Hire Us #  --------------------------------------

    path('hireus/<id>', hireus, name='hireus'),

]
