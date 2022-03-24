-- SQLite (localhost)
-- Cria tabela dados_anatel
CREATE TABLE IF NOT EXISTS dados_anatel (
    ID INTEGER primary key autoincrement,
    Nome_Entidade   TEXT,
    Nome_Fantasia   TEXT,
    CNPJ            TEXT,
    N_Fistel        TEXT,
    Classe          TEXT,
    N_Estacao       TEXT,
    End_Entidade    TEXT,
    Cidade_Entidade TEXT,
    UF_Entidade     TEXT,
    CEP_Entidade    TEXT,
    End_Corr        TEXT,
    Cidade_Corr     TEXT,
    UF_Corr         TEXT,
    CEP_Corr        TEXT,
    End_Estacao     TEXT,
    Cidade_Estacao  TEXT,
    UF_Estacao      TEXT,
    CEP_Estacao     TEXT,
    Latitude        TEXT,
    Longitude       TEXT,
    Frequencia      TEXT,
    Prefixo         TEXT,
    Potencia        TEXT
);


-- Load etl origem dados_anatel destino model python core_stations
INSERT INTO core_stations
select distinct
max(ID),
CASE trim(da.Nome_fantasia) WHEN '' THEN trim(da.Nome_Entidade)
                               ELSE trim(da.Nome_fantasia)
     END as entidade,
     
trim(da.UF_Estacao) as uf,
trim(da.Cidade_Estacao) as localidade,
trim(da.frequencia) as frequencia

from dados_anatel da
group by da.Nome_fantasia, da.UF_Estacao,da.Cidade_Estacao,da.frequencia
order by 1;



-- PostgreSQL (HEROKU)
-- Cria tabela dados_anatel
CREATE TABLE IF NOT EXISTS dados_anatel (
    ID SERIAL primary key,
    Nome_Entidade   TEXT,
    Nome_Fantasia   TEXT,
    CNPJ            TEXT,
    N_Fistel        TEXT,
    Classe          TEXT,
    N_Estacao       TEXT,
    End_Entidade    TEXT,
    Cidade_Entidade TEXT,
    UF_Entidade     TEXT,
    CEP_Entidade    TEXT,
    End_Corr        TEXT,
    Cidade_Corr     TEXT,
    UF_Corr         TEXT,
    CEP_Corr        TEXT,
    End_Estacao     TEXT,
    Cidade_Estacao  TEXT,
    UF_Estacao      TEXT,
    CEP_Estacao     TEXT,
    Latitude        TEXT,
    Longitude       TEXT,
    Frequencia      TEXT,
    Prefixo         TEXT,
    Potencia        TEXT
);

-- Load etl origem dados_anatel destino model python core_stations
INSERT INTO core_stations
select distinct
max(ID),
CASE trim(da.Nome_fantasia) WHEN '' THEN trim(da.Nome_Entidade)
                               ELSE trim(da.Nome_fantasia)
     END as entidade,
     
trim(da.UF_Estacao) as uf,
trim(da.Cidade_Estacao) as localidade,
trim(da.frequencia) as frequencia

from dados_anatel da
group by da.Nome_fantasia,da.Nome_Entidade, da.UF_Estacao,da.Cidade_Estacao,da.frequencia
order by 1;