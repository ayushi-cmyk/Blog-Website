from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    topics = [('pl','Plants'),
              ('al','Animals'),
              ('na','Nature'),
              ('pc','Place')]
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    state = models.CharField(max_length=100)
    topic = models.CharField(max_length=80, choices=topics)
    image = models.ImageField(upload_to='images/')
    heading = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.topic

