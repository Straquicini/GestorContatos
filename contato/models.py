from django.db import models

# Create your models here.

# id (primary key)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text),
# category (foreign key), show (boolean), owner (foreign key)
# picture (image)

class Contato(models.Model):
    first_name = models.CharField(max_length=20)     
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=9)
    email = models.EmailField(max_length=100, blank=True)
    created_date = models.DateTimeField()
    description = models.TextField(max_length=200)
    show = models.BooleanField(default=True)
