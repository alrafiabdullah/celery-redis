from django.db import models


# Create your models here.
class DummyData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Dummy Data'
        verbose_name_plural = 'Dummy Data'
