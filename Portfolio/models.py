from django.db import models

class Data(models.Model):
    header = models.CharField(max_length=20)
    judul = models.CharField(max_length=200)
    tentang = models.TextField()

    def __str__(self):
        return self.judul