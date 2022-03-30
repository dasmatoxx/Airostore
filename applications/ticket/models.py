from datetime import date

from django.contrib.auth import get_user_model
from django.db import models

from applications.airline_companies.models import Flight

User = get_user_model()


class TypeClass(models.Model):
    ECONOMY = 'Economy class'
    BUSINESS = 'Business class'
    FIRST = 'First class'
    CLASS = [
        (ECONOMY, 'Economy class'),
        (BUSINESS, 'Business class'),
        (FIRST, 'First class'),
    ]
    name = models.CharField(max_length=14, choices=CLASS)
    available_seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class TicketBook(models.Model):
    ac = 'accepted'
    re = 'refused'
    pe = 'pending'

    STATUS_CHOICES = (
        (ac, 'Accepted'),
        (re, 'Refused'),
        (pe, 'Pending')
    )

    flight = models.ForeignKey(Flight, models.DO_NOTHING)
    type = models.ForeignKey(TypeClass, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    total_price = models.PositiveIntegerField(default=0)
    last_name = models.CharField(max_length=255, blank=False)
    first_name = models.CharField(max_length=255, blank=False)
    middle_name = models.CharField(max_length=255, blank=False)
    date_of_birth = models.DateField(default=date.today)
    passport_id = models.CharField(max_length=255, blank=False)
    issued_passport = models.CharField(max_length=255, blank=False)
    period_of_validity = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')
    seat = models.PositiveIntegerField()

    def __str__(self):
        return f'Ticket by {self.user}'


