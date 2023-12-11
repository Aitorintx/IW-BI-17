from django.db import models


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

class Promotor(models.Model):
    idPromotor = models.AutoField(primary_key=True)
    namePromotor = models.TextField()
    infoPromotor = models.TextField()
    foto = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')

class Interprete(models.Model):
    idInterprete = models.AutoField(primary_key=True)
    nameInterprete = models.TextField()
    infoInterprete = models.TextField()

class Festival(models.Model):
    idFestival = models.AutoField(primary_key=True)
    nombreFestival = models.TextField()
    infoFestival = models.TextField()
    fecha = models.TextField()
    promotor = models.ForeignKey(Promotor, on_delete=models.CASCADE, related_name='festivales')
    interpretes=models.ManyToManyField(Interprete)


    



