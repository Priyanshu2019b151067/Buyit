from django.db import models
from django.contrib.auth.models import User
# Category Table
class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

# Product table
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='product_creator',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,default='NewUser')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits= 4,decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
    def __str__(self):
        return self.title

