from django.urls import path,include
from . import views


app_name='blog'

urlpatterns = [
    path('part/',views.blog_show,name='part'),
    path('detail/<int:id>',views.detail_article,name='detail'),



]