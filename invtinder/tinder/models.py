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


class User(AbstractUser):
    is_investor = models.BooleanField(default=False)
    company_type = models.CharField(max_length=10)
    no_list = models.ManyToManyField(Project, related_name="no_list")
    yes_list = models.ManyToManyField(Project, related_name="yes_list")


class Slides(models.Model):
    image = models.FileField(upload_to="videos/")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Slides"
