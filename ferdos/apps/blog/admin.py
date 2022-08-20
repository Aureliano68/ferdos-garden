from django.contrib import admin
from .models import *

# Register your models here.

    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','family','job_title','mobile','status')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display=('group_article',)

@admin.register(article)
class articleAdmin(admin.ModelAdmin):
    list_display=('name_article','create_at','is_active')