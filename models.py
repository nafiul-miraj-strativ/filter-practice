from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active =models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    