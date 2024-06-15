from django.db import models

class App(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    passworld = models.CharField(max_length=50)


class Statie(models.Model):
    title = models.CharField(max_length=100)
    anons = models.CharField(max_length=255)
    full_text = models.TextField()
    