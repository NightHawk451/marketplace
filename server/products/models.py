from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

def upload_file_path(instance, filename):
    return f"product_photo/{instance.product.pk}/{filename}"


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
        return self.uploaded_by

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=upload_file_path, null=True, blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        old = Images.objects.filter(pk=self.pk).first()
        if old:
            """Delete the old image upon change"""
            if old.image != self.image and old.image:
                old.image.delete(save=False)
        super(Images, self).save(*args, **kwargs)
