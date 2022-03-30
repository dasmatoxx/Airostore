from django.contrib.auth import get_user_model
from django.db import models

from applications.airline_companies.models import AviaCompany

User = get_user_model()


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='question')
    avia_company = models.ForeignKey(AviaCompany, on_delete=models.CASCADE,
                                 related_name='question')
    title = models.TextField()
    question = models.TextField()
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answer')
    answer = models.TextField()
    public_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question.title



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='like')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,
                               related_name='like')
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.like
