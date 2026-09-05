from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    specifications = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=150, blank=True)
    message = models.TextField(blank=True)

    products = models.ManyToManyField(Product, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
