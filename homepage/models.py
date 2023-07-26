from django.db import models

# Create your models here.
class BookDownloader(models.Model):
    user_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.user_name