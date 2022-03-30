from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from applications.account.models import User
from applications.airline_companies.models import AviaCompany


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             related_name='review')
    avia_company = models.ForeignKey(AviaCompany, on_delete=models.CASCADE,
                                related_name='review')
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10),
                                                        MinValueValidator(1)])




