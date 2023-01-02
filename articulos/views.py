from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from .models import Articulo

# Create your views here.
class VistaListaArticulos(ListView):
    model = Articulo
    template_name = 'lista_articulos.html'

class VistaDetalleArticulo(DetailView):
    model = Articulo
    template_name = 'detalle_articulo.html'
    context_object_name = 'articulo'
    login_url = 'login'

class VistaEditarArticulo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    template_name = 'editar_articulos.html'
    fields = ['titulo', 'cuerpo',]
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

class VistaEliminarArticulo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = 'eliminar_articulo.html'
    success_url = reverse_lazy('lista_articulos')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

class VistaCrearArticulo(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = 'nuevo_articulo.html'
    fields = ['titulo', 'cuerpo',]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
