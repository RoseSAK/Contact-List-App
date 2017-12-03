from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 150, blank=False)
    address = models.CharField(max_length = 200, blank=True, null=True)
    contact_details = models.IntegerField(default=0, blank=True, null=True)
    department = models.CharField(max_length = 100, blank=True, null=True)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Person._meta.fields]

# Create your models here.
