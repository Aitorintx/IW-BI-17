from django.db import models

class Promotor(models.Model):
    idPromotor = models.AutoField(primary_key=True)
    namePromotor = models.TextField()
    infoPromotor = models.TextField()

class Festival(models.Model):
    idFestival = models.AutoField(primary_key=True)
    nombreFestival = models.TextField()
    infoFestival = models.TextField()
    fecha = models.TextField()
    idPromotor = models.ForeignKey(Promotor, on_delete=models.CASCADE)

class Interprete(models.Model):
    idInterprete = models.AutoField(primary_key=True)
    nameInterprete = models.TextField()
    infoIntérprete = models.TextField()

class Actuacion(models.Model):
    idActuacion = models.AutoField(primary_key=True)
    idInterprete = models.ForeignKey(Interprete, on_delete=models.CASCADE)
    idFestival = models.ForeignKey(Festival, on_delete=models.CASCADE)

# 
#class Departamento(models.Model):
#    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
#    nombre = models.CharField(max_length=50)
#    telefono = models.IntegerField()
#
#class Habilidad(models.Model):
#    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
#    nombre = models.CharField(max_length=50)
# 
#class Empleado(models.Model):
#    # Campo para la relación one-to-many (un empleado pertenece a un departamento)
#    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
#    # Campo para la relación many-to-many (un empleado tiene varias habilidades)
#    habilidades = models.ManyToManyField(Habilidad)
#    nombre = models.CharField(max_length=40)
#    fecha_nacimiento = models.DateField()
#    # Es posible indicar un valor por defecto mediante 'default'
#    antiguedad = models.IntegerField(default=0)
#    # Para permitir propiedades con valor null, añadiremos las opciones null=True, blank=True.       	