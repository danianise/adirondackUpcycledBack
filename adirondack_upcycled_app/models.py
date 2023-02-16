from django.db import models
from model_utils import Choices
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=50)
    ID = Choices(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    # id = models.BigAutoField(primary_key=True)
    id = models.IntegerField(choices=ID, default=1, primary_key=True)
    hrefName = models.CharField(max_length=50, default="")

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)

class Listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', default=1)
    title = models.CharField(max_length=100)
    # mainPhoto = models.ImageField(upload_to='images/')
    mainPhoto = CloudinaryField('image')
    # photo1 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo1= CloudinaryField('image', blank=True, null=True)
    # photo2 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo2 = CloudinaryField('image', blank=True, null=True)
    # photo3 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo3 = CloudinaryField('image', blank=True, null=True)
    # photo4 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo4 = CloudinaryField('image', blank=True, null=True)
    # photo5 = models.ImageField(upload_to='images/', null=True, blank=True)
    photo5 = CloudinaryField('image', blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=9999.99)
    description = models.TextField()
    QUANTITY = Choices(1, 2, 3, 4, 5)
    quantity = models.IntegerField(choices=QUANTITY, default=1)
    available = models.BooleanField(default=True)

    def __str__(self):
        return '{}, ${}'.format(self.title, self.price)

class Event(models.Model):
    eventName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    url = models.URLField(max_length=200, blank=True, null=True)
    dateTime = models.DateTimeField()
    description = models.TextField()
    archive = models.BooleanField(default=False)

    def __str__(self):
        return '{}, {}'.format(self.eventName, self.dateTime)