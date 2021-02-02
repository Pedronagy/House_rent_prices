#%%
from numpy.core.fromnumeric import mean
import pandas as pd #dataframe
import numpy as np#dataframe
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns

data_original = pd.read_csv('site_data_zap.csv',sep='\t')
print(data_original.shape)
data = data_original.drop_duplicates('description')
data = data.drop(columns=['link'])
data = data.fillna(0)
print(data.shape)
data.insert(3,'total',data['rent'] + data['condominium'] + data['iptu'])
print(data.shape)
df = data.loc[(data['total'] <= 2500) & (data['area'] >= 5) & (data['area'] <= 250) & (data['room'] >= 1) & (data['bathroom'] >= 1) & (data['car_space'] <= 5)]
print(df.shape)
# %%
sns.set_context('paper', font_scale=1.4)
sns_plot = sns.jointplot(x='area', y='total', data=df, kind='scatter',xlim=(0,210),ylim=(250,2550))
sns_plot.savefig("Figures/area_rent_01.jpeg")
#%%
sns.set_context('paper', font_scale=1.4)
sns_plot = sns.jointplot(x='area', y='total', data=df, kind='hist',xlim=(0,210),ylim=(250,2550))
sns_plot.savefig("Figures/area_rent_02.jpeg")
#%%
sns.set_context('paper', font_scale=1.4)
sns_plot = sns.jointplot(x='area', y='total', data=df, kind='kde',xlim=(0,210),ylim=(250,2550),fill=True)
sns_plot.savefig("Figures/area_rent_03.jpeg")
#%%
sns.set_context('paper', font_scale=1.4)
sns_plot = sns.jointplot(x='area', y='total', data=df, kind='reg',xlim=(0,210),ylim=(250,2550))
sns_plot.savefig("Figures/area_rent_04.jpeg")
#%%
sns.set_context('paper', font_scale=1.4)
sns_plot = sns.jointplot(x='area', y='total', data=df, kind='hex',xlim=(0,210),ylim=(250,2550))
sns_plot.savefig("Figures/area_rent_05.jpeg")
#%%
g = sns.PairGrid(df, diag_sharey=False)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot)
g.savefig("Figures/pair_01.jpeg")
#%%
fig, axes = plt.subplots(1,3,sharey=True,figsize=(10,6))

g1 = sns.boxplot(y='area', x='room', data=df, ax=axes[0])
g2 = sns.boxplot(y='area', x='bathroom', data=df, ax=axes[1])
g3 = sns.boxplot(y='area', x='car_space', data=df, ax=axes[2])
g1.grid(axis='y')
g2.grid(axis='y')
g3.grid(axis='y')
# g1.xaxis.set_major_formatter(FormatStrFormatter('%g'))
# g2.set(yticklabels=[])
# g2.xaxis.set_major_formatter(FormatStrFormatter('%g'))
# g2.set(ylabel=None)
# g3.set(yticklabels=[])
# g3.xaxis.set_major_formatter(FormatStrFormatter('%g'))
# g3.set(ylabel=None)

fig.show()
fig.savefig("Figures/general_01.jpeg")
#%%
fig, axes = plt.subplots(1,3,sharey=True,figsize=(10,6))

g1 = sns.boxplot(y='total', x='room', data=df, ax=axes[0])
g2 = sns.boxplot(y='total', x='bathroom', data=df, ax=axes[1])
g3 = sns.boxplot(y='total', x='car_space', data=df, ax=axes[2])
g1.grid(axis='y')
g2.grid(axis='y')
g3.grid(axis='y')
# g2.set(yticklabels=[])
# g2.xaxis.set_major_formatter(FormatStrFormatter('%g'))
g2.set(ylabel=None)
# g3.set(yticklabels=[])
# g3.xaxis.set_major_formatter(FormatStrFormatter('%g'))
g3.set(ylabel=None)

fig.show()
fig.savefig("Figures/general_02.jpeg")
#%%
# geolocation
location = geolocator.geocode("Rua Thomas Alva Edison, Jardim Bela Vista")
print(location.adress)
print((location.latitude, location.longitude))
print(location.raw)
# %%
