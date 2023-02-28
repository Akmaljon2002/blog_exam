from django.contrib.auth.models import User
from django.db import models

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()
    kasb = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField()
    mavzu = models.CharField(max_length=50)
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return self.sarlavha
