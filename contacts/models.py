from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 150)
    address = models.CharField(blank=True, max_length = 200)
    contact_details = models.IntegerField(default=0, blank=True)
    department = models.CharField(blank=True, max_length = 100)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

# Create your models here.
