from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)

class Listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', default=1)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default='True')

    def __str__(self):
        return '{}, ${}'.format(self.title, self.price)