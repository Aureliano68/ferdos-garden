from distutils.command.upload import upload
from xml.parsers.expat import model
from django.db import models
from django.utils import timezone

# Create your models here.
# --------------------------------------------------------------------------------------------------------------------------------------

class places(models.Model):
    place_name=models.CharField(max_length=50,verbose_name='نام مکان')
    info=models.TextField(verbose_name='توضیحات')
    image=models.ImageField(upload_to='image/places/',verbose_name='تصویر')
    visit_day=models.CharField(max_length=60,verbose_name='روز بازدید')
    visit_hour=models.CharField(max_length=60,verbose_name='ساعت بازدید')
    rules=models.TextField(verbose_name=' قوانین و مقررات')
    regester=models.DateField(default=timezone.now,verbose_name='تاریخ ثبت')

    def __str__(self) :
        return f'{self.place_name}'
    
    class Meta:
        db_table = 'place_db'
        managed = True
        verbose_name = 'مکان'
        verbose_name_plural = 'مکان ها'
        
        
# --------------------------------------------------------------------------------------------------------------
class visitor_group(models.Model):
    type_name=models.CharField(max_length=50,verbose_name="نوع بازدید کننده")
    
    def __str__(self) :
        return f'{self.type_name}'
    
    class Meta:
        db_table = 'visitor_db'
        managed = True
        verbose_name = 'بازدید کننده'
        verbose_name_plural = ' بازدید کنندگان'
        
        
# --------------------------------------------------------------------------------------------------------------
class ticketprice(models.Model):
    visitor_group=models.ForeignKey(visitor_group,on_delete=models.CASCADE,verbose_name='نوع بازدید کننده')
    places=models.ForeignKey(places,on_delete=models.CASCADE,verbose_name='نام مکان')
    price=models.IntegerField(default=0,verbose_name='بهای بلیط')
    
    def __str__(self) :
        return f'{self.visitor_group}\t{self.places}\t{self.price}'
    
    class Meta:
        db_table = 'ticket_db'
        managed = True
        verbose_name = 'قیمت'
        verbose_name_plural = 'قیمت ها'
        
        
# --------------------------------------------------------------------------------------------------------------
class Mesaage(models.Model):
    fullname=models.CharField(max_length=50,verbose_name="نام و نام خانوادگی")
    email=models.EmailField(max_length=100,verbose_name=" ایمیل")
    subject=models.CharField(max_length=200,verbose_name=" عنوان پیام")
    message=models.TextField(verbose_name='متن پیام')
    is_seen=models.BooleanField(default=False,verbose_name='وضعیت مشاهده توسط مدیر')
    regester=models.DateTimeField(default=timezone.now,verbose_name='تاریخ ثبت پیام')
    
    def __str__(self) :
        return f'{self.fullname}\t{self.subject}'
    
    class Meta:
        db_table = 'message_db'
        managed = True
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام'
        