from django.db import models
from django.urls import reverse
class Category(models.Model):
    Category_name = models.CharField(max_length=50,unique=True)
    slug_field=models.SlugField(max_length=50,unique=True)
    Category_description = models.TextField(max_length=250, blank=True)
    Category_image = models.ImageField(upload_to='images/category', blank=True)
    
    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')
        
    def get_url(self):
        return reverse('product_by_category', args=[self.slug_field])
            
    def __str__(self):
        return self.Category_name
