from django.db import models
from django.utils.text import slugify
from datetime import date


class Category(models.Model):
    """
    Categories for organizing medicines (e.g., Painkillers, Antibiotics).
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    """
    Medicine model for storing product details, including metadata for SEO and inventory management.
    """
    name = models.CharField(
        max_length=255, 
        unique=True, 
        verbose_name="Product Name"
    )
    slug = models.SlugField(
        max_length=255, 
        unique=True, 
        blank=True, 
        verbose_name="Slug (for SEO-friendly URL)"
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Price (TK)"
    )
    power = models.PositiveIntegerField(
        default=0, 
        verbose_name="Medicine Power (mg)"
    )
    short_description = models.CharField(
        max_length=500, 
        verbose_name="Short Description"
    )
    description = models.TextField(
        verbose_name="Description"
    )
    category = models.ForeignKey(
        'Category', 
        on_delete=models.CASCADE, 
        related_name="medicines", 
        verbose_name="Category"
    )
    expire_date = models.DateField(
        verbose_name="Expiry Date"
    )
    stock = models.PositiveIntegerField(
        default=0, 
        verbose_name="Stock Quantity"
    )
    thumbnail = models.ImageField(
        upload_to="products/", 
        default="products/default.jpg", 
        verbose_name="Product Thumbnail"
    )
    meta_tags = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        verbose_name="Meta Tags (SEO)"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Created At"
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Last Updated At"
    )
    is_top_selling = models.BooleanField(
        default=False, 
        verbose_name="Is Top Selling Product"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Medicine"
        verbose_name_plural = "Medicines"

    def save(self, *args, **kwargs):
        """
        Automatically generate a slug based on the name if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def is_expired(self):
        """
        Check if the medicine has expired based on the expiry date.
        """
        return self.expire_date < date.today()

    def __str__(self):
        return self.name