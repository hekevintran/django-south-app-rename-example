from django.db import models

# Create your models here.
class Something(models.Model):
    value = models.BooleanField(default = False)
    new_value = models.IntegerField(default = 0)

    class Meta:
        db_table = 'old_app_something'
