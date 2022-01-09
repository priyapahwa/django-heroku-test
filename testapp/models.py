from django.db import models

# Create your models here.
class TeamModel(models.Model):
    name = models.CharField(max_length=50, null=False, default=True)

    def __str__(self):
        return self.name
