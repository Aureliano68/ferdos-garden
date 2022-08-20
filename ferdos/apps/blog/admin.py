from django.contrib import admin
from .models import article

# Register your models here.

@admin.register(article)
class articleAdmin(admin.ModelAdmin):
    list_display=('name','is_active')
    
