from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    date_ajou = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_ajou']
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    images = models.ImageField(upload_to="products", blank=True, null=True)
    date_ajou = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_ajou']
    def __str__(self):
        return self.name

