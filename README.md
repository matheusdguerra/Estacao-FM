# Estação FM

Sistema para listagem das frequências FM cadastradas na Anatel.

https://estacao-fm.herokuapp.com/

Possibilidade de filtragem das estações por estado e município.

Dados coletados do site da Anatel via Scraping.

## Como desenvolver

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a [instância com o .env](env_example).
6. Execute os testes.
7. Execute as migrações e crie superusuário

```console
git clone git@github.com:matheusdguerra/Estacao-FM.git
cd Estacao-FM
python3 -m venv .fm
cource .fm\bin\activate
pip install -r requirements-dev.txt
manage test
manage migrate
manage createsuperuser
```
