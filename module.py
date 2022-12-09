# %% [markdown]
# Dataset:\
# https://www.kaggle.com/datasets/imdevskp/cholera-dataset

# %%
import pandas as pd

# %% [markdown]
# ### 1. Data treatment

# %%
data = pd.read_csv('data.csv')
data.head()

# %%
data.info()

# %%
data['Number of reported cases of cholera'] = pd.to_numeric(
    data['Number of reported cases of cholera'], 
    errors='coerce', 
    downcast='float')

data['Number of reported deaths from cholera'] = pd.to_numeric(
    data['Number of reported deaths from cholera'], 
    errors='coerce', 
    downcast='float')

data['Cholera case fatality rate'] = pd.to_numeric(
    data['Cholera case fatality rate'], 
    errors='coerce', 
    downcast='float')

data.info()

# %%
data.dropna(inplace=True)
data.info()

# %%
data.head()

# %%
data.loc[data['Country']=='Congo', 'WHO Region'] = 'Africa'
data


