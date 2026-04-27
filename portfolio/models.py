from django.db import models

class Certificado(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

class Projeto(models.Model):
    TIPO_CHOICES = [
        ('Pessoal', 'Pessoal'),
        ('Disciplina', 'Disciplina'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    git = models.URLField()

    def __str__(self):
        return self.nome