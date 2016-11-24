# Parte 1 - A partir do prompt de comando,instalar os pacotes necessários 
# Se utilizar anaconda, coloque "conda install pandas", 
# "conda install scipy", "conda install scikit-learn", 
# "conda install numpy", "conda install matplotlib".

# Depois, no spyder rodar a programação de importação dos pacotes:
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt

# carrega a base de dados
dados_vulnerab = pd.read_csv('Dados_vulnerabilidade_AtlasBrasil_V6_criancas.csv')

# mantem apenas variaveis quantitativas
dados_vulnerab_ind = dados_vulnerab[['variavel1','variavel2','variavel3','variavel4','variavel5','variavel6']]

# inicializa classificador
kmeans = KMeans(n_clusters = 3,
                max_iter = 450, 
                n_init = 15, 
                init = 'k-means++')

kmeans.fit(dados_vulnerab_ind)

# inspeciona clusters por UF
dados_vulnerab['cluster'] = kmeans.labels_
dados_vulnerab = shuffle(dados_vulnerab)
print(dados_vulnerab[['sigla_UF', 'cluster']])

# testar se o tamanho do cluster está adequado

scatter_plot = plt.scatter(dados_vulnerab['variavel1'], dados_vulnerab['variavel2'], alpha=0.5, 
                          c=dados_vulnerab['cluster'])
plt.show()

scatter_plot = plt.scatter(dados_vulnerab['variavel1'], dados_vulnerab['variavel6'], alpha=0.5, 
                          c=dados_vulnerab['cluster'])
plt.show()

scatter_plot = plt.scatter(dados_vulnerab['variavel5'], dados_vulnerab['variavel6'], alpha=0.5, 
                          c=dados_vulnerab['cluster'])
plt.show()

# Fazer estatistica descritiva das variáveis
# Mostra a média das variáveis em separado
print(dados_vulnerab [['variavel1','variavel2','variavel3','variavel4','variavel5','variavel6']].mean())
print(dados_vulnerab [['variavel1','variavel2','variavel3','variavel4','variavel5','variavel6']].median())
print(dados_vulnerab [['variavel1','variavel2','variavel3','variavel4','variavel5','variavel6']].max())
print(dados_vulnerab [['variavel1','variavel2','variavel3','variavel4','variavel5','variavel6']].min())

# Mostra a média das variáveis por cluster
print(dados_vulnerab[['variavel1','variavel2','variavel3','variavel6']].groupby(dados_vulnerab['cluster']).describe())
print(dados_vulnerab[['variavel4','variavel5']].groupby(dados_vulnerab['cluster']).describe())

# Conta a quantidade de municípios por cluster e UF
table = pd.crosstab(dados_vulnerab.sigla_UF,dados_vulnerab.cluster, rownames=['A'], colnames=['B'])
print (table)

# Relação entre o IDH e cada uma das variáveis de vulnerabilidade

scatter_plot = plt.scatter(dados_vulnerab['variavel5'], dados_vulnerab['variavel1'], alpha=0.5, 
                          c=dados_vulnerab['cluster'])
plt.show()

scatter_plot = plt.scatter(dados_vulnerab['variavel5'], dados_vulnerab['variavel2'], alpha=0.5, 
                          c=dados_vulnerab['cluster'])
plt.show()

scatter_plot = plt.scatter(dados_vulnerab['variavel5'], dados_vulnerab['variavel3'], alpha=0.5, 
                          c=dados_vulnerab['cluster'])
plt.show()

scatter_plot = plt.scatter(dados_vulnerab['variavel5'], dados_vulnerab['variavel4'], alpha=0.5, 
                          c=dados_vulnerab['cluster'])
plt.show()

scatter_plot = plt.scatter(dados_vulnerab['variavel5'], dados_vulnerab['variavel6'], alpha=0.5, 
                          c=dados_vulnerab['cluster'])
plt.show()

# Calcula a média dos IDH por cluster 
table1 = pd.pivot_table(dados_vulnerab, values='variavel5', index=['sigla_UF'],
                       columns=['cluster'], aggfunc=np.mean)
print (table1)


