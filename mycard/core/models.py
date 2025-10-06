from django.db import models

# Create your models here.

class VisitCard(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)