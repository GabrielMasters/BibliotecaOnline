from django.db import models

#Classe Instituição
class Aluno(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_fantasia