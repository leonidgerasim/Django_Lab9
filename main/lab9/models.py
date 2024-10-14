from django.db import models

# Create your models here.


class Automobile(models.Model):
    mark = models.CharField(max_length=20)
    number = models.CharField(max_length=10)
    year = models.IntegerField()
    consumption = models.IntegerField()


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Driver(models.Model):
    driver = models.ForeignKey('Employee', on_delete=models.CASCADE)
    automobile = models.ForeignKey('Automobile', on_delete=models.CASCADE)


class Waybill(models.Model):
    driver = models.ForeignKey('Employee', on_delete=models.CASCADE)
    automobile = models.ForeignKey('Automobile', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    check_in_time = models.DateTimeField()
    initial_mileage = models.IntegerField()
    final_milage = models.IntegerField()
    milage = models.IntegerField()
    consumption = models.IntegerField()



