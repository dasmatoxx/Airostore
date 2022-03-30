from django.db import models
from cities_light.models import City


class Point(models.Model):
    place_of_departure = models.ForeignKey(City, null=True, on_delete=models.SET_NULL, related_name='points')

    place_of_arrival = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.place_of_departure} ---> {self.place_of_arrival}'


class Plane(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    number_of_seat = models.PositiveIntegerField(default=20)

    def __str__(self):
        return self.title


class AviaCompany(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    create_date = models.DateField()

    def __str__(self):
        return self.title


class AviaCompanyImage(models.Model):
    avia_company = models.ForeignKey(AviaCompany, on_delete=models.CASCADE,
                                related_name='image')
    image = models.ImageField(upload_to='avia_photo')

    def __str__(self):
        return self.avia_company.title


class Flight(models.Model):
    destination = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='flight')
    avia_company = models.ForeignKey(AviaCompany, on_delete=models.DO_NOTHING)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    plane = models.ForeignKey(Plane, models.DO_NOTHING)
    total_available_seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Рейс №{self.id}'



