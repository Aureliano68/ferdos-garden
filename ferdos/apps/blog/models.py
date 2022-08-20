from distutils.command import upload
from django.db import models

# Create your models here.
# --------------------------------------------------------------------------------------------------------------------------------
class Author(models.Model):
    name=models.CharField(max_length=30,verbose_name="نام ")
    family=models.CharField(max_length=50,verbose_name="نام خانوادگی")
    education=models.CharField(max_length=50,verbose_name="تحصیلات ")
    job_title=models.CharField(max_length=100,verbose_name="عنوان شغلی ")
    email=models.EmailField(max_length=200,verbose_name='ایمیل')
    slug=models.SlugField(max_length=30)
    mobile=models.IntegerField(max_length=11,verbose_name="موبایل")
    status=models.BooleanField(default=False,verbose_name='وضعیت فعال/غیر فعال')

    
    def __str__(self) :
        return f'{self.name}\t{self.family}\t{self.job_title}\t'
    
    class Meta:
        db_table = 'author_db'
        managed = True
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'
        
        
# -------------------------------------------------------------------------------------------------
class article_Group(models.Model):
    title_article=models.CharField(max_length=50,verbose_name='عنوان گروه ')
    
    def __str__(self) :
        return f'{self.title_article}\t'
    
    class Meta:
        managed = True
        verbose_name = 'گروه مقاله'
        verbose_name_plural = 'گروه مقالات'
        
        
# -------------------------------------------------------------------------------------------------
class article(models.Model):
    title_article=models.ForeignKey(article_Group,on_delete=models.CASCADE,verbose_name='گروه مقاله')
    Author=models.ManyToManyField(Author,verbose_name='نویسنده')
    name=models.CharField(max_length=50,verbose_name='نام مقاله')
    image=models.ImageField(upload_to='image/blog',verbose_name='عکس اصلی')
    abstract=models.CharField(max_length=200,verbose_name='خلاصه متن')
    article_text=models.TextField(verbose_name='متن مقاله')
    create_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True,verbose_name='فعال/غیر فعال')
    STATUS_FIELD=[
        ('draft','draft'),
        ('publish','publish')
    ]
    status=models.CharField(max_length=50,choices=STATUS_FIELD,verbose_name='وضعیت')
    
    def __str__(self) :
        return f'{self.name}\t'
    
    class Meta:
        managed = True
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        
    
# -------------------------------------------------------------------------------------------------

