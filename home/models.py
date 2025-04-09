from django.db import models


class Files(models.Model):
    name = models.CharField(max_length=20)
    url = models.ImageField(upload_to="img")
