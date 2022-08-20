from django.urls import path,include
from . import views


app_name='main'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.usercreate.as_view(),name='usercreate'),


]