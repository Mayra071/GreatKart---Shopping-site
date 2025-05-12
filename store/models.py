from django.db import models
from django.urls import reverse
from category.models import Category
from django.core.exceptions import ValidationError

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug_field = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/product')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def clean(self):
        if self.category and not Category.objects.filter(id=self.category.id).exists():
            raise ValidationError({'category': 'Selected category does not exist.'})
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        if self.category:
            return reverse('product_detail', args=[self.category.slug_field, self.slug_field])
        return reverse('store')
        
    def __str__(self):
        return self.product_name
    
    