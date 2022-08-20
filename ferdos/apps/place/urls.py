from django.urls import path
from .views import *

app_name='place'
urlpatterns = [
    path('history/',placehistory,name='history'),
    path('part/',placepart,name='part'),
    path('detail/<int:id>/',placepart_detail,name='detail'),
    path('pdf_path/',download_path_garden,name='pdf_path'),
    path('rule/',show_rule,name='rule'),
    path('contact/',message_show,name='contact'),







]