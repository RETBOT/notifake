from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('detalle_articulo',args=[str(self.id)])
    
class Comentario(models.Model):
    articulo = models.ForeignKey(
        Articulo, 
        on_delete=models.CASCADE,
        related_name='comentarios',
        )
    comentario = models.CharField(max_length=140)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comentario
    
    def get_absolute_url(self):
        return reverse("lista_publicaciones")
    
