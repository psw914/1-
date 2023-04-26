from django.contrib import admin
from .models import Foods

# Register your models here.
class DAdmin(admin.ModelAdmin):
    
    list_display = ("cook_year","cook_name","unit_price","count")
    list_filter = ["cook_year"]
    search_fields = ["cook_year","cook_name"]

admin.site.register(Foods,DAdmin)