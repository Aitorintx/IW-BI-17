from django.db import models

class Promotor(models.Model):
    idPromotor = models.AutoField(primary_key=True)
    namePromotor = models.TextField()
    infoPromotor = models.TextField()
    foto = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')

class Festival(models.Model):
    idFestival = models.AutoField(primary_key=True)
    nombreFestival = models.TextField()
    infoFestival = models.TextField()
    fecha = models.TextField()
    idPromotor = models.ForeignKey(Promotor, on_delete=models.CASCADE, related_name='festivales')

class Interprete(models.Model):
    idInterprete = models.AutoField(primary_key=True)
    nameInterprete = models.TextField()
    infoInterprete = models.TextField()
    festivales=models.ManyToManyField(Festival)



