from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(max_length=50)
    
    def save(self, *args, **kwargs):
        """
        modifies the save function to check if the value for views is less than 
        0 and updates the value to 0 if so.
        self.views - self refers to the instance of the object ("cat" in this case)
        https://docs.djangoproject.com/en/1.10/topics/db/models/
        """
        if self.views < 0:
            self.views = 0
            
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
           
    class Meta:
        verbose_name_plural = 'categories'
    
        def __str__(self):
            return self.name
        
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
  