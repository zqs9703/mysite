from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail
# Create your models here.

class BlogType(models.Model): # blog类型
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Blog(models.Model, ReadNumExpandMethod): 
    title = models.CharField(max_length=50)     #标题
    blog_type = models.ForeignKey(BlogType,on_delete=models.CASCADE) #blog类型
    content = RichTextUploadingField()    # 内容
    read_details = GenericRelation(ReadDetail)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #作者
    created_time = models.DateTimeField(auto_now_add=True)    #文章的创建时间
    last_updated_time = models.DateTimeField(auto_now=True)  #文章的修改时间

    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']