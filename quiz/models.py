from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class User(models.Model):
    useremail = models.EmailField()
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=18)

    def __str__(self):
        return self.useremail