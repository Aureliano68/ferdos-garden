from django.urls import path,include
from . import views


app_name='blog'

urlpatterns = [
    path('part/',views.blog_show,name='part'),
    path('detail/<int:id>',views.detail_article,name='detail'),
    path('pdf_path1/<int:id>',views.article_download_pdf,name='pdf_path1'),

    



]