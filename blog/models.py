from django.db import models
from django.urls import reverse
#from django.contrib.auth.models import User
from account.models import User
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from extensions.utils import jalali_converter
from ckeditor.fields import RichTextField
# Managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
# Models

class Category(models.Model):

    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name="زیر دسته")
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id', 'position']


    def __str__(self):
        return self.title
    objects = CategoryManager()

class Article(models.Model):

    STATUS_CHOISES = (
        ('d','پیش نویس'),     #draft
        ('p','منتشر شده'),    #published
        ('i','در حال بررسی'), #investigationn
        ('b','برگشت داده شده'),#back
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="articles", verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name="articles")
    time_to_read = models.IntegerField(verbose_name="مدت زمان مطالعه به دقیقه")
    description = RichTextField(blank=True,null=True,verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="images", verbose_name='تصویر مقاله')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_spical = models.BooleanField(default=False, verbose_name='مقاله ویژه')
    status = models.CharField(max_length=1,choices=STATUS_CHOISES, verbose_name='وضعیت')
    comments = GenericRelation(Comment)
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    def get_absolute_url(self):
        return reverse("account:home")

    # def category_published(self):
    #     return self.category.filter(status=True)
    
    def thumbnail_tag(self):
        return format_html("<img width='70px' height='60px' style='border-radius: 5px' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description="عکس"
    
    def category_to_str(self):
        return ",".join([category.title for category in self.category.active()])
    category_to_str.short_description="دسته بندی"

    objects = ArticleManager()