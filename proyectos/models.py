from django.db import models

class Entregable(models.Model):
    asunto = models.CharField(max_length=255)
    estado = models.CharField(max_length=50, choices=[
        ('Descartado', 'Descartado'),
        ('Bloqueado', 'Bloqueado'),
        ('En análisis', 'En análisis'),
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('En pruebas', 'En pruebas'),
        ('Concluido', 'Concluido'),
    ])
    proyecto = models.CharField(max_length=255) 
    horas_estimadas = models.IntegerField()
    horas_abarcadas = models.IntegerField()
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)  # Nuevo campo
    fecha_finalizacion = models.DateField(null=True, blank=True)
    descripcion = models.TextField()
    comentarios = models.TextField()
    persona_asignada = models.IntegerField()

def __str__(self):
        return self.asunto