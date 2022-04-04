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
max(ID) as id,
CASE trim(da.Nome_fantasia) WHEN '' THEN trim(da.Nome_Entidade)
                               ELSE trim(da.Nome_fantasia)
     END as entidade
     
,trim(da.UF_Estacao) as uf
,trim(da.Cidade_Estacao) as localidade
,trim(da.frequencia) as frequencia
,trim(da.CEP_Corr) as CEP_Corr 
,trim(da.CEP_Entidade) as CEP_Entidade  
,trim(da.CEP_Estacao) as CEP_Estacao  
,trim(da.CNPJ) as CNPJ 
,trim(da.Cidade_Corr) as Cidade_Corr   
,trim(da.Cidade_Entidade) as Cidade_Entidade 
,trim(da.Classe) as Classe    
,trim(da.End_Corr) as End_Corr      
,trim(da.End_Entidade) as End_Entidade  
,trim(da.End_Estacao) as End_Estacao
,trim(da.Latitude) as Latitude         
,trim(da.Longitude) as Longitude      
,trim(da.N_Estacao) as N_Estacao       
,trim(da.N_Fistel) as N_Fistel         
,trim(da.Potencia) as Potencia          
,trim(da.Prefixo) as Prefixo     
,trim(da.UF_Corr) as UF_Corr  
,trim(da.UF_Entidade) as UF_Entidade
,trim(da.Nome_Entidade) as Nome_Entidade              
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