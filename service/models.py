from django.db import models

# Create your models here.
class Car(models.Model):
    Service_Choices=[('P','Platinum'),('G','Gold')]
    car_model=models.CharField(max_length=100)
    car_owner=models.CharField(max_length=100)
    car_notes=models.CharField(max_length=100)
    car_number=models.CharField(max_length=100)
    description=models.TextField()
    service_type=models.CharField(max_length=1,choices=Service_Choices,blank=True)
    submission_date=models.DateField()
    year_old=models.IntegerField(null=True)
    servicing=models.ManyToManyField('Service',blank=True)

class Service(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
