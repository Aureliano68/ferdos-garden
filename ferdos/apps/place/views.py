from django.shortcuts import render,redirect
from .models import places,ticketprice,Mesaage
from django.http import HttpResponse,HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
from .forms import *



# Create your views here.
# --------------------------------------------------------------------------------------------------------------------------------------------
def placehistory(request):
        return render(request,'place/history.html')


# ---------------------------------------------------------------------------------- 
def placepart(request):
        place=places.objects.all()
        context={
            'place':place
        }
    
       
        return render(request,'place/part.html',context)


# ---------------------------------------------------------------------------------- 
def placepart_detail(request,id):
        place=places.objects.get(id=id)
        context={
            'place':place,
        }
        return render(request,'place/detail.html',context)


# ---------------------------------------------------------------------------------- 
def download_path_garden(request):
        fs=FileSystemStorage()
        file_name='pdf_path/ferdowsGardenPath.pdf'
        if fs.exists(file_name):
                with fs.open(file_name) as pdf:
                        response=HttpResponse(pdf,content_type='application/pdf')
                        response['Content-Disposition'] = 'attachment; filename= "erdowsGardenPath.pdf"'
                        return response
        else:
                HttpResponseNotFound('file not found')
                

                
def show_rule(request):
        place=places.objects.all()
        ticket_price=ticketprice.objects.all()
        context={
                'price':ticket_price,
                'place':place,
        }
        return render(request,'place/rule.html',context)

def message_show(request):
        forms=form_message(request.POST)
        if forms.is_valid():
                data=forms.cleaned_data
                msg=Mesaage()
                msg.fullname=data['full_name']
                msg.email=data['email']
                msg.subject=data['subject']
                msg.message=data['message']
                msg.save()
                return redirect('main:index')
        return render(request,'place/contact.html',{'form':forms})
                

        
        
       

