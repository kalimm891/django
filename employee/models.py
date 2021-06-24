from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    salary = models.IntegerField()

    class Meta:
        db_table ="empdata"

