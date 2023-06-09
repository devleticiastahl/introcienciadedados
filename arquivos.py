# -*- coding: utf-8 -*-
"""Arquivos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Yl8PmUZwG4TlDcqyC5fk0SS2a9NBazu

# Tipos de arquivos

* Formatos comuns como **CSV, XLS (Excel), XML, Json e os próprios arquivos em formato de texto** são bem comuns para programadores de um modo geral.
* O contexto de DS e BigData apresenta alguns outros formatos que não são tão comuns para quem está iniciando no mundo do DS
* Entre esses formatos, podemos encontrar: 
 * arquivos binários
 * MessagePack
 * Pickle
 * dados do sistema SAS
 * arquivos HDF
 * dados binários Feather
 * arquivos STATA, entre outros

 Muitas vezes não há como escolher o tipo de dado que o projeto precisará consumir.

## Pandas

* A biblioteca Pandas é uma grande aliada e oferece muitas funcionalidades para lidar com arquivos.
* Há funções prontas já no Pandas para realizar o consumo de dados, veja algumas opções que podem ser utilizadas e facilitam muito o processo de carga de dados:
***read_csv** -> lê dados que utilizam vírgula como delimitador, o arquivo pode vir de um arquivo ou de um endereço URL
***read_excel** -> lê dados tabulares de um arquivo Excel XLS ou XLSX
***read_html** -> lê as tabelas que estão em um arquivo html especificado
***read_json** -> lê dados de uma representação em string JSON (Java Script Object Notation)

Há funções para vários outros tipos (veja na documentação do Pandas)

## Fontes de dados

Há uma infinidade de fontes de dados públicas e disponíveis para
serem utilizadas. Há dados verdadeiros e dados fabricados.<br>
Aproveite e use para estudar e criar seus primeiros projetos:<br>
**Kaggle**
https://www.kaggle.com/datasets<br> 
**Dados Governo Brasileiro**
https://dados.gov.br/dataset <br>
**Instituto Johns Hopkins**
https://github.com/govex/COVID-19/tree/master/data_tables/vaccine_data
**UCI Machine Learning**
https://archive.ics.uci.edu/ml/datasets.php<br>
**Datasets no GitHub (muito bom!)**
https://github.com/awesomedata/awesome-public-dataset

## API

Muitas vezes a fonte de dados pode ser uma API.
Na nossa demonstração, vamos usar uma api de teste,
acessando um endereço, ela gera um dado aleatório de uma pessoa!
https://randomuser.me/api
<br>Resultado em Json!
Observaremos isso na
demonstração

## Gravar Dados

Assim como é feita a carga de dados, oriundos do mundo externo, também é necessário gravar dados muitas vezes.<br>
Há **funções para realizar essas gravações**, incluindo as opções de gravação de dados que a própria biblioteca Pandas faz (assim como faz também para ler dados).<br>

Vamos fazer uma demonstração tanto de gravação, quanto
de leitura de dados.

## Demonstração

### Importar as Bibliotecas
"""

import csv
import pandas as pd

"""### Abrir arquivo (vamos olhar o contúedo dele, é uma informação de texto copiada da Wikipedia - https://pt.wikipedia.org/wiki/Machado_de_Assis

Vamos subir esse arquivo para o Colla (lembrando que toda vez que ele parar a execução o arquivo será excluído)
"""

# 'r' = read = vai abrir e ler este arquivo
arquivo = open('machado_de_assis.txt','r')

"""### Ler linhas, fechar arquivo e mostrar conteúdo"""

# Variável conteudo = uma lista com todas as linhas do arquivo
conteudo = arquivo.readlines()
arquivo.close

# Imprimindo o conteúdo da tela
print(conteudo)
print('----')
for linha in conteudo:
  print(linha)

"""### Alterar em todo o texto a palavra "Rio de Janeiro" por "Ribeirão Petro"
"""

x = ''
for linha in conteudo:
  # Se a linha for diferente de vazia, ou seja, tem conteúdo na linha
  if linha != '':
    #Vai colocar toda linha não vazia na variável X
    x += linha

print('Texto da variável x sem Replace')
print('---------')
print(x)
x = x.replace('Rio de Janeiro', 'Ribeirão Petro')
print('Texto da variável x com Replace')
print('---------')
print(x)

"""### Gravar um novo arquivo"""

# 'w' = write = vai abrir e escrever neste arquivo
arquivo_novo = open('macho de assis_2.txt','w')
# write_lines(x) = escreve no arquivo todas as linhas presentes na variável x (que é uma lista)
arquivo_novo.writelines(x)

arquivo_novo.close()

"""## Trabalhando com  arquivos CSV

### Abrindo Arquivo CSV - Cotação das ações da Tesla

https://www.kaggle.com/datasets/rpaguirre/tesla-stock-price?resource=download

(quase 7 anos de arquivo)
"""

# Utilizando o with as, não precisamos fechar o arquivo, depois ele já fecha automaticamente

with open('kaggle_tesla.csv', 'r') as f:
  # Vai separar as linahs pelo delimitador
  leitor =  csv.reader(f, delimiter=',')
  for linha in leitor:
    # Vamos pegar essas 3 colunas
    data = linha[0]
    fechamento = linha[4]
    volume = linha[5]
    print('Data: ', data, '--Fechamento: ', fechamento, '--Volume: ', volume)

"""### Trabalhando com arquivo CSV usando Pandas

Vamos buscar um arquivo diretamento do GitHub
https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_2021.csv
"""

arquivo = 'https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_2021.csv'

dados = pd.read_csv(arquivo)
dados

"""### Vamos plotar uma informação"""

# winner_hand - é uma coluna do csv que mostra qual mão o jogador joga mais
# value_counts() - conta os valores
# sortvalues() - deixa os resultados da contagem em ordem crescente
# plot(kind = 'barh') - criando um gráfico de barras na horizontal

dados.winner_hand.value_counts().sort_values().plot(kind = 'barh')

"""### Abrir o arquivo Tesla usando o Pandas, determinando nome das colunas e puxando apenas 4 linhas"""

arquivo = 'kaggle_tesla.csv'
dados = pd.read_csv(arquivo, skiprows=1, names = ['data', 'abertura', 'max', 'min','fechamento', 'coluna'], nrows=4)
dados

"""### Trabalhar com arquivos Json, buscando dados da API (https://randomuser.me/api) que gera como resultados arquivos JSON. Essa é uma API bem legal de teste (gera dados de um usuário aleatório)"""

import json
import requests

resposta = requests.get('https://randomuser.me/api')
dados = json.loads(resposta.text)
dados

print(dados['results'][0]['name']['first'])