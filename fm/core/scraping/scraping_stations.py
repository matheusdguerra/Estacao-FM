# (.fm) C:\Users\Matheus.Guerra.CETIL\fm>pip install requests
# requests-2.27.1

# (.fm) C:\Users\Matheus.Guerra.CETIL\fm>pip install bs4
# beautifulsoup4-4.10.0

# pip install psycopg2-binary
# psycopg2-binary-2.9.3

# pip install sqlalchemy
# sqlalchemy-1.4.32


import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
from sqlalchemy import create_engine


data = []
radio = []

# payload com todos os estado e municipios

payload = {
    'acao': 'p',
    'PagSRD': '/SRD/RELATORIOS/RADIODIFUSAO/RELRADIOCOMPLETO.ASP',
    'strAction': '/SRD/Relatorios/Radiodifusao/RelRadioCompleto.asp',
    'vIndMunicipioTodos': 'True',
    'vIndUFTodos': 'True',
    'OP': '5',
    'NumServico': '230',
    'SiglaUF': 'TT',
    'CodMunicipio': 'TT',
    'radioSituacao': '0'
}


# payload RS Porto Alegre
"""
payload = {
    'acao': 'p',
    'PagSRD': '/SRD/RELATORIOS/RADIODIFUSAO/RELRADIOCOMPLETO.ASP',
    'strAction': '/SRD/Relatorios/Radiodifusao/RelRadioCompleto.asp',
    'vIndMunicipioTodos': 'True',
    'vIndUFTodos': 'True',
    'OP': '5',
    'NumServico': '230',
    'SiglaUF': 'RS',
    'CodMunicipio': '4314902',
    'radioSituacao': '0'
}
"""

# Coleta dados no html da Anatel
response = requests.get('https://sistemas.anatel.gov.br/SRD/Relatorios/Radiodifusao/RelRadioCompleto.asp',
                        params=payload)


content = response.content

site = BeautifulSoup(content, 'html.parser')

stations_full = site.find('form', attrs={'method': 'post'})


for table in stations_full.findAll('table', attrs={'class': 'Tabela'}):
    for line in table.findAll('tr'):
        for rows in line.findAll('td', attrs={'class': 'CampoEsquerda'}):

            radio.append(rows.text.strip('\xa0'))


inicio = 2
final = 25  # cada rádio tem 24 informações

for idx, c in enumerate(radio):
    if idx > len(radio)/25:
        break
    else:
        data.append(radio[inicio:final])
        inicio = final
        final += 23


# cria dataframe que será usadao para upar dados no Sqlite
dataframe = pd.DataFrame(data, columns=['nome_entidade', 'nome_fantasia', 'cnpj', 'n_fistel', 'classe', 'n_estacao',
                                        'end_entidade', 'cidade_entidade', 'uf_entidade', 'cep_entidade',
                                        'end_corr',	'cidade_corr', 'uf_corr', 'cep_corr',
                                        'end_estacao', 'cidade_estacao', 'uf_estacao', 'cep_estacao',
                                        'latitude', 'longitude', 'frequencia', 'prefixo', 'potencia']
                         )


# load dados no banco Sqlite (localhost)
# cria conexão
# conn_sqlite = sqlite3.connect('C:\\Users\\Matheus.Guerra.CETIL\\fm\\db.sqlite3')
# c_sqlite = conn_sqlite.cursor()

# load dados (localhost)
# dataframe.to_sql('dados_anatel', conn_sqlite, if_exists='append', index=False)


# load dados no banco Postgres (Heroku)
conn_postgres = create_engine(
    "postgresql://otaytqsjhmziev:4f00b27fea10434aedf2e2d97fee22973c11d04f544908d0d87370347fc1af67@ec2-54-158-232-223.compute-1.amazonaws.com/d7v7732fba90i")
c_postgres = conn_postgres.connect()

# load dados (Heroku)
dataframe.to_sql('dados_anatel', conn_postgres, if_exists='append', index=False)
