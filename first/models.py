from django.db import models

# Create your models here.
class Foods(models.Model):
    cook_year = models.IntegerField()
    cook_name = models.CharField(max_length=50)
    unit_price = models.IntegerField()
    count = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "식자재 인상률"
    def __str__(self):
        return f"{self.cook_year}{self.cook_name}{self.unit_price}{self.count}"