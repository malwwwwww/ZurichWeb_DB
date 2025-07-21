from django.db import models

class EQUIPOS(models.Model):
    ID_EQUIPO = models.CharField(max_length=10, primary_key=True)
    ESTADO = models.CharField(max_length=20)
    RAZON_SOCIAL = models.CharField(max_length=100)
    UBICACION = models.CharField(max_length=100, blank=True, null=True)
    TIPO_EQUIPO = models.CharField(max_length=50, blank=True, null=True)
    SITUACION = models.CharField(max_length=50, blank=True, null=True)
    PROVEEDOR = models.CharField(max_length=100, blank=True, null=True)
    MARCA = models.CharField(max_length=50, blank=True, null=True)
    MODELO = models.CharField(max_length=50, blank=True, null=True)
    SERIE = models.CharField(max_length=50, blank=True, null=True)
    LINEA_TEL = models.CharField(max_length=20, blank=True, null=True)
    IMEI = models.CharField(max_length=20, blank=True, null=True)
    COMPANIA = models.CharField(max_length=50, blank=True, null=True)
    PROCESADOR = models.CharField(max_length=50, blank=True, null=True)
    RAM_1 = models.CharField(max_length=20, blank=True, null=True)
    RAM_2 = models.CharField(max_length=20, blank=True, null=True)
    DISCO_1 = models.CharField(max_length=20, blank=True, null=True)
    DISCO_2 = models.CharField(max_length=20, blank=True, null=True)
    SISTEMA_OPERATIVO = models.CharField(max_length=50, blank=True, null=True)
    OBSERVATIONS = models.TextField(blank=True, null=True)
    MAC_WIFI1 = models.CharField(max_length=17, blank=True, null=True)
    MAC_WIFI2 = models.CharField(max_length=17, blank=True, null=True)
    MAC_ETHERNET1 = models.CharField(max_length=17, blank=True, null=True)
    MAC_ETHERNET2 = models.CharField(max_length=17, blank=True, null=True)
    DEPARTAMENTO_ASIGNADO = models.CharField(max_length=50, blank=True, null=True)
    FECHA_ALTA = models.DateTimeField(blank=True, null=True)
    FOTO = models.FileField(upload_to='fotos/', blank=True, null=True)
    DOCUMENTOS = models.FileField(upload_to='documentos/', blank=True, null=True)
    ANTIVIRUS = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'EQUIPOS'

    def __str__(self):
        return self.ID_EQUIPO

class MONITORES(models.Model):
    ID_MONITOR = models.CharField(max_length=10, primary_key=True)
    ESTADO = models.CharField(max_length=20)
    RAZON_SOCIAL = models.CharField(max_length=100)
    MARCA = models.CharField(max_length=50, blank=True, null=True)
    MODELO = models.CharField(max_length=50, blank=True, null=True)
    NUM_SERIE = models.CharField(max_length=50, blank=True, null=True)
    OBSERVATIONS = models.TextField(blank=True, null=True)
    DOCUMENTOS = models.FileField(upload_to='documentos/', blank=True, null=True)

    class Meta:
        db_table = 'MONITORES'

    def __str__(self):
        return self.ID_MONITOR

class NO_BREAKS(models.Model):
    ID_BREAK = models.CharField(max_length=10, primary_key=True)
    ESTADO = models.CharField(max_length=20)
    RAZON_SOCIAL = models.CharField(max_length=100)
    MARCA = models.CharField(max_length=50, blank=True, null=True)
    MODELO = models.CharField(max_length=50, blank=True, null=True)
    NUM_SERIE = models.CharField(max_length=50, blank=True, null=True)
    OBSERVATIONS = models.TextField(blank=True, null=True)
    DOCUMENTOS = models.FileField(upload_to='documentos/', blank=True, null=True)

    class Meta:
        db_table = 'NO_BREAKS'

    def __str__(self):
        return self.ID_BREAK