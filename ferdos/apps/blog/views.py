from django.shortcuts import render

# Create your views here.
from urllib import response
from django.shortcuts import render
from .models import article
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.



def blog_show(request):
    articles=article.objects.all()
    context={
        'article':articles
    }
    return render(request,'blog/part_article.html',context)


def detail_article(request,id):
    articles=article.objects.get(id=id)
    context={
        'article':articles
    }
    return render(request,'blog/detail_article.html',context)

def article_download_pdf(request,id):
    if id==2:
        storage=FileSystemStorage()
        file_name='pdf_path/article_1.pdf'
        if storage.exists(file_name):
            with storage.open(file_name) as pdf:
                response=HttpResponse(pdf,content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename= "article_1.pdf"'
                return response

        else:
            HttpResponseNotFound('file not found') 
            
    elif id==1:
        storage=FileSystemStorage()
        file_name='pdf_path/article_2.pdf'
        if storage.exists(file_name):
            with storage.open(file_name) as pdf:
                response=HttpResponse(pdf,content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename= "article_1.pdf"'
                return response

        else:
            HttpResponseNotFound('file not found') 
        
            
    