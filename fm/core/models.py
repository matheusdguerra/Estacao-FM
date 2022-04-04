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
    frequencia = models.CharField('Frequência', max_length=50)
    Nome_Entidade = models.CharField('Nome_Entidade', max_length=100, default='')
    CNPJ = models.CharField('CNPJ', max_length=100, default='')
    N_Fistel = models.CharField('N_Fistel', max_length=100, default='')
    Classe = models.CharField('Classe', max_length=100, default='')
    N_Estacao = models.CharField('N_Estacao', max_length=100, default='')
    End_Entidade = models.CharField('End_Entidade', max_length=100, default='')
    Cidade_Entidade = models.CharField('Cidade_Entidade', max_length=100, default='')
    UF_Entidade = models.CharField('UF_Entidade', max_length=100, default='')
    CEP_Entidade = models.CharField('CEP_Entidade', max_length=100, default='')
    End_Corr = models.CharField('End_Corr', max_length=100, default='')
    Cidade_Corr = models.CharField('Cidade_Corr', max_length=100, default='')
    UF_Corr = models.CharField('UF_Corr', max_length=100, default='')
    CEP_Corr = models.CharField('CEP_Corr', max_length=100, default='')
    End_Estacao = models.CharField('End_Estacao', max_length=100, default='')
    CEP_Estacao = models.CharField('CEP_Estacao', max_length=100, default='')
    Latitude = models.CharField('Latitude', max_length=100, default='')
    Longitude = models.CharField('Longitude', max_length=100, default='')
    Prefixo = models.CharField('Prefixo', max_length=100, default='')
    Potencia = models.CharField('Potencia', max_length=100, default='')

    class Meta:
        verbose_name_plural = 'estação FM'
        verbose_name = 'estação FM'

    def __str__(self):
        return self.entidade
