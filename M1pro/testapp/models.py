from django.db import models

# Gender categories
GENDER_CHOICES = (
    ('M', 'Men'),
    ('W', 'Women'),
    ('K', 'Kids'),
)

# Subcategories for each gender
CATEGORY_CHOICES = (
    ('SW', 'Sportswear'),
    ('CW', 'Casual Wear'),
    ('FW', 'Formal Wear'),
    ('OW', 'Outerwear'),
    ('NA', 'New Arrivals'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)  # Gender choice (Men, Women, Kids)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)  # Subcategory choice
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='', blank=True)
    prodapp = models.TextField(default='', blank=True)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return f"{self.title} - {self.get_gender_display()} - {self.get_category_display()}"
