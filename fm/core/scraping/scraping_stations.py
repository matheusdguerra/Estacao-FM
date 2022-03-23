# (.fm) C:\Users\Matheus.Guerra.CETIL\fm>pip install requests
# requests-2.27.1

# (.fm) C:\Users\Matheus.Guerra.CETIL\fm>pip install bs4
# beautifulsoup4-4.10.0

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

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


# cria datdaframe que será usadao para upar dados no Sqlite
dataframe = pd.DataFrame(data, columns=['Nome_Entidade', 'Nome_Fantasia', 'CNPJ', 'N_Fistel', 'Classe', 'N_Estacao',
                                        'End_Entidade', 'Cidade_Entidade', 'UF_Entidade', 'CEP_Entidade',
                                        'End_Corr',	'Cidade_Corr', 'UF_Corr', 'CEP_Corr',
                                        'End_Estacao', 'Cidade_Estacao', 'UF_Estacao', 'CEP_Estacao',
                                        'Latitude', 'Longitude', 'Frequencia', 'Prefixo', 'Potencia']
                         )


# load dados no banco Sqlite
# cria conexão
conn = sqlite3.connect('C:\\Users\\Matheus.Guerra.CETIL\\fm\\db.sqlite3')
c = conn.cursor()

# load dados
dataframe.to_sql('dados_anatel', conn, if_exists='append', index=False)
