# (.fm) C:\Users\Matheus.Guerra.CETIL\fm>pip install requests
# requests-2.27.1

# (.fm) C:\Users\Matheus.Guerra.CETIL\fm>pip install bs4
# beautifulsoup4-4.10.0

import requests
from bs4 import BeautifulSoup

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

response = requests.get('https://sistemas.anatel.gov.br/SRD/Relatorios/Radiodifusao/RelRadioCompleto.asp',
                        params=payload)

content = response.content

site = BeautifulSoup(content, 'html.parser')

stations_full = site.find('form', attrs={'method': 'post'})

stations = stations_full.find('tbody')

print(stations)


# for station in stations:
#    station_name = station.find('td', attrs={'class': 'CampoEsquerda'})
#    print(station_name.text)


"""

payload = {
    'Servico': '230',
    'acao': 'listagem',
    'op': '5',
    'SiglaServico': 'FM',
    'Situacao': '1',
    'NumServico': '230',
    'SiglaUF': 'RS'
}

response = requests.get('https://sistemas.anatel.gov.br/srd/Consultas/ConsultaGeral/TelaListagem.asp',
                        params=payload)

content = response.content

site = BeautifulSoup(content, 'html.parser')

stations = site.findAll('tr', attrs={'id': 'TRplus'})

for station in stations:
    station_name = station.find('td', attrs={'class': 'CampoEsquerda'})
    print(station_name.text)

<td class = "CampoEsquerda" width = "*%" > RADIO MINUANO DE ALEGRETE LTDA < /td >

<td class = "CampoCentro" width = "*%" > RS < /td >

<td class = "CampoEsquerda" width = "*%" > Alegrete < /td >

<a href = "javascript:Redir('230', 'FM    ', 'RS', '4300406', '33806', '', '45347', '97,5 MHz', '3 ', '')" > 248 < /a >

station_name = station.find('td', attrs={'class': 'CampoEsquerda'})
print(station_name.text)

"""
