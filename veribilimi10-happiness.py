# -*- coding: utf-8 -*-
"""
Created on Sun May 21 17:38:52 2023

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

happy1 = pd.read_csv("2015.csv")
happy2 = pd.read_csv("2016.csv")
happy3 = pd.read_csv("2017.csv")
happy4 = pd.read_csv("2018.csv")
happy5 = pd.read_csv("2019.csv")

#Hangi ülkeler veya bölgeler genel mutlulukta ve mutluluğa katkıda bulunan altı faktörün her birinde
# en yüksek sırada yer alıyor?


sort_eco = happy1.sort_values(by = ['Economy (GDP per Capita)'], ascending = False)
sort_eco = sort_eco.head(10)
sort_fa = happy1.sort_values(by = ['Family'], ascending = False)
sort_fa = sort_fa.head(10)
sort_he = happy1.sort_values(by = ['Health (Life Expectancy)'], ascending = False)
sort_he = sort_he.head(10)
sort_free = happy1.sort_values(by = ['Freedom'], ascending = False)
sort_free = sort_free.head(10)
sort_tru = happy1.sort_values(by = ['Trust (Government Corruption)'], ascending = False)
sort_tru = sort_tru.head(10)
sort_genero = happy1.sort_values(by = ['Generosity'], ascending = False)
sort_genero = sort_genero.head(10)
sort_dyst = happy1.sort_values(by= ['Dystopia Residual'],ascending = False)
sort_dyst = sort_dyst.head(10)
sort_hap_sco= happy1.sort_values("Happiness Score",ascending= False)
sort_hap_sco = sort_hap_sco.head(10)

ax=sns.barplot(x="Country", y="Economy (GDP per Capita)", data=sort_eco)
ax.tick_params(axis = 'x', rotation = 45)
#plt.show()
ax=sns.barplot(x="Country",y="Family", data=sort_fa)
ax.tick_params(axis = 'x', rotation = 45)
#plt.show()
ax=sns.barplot(x="Country",y="Health (Life Expectancy)", data=sort_he)
ax.tick_params(axis = 'x', rotation = 45)
#plt.show()
ax=sns.barplot(x="Country",y="Freedom", data=sort_free)
ax.tick_params(axis = 'x', rotation = 45)
#plt.show()
ax=sns.barplot(x="Country",y="Trust (Government Corruption)", data = sort_tru)
ax.tick_params(axis = 'x', rotation = 45)
#plt.show()
ax=sns.barplot(x="Country",y="Generosity", data=sort_genero)
ax.tick_params(axis = 'x', rotation = 45)
#plt.show()
ax = sns.barplot(x="Country",y="Dystopia Residual", data= sort_dyst)
ax.tick_params(axis='x',rotation= 45)
#plt.show()
sns.barplot(x= "Country", y="Happiness Score",data= sort_hap_sco)
plt.xticks(rotation= 45)
#plt.show()


#2015-2016 ile 2016-2017 raporları arasında ülke sıralamaları veya puanları nasıl değişti?

head2 = happy2.head(10)
sort2 = head2.sort_values("Happiness Score",ascending= False)
head3 = happy3.head(10)
sort3 = head3.sort_values("Happiness.Score",ascending= False)
head4 = happy4.head(10)
sort4 = head4.sort_values("Score", ascending= False)
head5 = happy5.head(10)
sort5 = head5.sort_values("Score",ascending= False)

sns.barplot(x="Country",y="Happiness Score", data= sort2)
plt.xticks(rotation = 45)
plt.title("2016 yılı en mutlu ülkeler")
#plt.show()

sns.barplot(x="Country",y="Happiness.Score", data= sort3)
plt.xticks(rotation = 45)
plt.title("2017 yılı en mutlu ülkeler")
#plt.show()

sns.barplot(x="Country or region",y="Score", data= sort4)
plt.xticks(rotation = 45)
plt.title("2018 yılı en mutlu ülkeler")
#plt.show()

sns.barplot(x="Country or region",y="Score", data= sort5)
plt.xticks(rotation = 45)
plt.title("2019 yılı en mutlu ülkeler")
#plt.show()


#Herhangi bir ülke mutlulukta önemli bir artış veya azalma yaşadı mı?

country = happy1.iloc[:,:1].values
country = pd.DataFrame(data = country, columns=["Country"])
hap_sco_2015 = happy1.iloc[:,3:4].values
hap_sco_2015 = pd.DataFrame(data = hap_sco_2015, columns=["Happiness Score 2015"])
hap_sco_2016 = happy2.iloc[:,3:4].values
hap_sco_2016 = pd.DataFrame(data = hap_sco_2016, columns=["Happiness Score 2016"])
hap_sco_2017 = happy3.iloc[:,2:3].values
hap_sco_2017 = pd.DataFrame(data = hap_sco_2017, columns=["Happiness Score 2017"])
hap_sco_2018 = happy4.iloc[:,2:3].values
hap_sco_2018 = pd.DataFrame(data = hap_sco_2018, columns=["Happiness Score 2018"])
hap_sco_2019 = happy5.iloc[:,2:3].values
hap_sco_2019 = pd.DataFrame(data = hap_sco_2019, columns=["Happiness Score 2019"])

a= pd.concat([country,hap_sco_2015,hap_sco_2016],axis=1)
b= pd.concat([hap_sco_2017,hap_sco_2018,hap_sco_2019],axis=1)
genelveri = pd.concat([a,b],axis=1)



z=input('ulke ismini gir')
z=z.capitalize()
first_value = genelveri[genelveri.Country==z].values[0][1:6]
yıllar=genelveri.columns[1:6]
sns.barplot( y=yıllar,x =first_value)
plt.show()



