from django.db import models

# Create your models here.

class mascota(models.Model):
    alias = models.CharField(max_length=20, unique=True)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    fecha_ingreso = models.DateField(auto_now_add=True)
    t_status = [
        ('AD', 'Adoptado'),
        ('IG', 'Ingresado'),
        ('RI', 'Reingresado')
    ]
    status = models.CharField(max_length=2, choices=t_status, default='IG')
    def __str__(self):
        txt = "{0} {1} {2} {3} {4} {5}"
        return txt.format(self.alias, self.especie, self.raza, self.color, self.sexo, self.fecha_ingreso, self.status)



class adoptante(models.Model):
    apellido_pat = models.CharField(max_length=20)
    apellido_mat = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    edad = models.PositiveSmallIntegerField()
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField()

    def nombre_completo(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellido_pat, self.apellido_mat, self.nombre) 

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.nombre_completo(), self.email)

class historial_mascota(models.Model):
    mascota = models.ForeignKey(mascota, null=False, blank=False, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(adoptante, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        txt = "{0} fue adoptado por {1} la fecha {2}"
        fecMat= self.fecha.strftime("%A %d/%m/%Y")
        return txt.format(self.mascota, self.adoptante, fecMat)



class contacto(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    contenido = models.TextField()