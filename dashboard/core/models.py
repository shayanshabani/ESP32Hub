from django.db import models

# Create your models here.


class DataModel(models.Model):
    topic = models.CharField(max_length=256)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} - {self.message[:50]}"
