from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    video = models.FileField(upload_to="videos/")
    description = models.TextField(max_length=500)
    pitch_deck = models.FileField(upload_to="pitch_decks/")


class Slides(models.Model):
    image = models.FileField(upload_to="videos/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Slides"


class User(AbstractUser):
    company_type = models.CharField(max_length=10)
    choice_list = models.ManyToManyField(Project, through="ChoiceList")


class ChoiceList(models.Model):
    choice_type = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
