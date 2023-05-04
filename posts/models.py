from django.db import models
from django.core.validators import MinLengthValidator
from accounts.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    created_at = models.DateTimeField( auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def clean(self):
        self.category_name = self.category_name.capitalize()

    def __str__(self):
        return self.category_name

class PostPoem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    poem_content = models.TextField(validators=[MinLengthValidator(100)])
    poem_slug = models.SlugField(max_length=100,unique=True)
    post_overview = models.TextField(max_length=500)
    author_name = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='post_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title
    
class PostStory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    story_title = models.CharField(max_length=50)
    story_content = models.TextField(validators=[MinLengthValidator(800)])
    story_summary = models.TextField(max_length=500)
    story_slug = models.SlugField(max_length=100,unique=True)
    author_name = models.CharField(max_length=50,blank=True)
    story_cover_photo = models.ImageField(upload_to='story_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.story_title