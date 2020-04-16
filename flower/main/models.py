from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name="Pełna nazwa produktu")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    residual = models.IntegerField(null=True)
    color = models.CharField(max_length=128, null=True)
    delivery_time = models.DurationField(null=True)
    poster = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Kwiatka"
        verbose_name_plural = "Kwiaty"