from django.contrib import admin
from .models import  *
# Register your models here.



class ServicesAdmin(admin.ModelAdmin):
    list_display = ('services', 'subservices')
    list_filter = ('services', )
    search_fields = ('services', 'subservices')

class HireusAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_filter = ('title', )

admin.site.register(Services)
admin.site.register(Subservices,ServicesAdmin)
admin.site.register(Hireus)
<<<<<<< HEAD
admin.site.register(Hireuseconn,HireusAdmin)
=======
admin.site.register(Hireuseconn)

admin.site.register(Contact_us)
>>>>>>> 1358e1a9603b8dd5c26f3acfbc4ca94bfba2e960
