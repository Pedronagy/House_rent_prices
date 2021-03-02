#%%
from numpy.core.fromnumeric import mean
import pandas as pd #dataframe
import numpy as np#dataframe
import matplotlib.pyplot as plt
import seaborn as sns

data_original = pd.read_csv('site_data.csv',sep='\t')
print(data_original.shape)
data = data_original.drop_duplicates()
print(data.shape)
df = data.loc[(data['rent'] <= 2000) & (data['area'] <= 150)]
print(df.shape)
# %%
# Create the heatmap, add annotations and a color map
df_mx = data.corr()
sns.heatmap(df_mx, annot=True, cmap='Blues')
# %%
sns.pairplot(data)
tips_df = sns.load_dataset('tips')
# %%
sns.jointplot(x='area', y='rent', data=df, kind='reg')
#%%
sns.boxplot(y='rent', x='room', data=df, hue='description')
# %%
sns.barplot(x='area', y='description', data=df)

# %%
df['description'].value_counts()
data['description'].value_counts()
# %%
