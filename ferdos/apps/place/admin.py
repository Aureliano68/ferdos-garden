from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(places)
class placeAdmin(admin.ModelAdmin):
    list_display=('place_name','visit_day','visit_hour','info','image')
    
@admin.register(visitor_group)
class visitorAdmin(admin.ModelAdmin):
        list_display=('type_name',)

@admin.register(ticketprice)
class ticketAdmin(admin.ModelAdmin):
        list_display=('visitor_group','places','price')

@admin.register(Mesaage)
class MesaageAdmin(admin.ModelAdmin):
        list_display=('fullname','email','subject','message','is_seen','regester')