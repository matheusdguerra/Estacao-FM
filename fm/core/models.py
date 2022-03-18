from django.db import models


class Stations(models.Model):
    KIND_UF = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('PB', 'Paraíba'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('MG', 'Minas Gerais'),
        ('PE', 'Pernambuco'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SE', 'Sergipe'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('PA', 'Pará'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins'),
    )

    entidade = models.CharField('Nome da entidade', max_length=100)
    uf = models.CharField('Estado', max_length=2, choices=KIND_UF)
    localidade = models.CharField('Localidade', max_length=50)
    frequencia = models.CharField('Frequência', max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'estação FM'
        verbose_name = 'estação FM'

    def __str__(self):
        return self.entidade
