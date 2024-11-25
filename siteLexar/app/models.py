from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usernam']

    def __str__(self):
        return self.email


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="category_name")

    def __str__(self):
        return self.category_name


class Goods(models.Model):
    product_name = models.CharField(max_length=100, verbose_name="product_name")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="category")
    price = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return self.product_name
