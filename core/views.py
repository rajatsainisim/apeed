from django.shortcuts import render
from .models import *

def index(request):
    title = 'Home'
    services_obj = Subservices.objects.all()
    print(services_obj)
    return render(request, 'landing_page.html', {'title': title, 'services_obj': services_obj})



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


def automation_testing(request):
    return render(request, 'index/services/automation/automation-testing.html')


def unit_testing(request):
    return render(request, 'index/services/automation/unit-testing.html')


def codecption(request):
    return render(request, 'index/services/automation/codecption.html')


def cucumber(request):
    return render(request, 'index/services/automation/cucumber.html')


def selenium(request):
    return render(request, 'index/services/automation/selenium.html')


# IoT Application Services

def iot_application_services(request):
    return render(request, 'index/services/iot/iot-application-services.html')


def android_custom_rom_development(request):
    return render(request, 'index/services/iot/android-custom-rom-development.html')


def geekbox_rom(request):
    return render(request, 'index/services/iot/geekbox-rom.html')


def raspberry_pi(request):
    return render(request, 'index/services/iot/raspberry-pi.html')


# Mobile App Development Services
def mobile_app_development_services(request):
    return render(request, 'index/services/mobile_app/mobile-app-development-services.html')


def android_app_development(request):
    return render(request, 'index/services/mobile_app/android-app-development.html')


def ios_app_development(request):
    return render(request, 'index/services/mobile_app/ios-app-development.html')


def flutter_app_development(request):
    return render(request, 'index/services/mobile_app/flutter-app-development.html')


def hybrid_app_development(request):
    return render(request, 'index/services/mobile_app/hybrid-app-development.html')

    # Web Design Services


def web_design_services(request):
    return render(request, 'index/services/web_design/web-design-services.html')


def website_redesign(request):
    return render(request, 'index/services/web_design/website-redesign.html')


def graphic_design(request):
    return render(request, 'index/services/web_design/graphic-design.html')


def mobile_application_design(request):
    return render(request, 'index/services/web_design/mobile-application-design.html')


def responsive_web_design(request):
    return render(request, 'index/services/web_design/responsive-web-design.html')


def logo_design(request):
    return render(request, 'index/services/web_design/logo-design.html')


# Web Development Services

def web_development_services(request):
    return render(request, 'index/services/web_development_services/web-development-services.html')


def api_integration_services(request):
    return render(request, 'index/services/web_development_services/api-integration-services.html')


def php_development(request):
    return render(request, 'index/services/web_development_services/php-development.html')


def react_js_development(request):
    return render(request, 'index/services/web_development_services/react-js-development.html')


def python_development(request):
    return render(request, 'index/services/web_development_services/python-development.html')


def magento_development(request):
    return render(request, 'index/services/web_development_services/magento-development.html')


def wordpress_development_services(request):
    return render(request, 'index/services/web_development_services/wordpress-development-services.html')


def e_commerce_website_development(request):
    return render(request, 'index/services/web_development_services/e-commerce-website-development.html')


def full_stack_development(request):
    return render(request, 'index/services/web_development_services/full-stack-development.html')


def progressive_web_apps(request):
    return render(request, 'index/services/web_development_services/progressive-web-apps.html')

    # Web Development Frameworks


def web_development_frameworks(request):
    return render(request, 'index/services/web_development_frameworks/web-development-frameworks.html')


def node_js_framework(request):
    return render(request, 'index/services/web_development_frameworks/node-js-framework.html')


def angular_js_framework(request):
    return render(request, 'index/services/web_development_frameworks/angular-js-framework.html')


def yii_framework(request):
    return render(request, 'index/services/web_development_frameworks/yii-framework.html')


def ruby_on_rails_development(request):
    return render(request, 'index/services/web_development_frameworks/ruby-on-rails-development.html')


def django_framework(request):
    return render(request, 'index/services/web_development_frameworks/django-framework.html')


def flask_framework(request):
    return render(request, 'index/services/web_development_frameworks/flask-framework.html')


def spring_boot_framework(request):
    return render(request, 'index/services/web_development_frameworks/spring-boot-framework.html')


def laravel_development(request):
    return render(request, 'index/services/web_development_frameworks/laravel-development.html')

    # Digital Marketing Services


def digital_marketing_services(request):
    return render(request, 'index/services/digital_marketing_services/digital-marketing-services.html')


def orm(request):
    return render(request, 'index/services/digital_marketing_services/orm.html')


def smm(request):
    return render(request, 'index/services/digital_marketing_services/smm.html')


def smo(request):
    return render(request, 'index/services/digital_marketing_services/smo.html')


def seo(request):
    return render(request, 'index/services/digital_marketing_services/seo.html')

    # ERP Software Development


def erp_software_development(request):
    return render(request, 'index/services/erp/erp-software-development.html')


def inventory_management(request):
    return render(request, 'index/services/erp/inventory-management.html')


def project_management(request):
    return render(request, 'index/services/erp/project-management.html')


def human_resource_management(request):
    return render(request, 'index/services/erp/human-resource-management.html')

    # Artificial Intelligence


def artificial_intelligence(request):
    return render(request, 'index/services/artificial/artificial-intelligence.html')


def chatbot_development(request):
    return render(request, 'index/services/artificial/chatbot-development.html')


def natural_language_processing(request):
    return render(request, 'index/services/artificial/natural-language-processing.html')


def human_and_computer_vision(request):
    return render(request, 'index/services/artificial/human-and-computer-vision.html')


def machine_learning(request):
    return render(request, 'index/services/artificial/machine-learning.html')


def deep_learning(request):
    return render(request, 'index/services/artificial/deep-learning.html')


def robotic_process_automation(request):
    return render(request, 'index/services/artificial/robotic-process-automation.html')


def alexa_app_development(request):
    return render(request, 'index/services/artificial/alexa-app-development.html')

# ------------------------------ # Hire Us #  --------------------------------------

def hire_magento_developer(request):
    return render(request, 'index/hire_us/hire-magento-developer.html')

