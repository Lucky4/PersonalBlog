from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=64, unique=True, default='', verbose_name='e-mail')
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=128, unique=True)
    posts = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=128)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-modify_time']
