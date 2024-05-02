from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usario(User): 
    TIPO_USUARIO_CHOICES = [
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    ]
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    rut=models.CharField(max_length=10, unique=True)
    direccion=models.CharField(max_length=100)
    correo_electronico=models.EmailField(max_length=100, unique=True)
    telefono=models.CharField(max_length=12)
    tipo_usuario=models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def __str__(self) -> str:
        return f"{self.nombres} {self.apellidos}"
    

class Inmueble(models.Model):
    TIPO_INMUEBLE_CHOICES = [
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela'),
    ]

    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    imagen =models.ImageField(upload_to='')
    precio=models.DecimalField(max_digits=10, decimal_places=0)
    comuna = models.CharField(max_length=50)
    disponible=models.BooleanField(default=True)
    m2_construidos = models.DecimalField(max_digits=10, decimal_places=2)
    m2_terreno = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_estacionamientos = models.PositiveIntegerField()
    cantidad_habitaciones = models.PositiveIntegerField()
    cantidad_banos = models.PositiveIntegerField()
    tipo_de_inmueble=models.CharField(max_length=12, choices=TIPO_INMUEBLE_CHOICES)
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
class Solicitud_arriendo(models.Model): 
    arrendatario=models.ForeignKey(Usario, on_delete=models.CASCADE)
    Inmueble=models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha_inicio=models.DateField()
    fecha_termino=models.DateField()
    mensaje=models.TextField(blank=True) 

    def __str__(self) -> str:
        return f"{self.arrendatario} {self.Inmueble} {self.fecha_inicio} {self.fecha_termino}"
    
