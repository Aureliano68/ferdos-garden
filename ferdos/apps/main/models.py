from tkinter import Widget
from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام ')
    family=models.CharField(max_length=100,verbose_name=' نام خانوادگی ')
    password=models.IntegerField(verbose_name='پسورد')
    is_active=models.BooleanField(default=True, verbose_name='وضعیت')
    
    def __str__(self) -> str:
        return f'{self.name}\t{self.family}'
    
    class Meta:
        managed = True
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        
    
