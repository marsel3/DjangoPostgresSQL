from django.db import models

# Create your models here.
class Sportsmen(models.Model):
    sportsmen_id = models.AutoField(primary_key=True)
    sportsmen_fio = models.CharField(max_length=255, verbose_name='ФИО')
    


    def __str__(self):
        return self