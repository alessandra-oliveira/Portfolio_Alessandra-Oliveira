from django.db import models

class Pessoal(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=20)
    email = models.EmailField()
    git = models.URLField()
    linked = models.URLField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome