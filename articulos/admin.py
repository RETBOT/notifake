# by: RETBOT 
from atexit import register
from django.contrib import admin
from .models import Articulo, Comentario

class ComentariosEnlinea(admin.TabularInline):
    model = Comentario
# by: RETBOT 
class ArticuloAdmin(admin.ModelAdmin):
    inlines = [
        ComentariosEnlinea,
    ]

# Register your models here.
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentario)
# by: RETBOT 
