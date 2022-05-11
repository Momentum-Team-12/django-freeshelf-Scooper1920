from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title       = models.CharField(max_length=100, null=True)
    author      = models.CharField(max_length=100, null=True)
    url         = models.URLField(blank=True,null=True)
    description = models.TextField(null = True, blank = True)
    created_at  = models.DateTimeField(auto_now_add=True)
#in this case below a book can have 1 category one to many relationship, like a library
    category    = models.ForeignKey('Category', related_name='books',null = True, on_delete=models.CASCADE )

    def __str__(self):
        return self.title
    

class  Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique =True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs = {'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

#create the slug path in urls from the slug tutorial in your slack
#here we are overridng the behavior of a model
#foreign keys need an ondelete

class Favorite(models.Model):
    book = models.ForeignKey('Book', related_name='favorites',on_delete=models.CASCADE)
    #foreign key = user.pk
    user = models.ForeignKey('User', related_name= 'favorites', on_delete=models.CASCADE)