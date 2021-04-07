from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

class Product(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=20.00)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    @property
    def owner(self):
        print('we are here')
        return self.uploaded_by