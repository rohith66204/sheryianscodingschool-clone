from django.db import models

class Course(models.Model):  # Ensure 'Course' has a capital 'C'
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    image = models.ImageField(upload_to='courses/')
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_discount_percentage(self):
        if self.original_price and self.discount_price:
            return round((1 - (self.discount_price / self.original_price)) * 100, 2)
        return 0

    def __str__(self):
        return self.title
