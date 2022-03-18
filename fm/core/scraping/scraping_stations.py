# (.fm) C:\Users\Matheus.Guerra.CETIL\fm>pip install requests
# requests-2.27.1

# (.fm) C:\Users\Matheus.Guerra.CETIL\fm>pip install bs4
# beautifulsoup4-4.10.0

import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
radio = []

# payload com todos os estado e municipios
"""
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
"""

# payload RS Porto Alegre

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

response = requests.get('https://sistemas.anatel.gov.br/SRD/Relatorios/Radiodifusao/RelRadioCompleto.asp',
                        params=payload)


content = response.content

site = BeautifulSoup(content, 'html.parser')

stations_full = site.find('form', attrs={'method': 'post'})


for table in stations_full.findAll('table', attrs={'class': 'Tabela'}):
    for line in table.findAll('tr'):
        for rows in line.findAll('td', attrs={'class': 'CampoEsquerda'}):

            radio.append(rows.text)

inicio = 2
final = 25  # cada rádio tem 24 informações

for idx, c in enumerate(radio):
    if idx > len(radio)/25:
        break
    else:
        data.append(radio[inicio:final])
        inicio = final
        final += 23
# print(data)

dataframe = pd.DataFrame(data, colluns=['Nome_Entidade', 'uf', 'localidade', 'frequencia'])

print(dataframe)
"""
for lista in data:
    if lista[1].replace(u'\xa0', u'') == '':
        entidade = lista[0].strip()
    else:
        entidade = lista[1].strip()

    uf = lista[16].strip()

    localidade = lista[15].strip()

    frequencia = lista[20].strip()

    print('Entidade:', entidade)
    print('UF:', uf)
    print('Localidade:', localidade)
    print('Frequencia:', frequencia)
    print('')
"""

"""
'Nome Entidade', 'Nome Fantasia', 'CNPJ',	'Nº Fistel',	'Classe', 'Nº Estação', 'End. Entidade', 'Cidade', 'UF'	 RS	CEP:	 90840440
End. Corr.:	 RUA ORFANATROFIO, 711 - ALTO PETROPOLIS, .	Cidade:	 Porto Alegre	UF:	 RS	CEP:	 90840440
End. Estação:	 RUA ORFANATROFIO
711, .	Cidade:	 Porto Alegre	UF:	 RS	CEP:	 90000000
Latitude:	 30S045200	Longitude:	 51W105900	Freqüência:	 98, 3 MHz	Prefixo:	 ZYD676	Potência:	 10.000 kW
"""
