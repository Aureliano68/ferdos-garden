from distutils.command import upload
from django.db import models
from django.utils import timezone

# Create your models here.
# --------------------------------------------------------------------------------------------------------------------------------
class Author(models.Model):
    name=models.CharField(max_length=30,verbose_name="نام ")
    family=models.CharField(max_length=50,verbose_name="نام خانوادگی")
    education=models.CharField(max_length=50,verbose_name="تحصیلات ")
    job_title=models.CharField(max_length=100,verbose_name="عنوان شغلی ")
    email=models.EmailField(max_length=200,verbose_name='ایمیل')
    slug=models.SlugField(max_length=30)
    mobile=models.IntegerField(verbose_name="موبایل")
    status=models.BooleanField(default=False,verbose_name='وضعیت فعال/غیر فعال')

    
    def __str__(self) :
        return f'{self.name}\t{self.family}\t{self.job_title}\t'
    
    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'
        
        
# -------------------------------------------------------------------------------------------------
class Group(models.Model):
    group_article=models.CharField(max_length=50,verbose_name='عنوان گروه ')
    
    def __str__(self) :
        return f'{self.group_article}\t'
    
    class Meta:
        verbose_name = 'گروه مقاله'
        verbose_name_plural = 'گروه مقالات'
        
        
# -------------------------------------------------------------------------------------------------
class article(models.Model):
    Group=models.ForeignKey(Group,on_delete=models.CASCADE,verbose_name='گروه مقاله')
    Author=models.ManyToManyField(Author,verbose_name='نویسنده')
    name_article=models.CharField(max_length=50,verbose_name='نام مقاله')
    image=models.ImageField(upload_to='image/blog',verbose_name='عکس اصلی')
    abstract=models.CharField(max_length=200,verbose_name='خلاصه متن')
    text_little=models.TextField(max_length=500,verbose_name='متن چکیده مقاله')
    key_words=models.CharField(max_length=100,verbose_name=' کلمات کلیدی')
    pdf_name=models.CharField(max_length=100,verbose_name=' نام فایل ')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ نوشتن مقاله ')
    publish_date=models.DateTimeField(default=timezone.now,verbose_name='  تاریخ انتشار ')
    regester=models.DateTimeField(auto_now=True,verbose_name='  تاریخ بروز رسانی ')
    is_active=models.BooleanField(default=False,verbose_name='فعال/غیر فعال')
    view=models.IntegerField(default=0,verbose_name='تعداد بازدید')
    def __str__(self) :
        return f'{self.name_article}\t{self.abstract}\t'
    
    class Meta:
        managed = True
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        
    
# -------------------------------------------------------------------------------------------------

