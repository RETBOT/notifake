from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UsuarioPers(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank = True)

