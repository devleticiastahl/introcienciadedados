# -*- coding: utf-8 -*-
"""Scikit-Learn, MatPlotLib e Seaborn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u6CrM_UMkXBTUA6AEXKUFYfPZfJuKssZ

# Introdução às Bibliotecas Scikit-Learn, MatPlotLib e Seaborn

# Scikit-Learn

https://scikit-learn.org/stable/index.html

Scikit-learn é uma biblioteca gratuita de **aprendizado de máquina (machine learning)** que pode ajudar você a construir modelos para analisar dados. <br> 

*   Com ela, é possível fazer **aprendizado supervisionado e não supervisionado**.
*   A biblioteca tem muitas ferramentas úteis, como **ajuste de modelo, pré-processamento de dados e avaliação de modelo.**
* Ela foi construída usando outras bibliotecas populares, como **NumPy, SciPy e Matplotlib.**
* Ela já oferece alguns datasets que podem ser utilizados
para realizar testes e aprender a utilizá-la: <br>
  * Boston House-Prices Dataset
  * Breast Cancer Dataset
  * Diabetes Dataset
  * Iris Dataset

Já conhece o site do Data Viz Project? Esse ambiente nos
ajuda a conhecer um pouco mais sobre que tipo de gráfico usar
para cada situação. https://datavizproject.com/

# Matplotlib e Seaborn

*   As bibliotecas **MatPlotLib e Seaborn**, do Python, fazem parte de um conjunto de bibliotecas open source para **visualização
de dados. Para geração de gráficos.**
*  A biblioteca Seaborn é baseada na MatPlotLib. Há também
outras bibliotecas que também são baseadas na MatPlotLib.
*  A biblioteca MatPlotLib por ser a base para grande parte de
outras bibliotecas, é uma das mais completas, entretanto
muitas das configurações precisam ser feitas manualmente,
com linhas de programação
* A biblioteca Seaborn já se apresenta com um conjunto de
parâmetros que se autoconfiguram, para se adaptar ao seu
conjunto de dados e muitas das informações não precisam
ser explicitadas, elas já estão configuradas. Irá perceber
também que há uma pitada de bom gosto na arte final dos
gráficos da biblioteca Seaborn.

# Bora praticar

## Importar as Bibliotecas
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

"""## Gerar pontos X e Y"""

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 2, 6, 7, 8, 9, 10]

"""## Plotar X e Y"""

plt.scatter(x,y)
plt.show

"""## Gerar um novo gráfico (para valor de Y sendo o quadrado do valor de X)"""

# Gerando um array que vai de -100 a 100, de um em um
x1 = np.arange(-100, 100, 1)
x1

# o y neste caso vai ser os valores de x1 ao quadrado
plt.plot(x1,x1**2)
plt.show

"""## Experimentando ver cortar o eixo X (vamos diminuir um pouco o valor de Y"""

# Como um número elevado ao quadrado nunca dá um valor negativo
# para fazer com que corte o eixo X, temos que diminuir o valor de Y
plt.plot(x1, (x1**2)-2000)
plt.show

"""## Mais uma experiência com dados fabricados"""

dias = np.arange(1,31)
dias

vacinados = np.random.randint(0, 1000, 30)
contagios = np.random.randint(0, 700, 30)
vacinados

contagios

# Plotar Gráfico

#plt.style.use('classic')
#plt.style.use('dark_background')
plt.style.use('default')

plt.figure(figsize=(10,5))
plt.bar(dias, vacinados)
plt.plot(dias, contagios, 'r')
plt.ylabel("Vacinados por Dia")
plt.show

# Criando DataFram com os dados fabricados

dados = pd.DataFrame(dias, columns=['Dias'])

dados['Contagios'] = contagios
dados['Vacinados'] = vacinados
dados

"""## Plotar um gráfico a partir de um DataFrame com o Pandas"""

dados.plot(kind='bar', x='Dias', y='Vacinados')

"""## Plotar um gráfico a partir de um DataFrame com o Seaborn"""

sns.barplot(data=dados, x='Dias', y='Contagios')
# sns.barplot(data=dados, x='Dias', y='Vacinados', color='red')
sns.lineplot(data=dados, x='Dias', y='Vacinados', color='red')