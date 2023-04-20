from django.contrib import admin
from .models import Site, Photo_site, Guide_site,Visit_site

# Register your models here.

class SiteAdmin(admin.ModelAdmin):
    list_display=('name','description','location','province','country','budget')

class PhotoSiteAdmin(admin.ModelAdmin):
    list_display=('id_site','name','description','link')

class GuideSiteAdmin(admin.ModelAdmin):
    list_display=('id_site','dni','state')

admin.site.register(Site, SiteAdmin)
admin.site.register(Visit_site)
admin.site.register(Photo_site, PhotoSiteAdmin)
admin.site.register(Guide_site, GuideSiteAdmin)