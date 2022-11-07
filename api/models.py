from django.db import models
from django.utils import timezone

class employee(models.Model):
    id = models.IntegerField(primary_key =True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    position = models.CharField(max_length=15)
    date_emp = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.firstname
   