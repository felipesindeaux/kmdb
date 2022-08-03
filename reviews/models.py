from django.db import models


class Recomendation(models.TextChoices):
    MUST = ("Must Watch",)
    SHOULD = ("Should Watch",)
    AVOID = ("Avoid Watch",)
    NO = ("No Opnion",)

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50, choices=Recomendation.choices, default=Recomendation.NO)

    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='reviews')
    critic = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='reviews')
