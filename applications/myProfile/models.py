# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField('Titulo',max_length=100)
    describe = models.TextField('Descripcion')
    image = models.ImageField('Portada_De_Proyecto',upload_to=f'{'image'}', default=None)
    url = models.URLField('Link',blank=True)

    def __str__(self):
        return self.title
