from django.contrib.sitemaps import Sitemap
from .models import Contact

class ContactSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Contact.objects.all()#filter(is_draft=False)

    def lastmod(self, obj):
        return obj.pub_date