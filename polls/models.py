from django.db import models

# Create your models here.

class Question(models.Model):
    tipo = models.CharField("tipo", max_length=200)
    nome = models.CharField("nome", max_length=200)
    descricao = models.CharField("descrição", max_length=200)
    telefone = models.CharField("telefone", max_length=200)
    email = models.CharField("e-mail", max_length=200)
    pub_date = models.DateField("data de publicação")


    # subclasse meta que  é usada para definir metadados do modelo. Esses metadados configuram comportamentos adicionais ou especificam características para o modelo, como ordenação padrão, restrições únicas, nomes amigáveis e muito mais.
    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'