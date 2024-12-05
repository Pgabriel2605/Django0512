# appmodelo/models.py
from django.db import models

from django.db import models

class Comentario(models.Model):
    nome = models.CharField(max_length=100, default='Pedro Gabriel')  # Campo para o nome
    idade = models.IntegerField(default=19)  # Campo para idade
    email = models.EmailField(default='pedro@palma.com')  # Campo para email, agora opcional
    telefone = models.CharField(max_length=15, default='14996014525')  # Campo para telefone (max_length definido)

    def __str__(self):
        return self.nome



    


    def __str__(self):
        return self.titulo
