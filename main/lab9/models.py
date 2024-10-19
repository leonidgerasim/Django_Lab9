from django.db import models

# Create your models here.


class Automobile(models.Model):
    mark = models.CharField(max_length=20)
    number = models.CharField(max_length=10)
    year = models.IntegerField()
    consumption = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f'{self.mark} {self.number}'


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Driver(models.Model):
    driver = models.ForeignKey('Employee', on_delete=models.CASCADE)
    automobile = models.ForeignKey('Automobile', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.driver}'


class Waybill(models.Model):
    date = models.DateTimeField(auto_now=True)
    driver = models.ForeignKey('Employee', on_delete=models.CASCADE)
    automobile = models.ForeignKey('Automobile', on_delete=models.CASCADE, default=None)
    departure_time = models.DateTimeField()
    check_in_time = models.DateTimeField()
    initial_mileage = models.IntegerField()
    final_milage = models.IntegerField()
    milage = models.IntegerField(default=None)
    consumption = models.IntegerField(default=None)

    def __str__(self):
        return f'{self.driver} {self.date}'



