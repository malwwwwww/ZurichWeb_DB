from django.db import models
from django.utils import timezone

class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    num_oficial = models.IntegerField(unique=True)
    num_provicional = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=255, null=True, blank=True)
    apellido_materno = models.CharField(max_length=255, null=True, blank=True)
    nombre_completo = models.CharField(max_length=255, null=True, blank=True)
    sexo = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=50)
    fecha_alta = models.DateField(auto_now_add=True)
    usuario_ultima_modificacion = models.CharField(max_length=255, null=True, blank=True)
    fecha_contratacion = models.DateField(null=True, blank=True)
    fecha_baja = models.DateField(null=True, blank=True)
    departamento = models.CharField(max_length=255, null=True, blank=True)
    puesto = models.CharField(max_length=255, null=True, blank=True)
    centro_costo = models.CharField(max_length=255, null=True, blank=True)
    sucursal = models.CharField(max_length=255, null=True, blank=True)
    plan = models.CharField(max_length=255, null=True, blank=True)
    telefono_trabajo = models.CharField(max_length=50, null=True, blank=True)
    telefono_celular = models.CharField(max_length=50, null=True, blank=True)
    telefono_otro = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    horario_comedor = models.CharField(max_length=255, null=True, blank=True)
    turno = models.CharField(max_length=255, null=True, blank=True)
    foto = models.ImageField(upload_to='empleados/fotos/', null=True, blank=True)
    jefe_inmediato = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'EMPLEADOS'

    def __str__(self):
        return self.nombre_completo or ''

    def save(self, *args, **kwargs):
        self.nombre_completo = f"{self.nombre or ''} {self.apellido_paterno or ''} {self.apellido_materno or ''}".strip()
        super().save(*args, **kwargs)