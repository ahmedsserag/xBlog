from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=100, help_text="Max lenght is 100.")
    #cover = models.ImageField(default='', upload_to=user_directory_path, blank=True)
    body = models.TextField(max_length=1250, verbose_name="Content")
    TYPE = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    )
    status = models.CharField(choices=TYPE, max_length=9, default='Published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True) # Every time the object is saved, such as last modified.
    created = models.DateTimeField(auto_now_add=True, editable=True) # Automatically set the field to now when the object is first created.

    class Meta:
        ordering = ['-publish'] # Sort posts based on newest date of publish
        indexes = [
            models.Index(fields=['-publish']), # Enhance databases query performance
        ]
    
    # def user_directory_path(instance, filename):
    #     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #     return f"{instance.user.id}/{filename}"
    
    def __str__(self) -> str:
        return str(self.title)
    
    # Canonical URLs for enhanced SEO
    def get_absolute_url(self):
        return reverse("blog:single-post",args=[self.slug])
    