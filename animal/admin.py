from django.contrib import admin
from animal.models import Advert
# Register your models here.

class AdvertAdmin(admin.ModelAdmin):
    fields = ['title','category','date','place','description','photo','price','sex']


admin.site.register(Advert, AdvertAdmin)
