#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine, Table, MetaData
import psycopg2
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import random

# In[2]:


engine = create_engine('postgresql://postgres:qwerty@26.132.86.192:5436/postgres')
atms_df = pd.read_sql_query('SELECT * FROM atms', con=engine)
oh_df = pd.read_sql_query('SELECT * FROM offices_hours', con=engine)
oh_df.drop('id', inplace=True, axis=1)

oh_df.replace("Нет обслуживания ЮЛ", None, inplace=True)
oh_df.dropna(inplace=True)
oh_df.drop('saturday', axis=1, inplace=True)
oh_df.drop('sunday', axis=1, inplace=True)

# In[ ]:


# In[7]:


oh_df

# In[8]:


office_ids = oh_df.loc[oh_df['monday'] != '09:00-18:00', 'office_id'].tolist()
eoffice_ids = oh_df.loc[oh_df['thursday'] != '10:00-19:00', 'office_id'].tolist()
foffice_ids = oh_df.loc[oh_df['friday'] != '10:00-18:00', 'office_id'].tolist()

# In[9]:


ohp_df = oh_df.copy()
ohp_df = ohp_df['office_id']

# In[10]:


columns = ['w1m9-m10', 'w1m10-m11', 'w1m11-m12', 'w1m12-m13', 'w1m13-m14', 'w1m14-m15', 'w1m15-m16', 'w1m16-m17',
           'w1m17-m18', 'w1m18-m19',
           'w1tu9-tu10', 'w1tu10-tu11', 'w1tu11-tu12', 'w1tu12-tu13', 'w1tu13-tu14', 'w1tu14-tu15', 'w1tu15-tu16',
           'w1tu16-tu17', 'w1tu17-tu18', 'w1tu18-tu19',
           'w1w9-w10', 'w1w10-w11', 'w1w11-w12', 'w1w12-w13', 'w1w13-w14', 'w1w14-w15', 'w1mw5-w16', 'w1w16-w17',
           'w1w17-w18', 'w1w18-w19',
           'w1th9-th10', 'w1th10-th11', 'w1th11-th12', 'w1th12-th13', 'w1th13-th14', 'w1th14-th15', 'w1th15-tu16',
           'w1th16-th17', 'w1th17-th18', 'w1th18-th19',
           'w1f9-f10', 'w1f10-f11', 'w1f11-f12', 'w1f12-f13', 'w1f13-f14', 'w1f14-f15', 'w1f15-f16', 'w1f16-f17',
           'w1f17-f18', 'w1f18-f19',
           'w2m9-m10', 'w2m10-m11', 'w2m11-m12', 'w2m12-m13', 'w2m13-m14', 'w2m14-m15', 'w2m15-m16', 'w2m16-m17',
           'w2m17-m18', 'w2m18-m19',
           'w2tu9-tu10', 'w2tu10-tu11', 'w2tu11-tu12', 'w2tu12-tu13', 'w2tu13-tu14', 'w2tu14-tu15', 'w2tu15-tu16',
           'w2tu16-tu17', 'w2tu17-tu18', 'w2tu18-tu19',
           'w2w9-w10', 'w2w10-w11', 'w2w11-w12', 'w2w12-w13', 'w2w13-w14', 'w2w14-w15', 'w2mw5-w16', 'w2w16-w17',
           'w2w17-w18', 'w2w18-w19',
           'w2th9-th10', 'w2th10-th11', 'w2th11-th12', 'w2th12-th13', 'w2th13-th14', 'w2th14-th15', 'w2th15-tu16',
           'w2th16-th17', 'w2th17-th18', 'w2th18-th19',
           'w2f9-f10', 'w2f10-f11', 'w2f11-f12', 'w2f12-f13', 'w2f13-f14', 'w2f14-f15', 'w2f15-f16', 'w2f16-f17',
           'w2f17-f18', 'w2f18-f19',
           'w3m9-m10', 'w3m10-m11', 'w3m11-m12', 'w3m12-m13', 'w3m13-m14', 'w3m14-m15', 'w3m15-m16', 'w3m16-m17',
           'w3m17-m18', 'w3m18-m19', 'w3tu9-tu10', 'w3tu10-tu11',
           'w3tu11-tu12', 'w3tu12-tu13', 'w3tu13-tu14', 'w3tu14-tu15', 'w3tu15-tu16', 'w3tu16-tu17', 'w3tu17-tu18',
           'w3tu18-tu19', 'w3w9-w10', 'w3w10-w11', 'w3w11-w12',
           'w3w12-w13', 'w3w13-w14', 'w3w14-w15', 'w3w15-w16', 'w3w16-w17', 'w3w17-w18', 'w3w18-w19', 'w3th9-th10',
           'w3th10-th11', 'w3th11-th12', 'w3th12-th13', 'w3th13-th14',
           'w3th14-th15', 'w3th15-tu16', 'w3th16-th17', 'w3th17-th18', 'w3th18-th19', 'w3f9-f10', 'w3f10-f11',
           'w3f11-f12', 'w3f12-f13', 'w3f13-f14', 'w3f14-f15', 'w3f15-f16',
           'w3f16-f17', 'w3f17-f18', 'w3f18-f19', 'w4m9-m10', 'w4m10-m11', 'w4m11-m12', 'w4m12-m13', 'w4m13-m14',
           'w4m14-m15', 'w4m15-m16', 'w4m16-m17', 'w4m17-m18', 'w4m18-m19',
           'w4tu9-tu10', 'w4tu10-tu11', 'w4tu11-tu12', 'w4tu12-tu13', 'w4tu13-tu14', 'w4tu14-tu15', 'w4tu15-tu16',
           'w4tu16-tu17', 'w4tu17-tu18', 'w4tu18-tu19', 'w4w9-w10',
           'w4w10-w11', 'w4w11-w12', 'w4w12-w13', 'w4w13-w14', 'w4w14-w15', 'w4w15-w16', 'w4w16-w17', 'w4w17-w18',
           'w4w18-w19', 'w4th9-th10', 'w4th10-th11', 'w4th11-th12',
           'w4th12-th13', 'w4th13-th14', 'w4th14-th15', 'w4th15-tu16', 'w4th16-th17', 'w4th17-th18', 'w4th18-th19',
           'w4f9-f10', 'w4f10-f11', 'w4f11-f12', 'w4f12-f13', 'w4f13-f14',
           'w4f14-f15', 'w4f15-f16', 'w4f16-f17', 'w4f17-f18', 'w4f18-f19',
           'w5m9-m10', 'w5m10-m11', 'w5m11-m12', 'w5m12-m13', 'w5m13-m14', 'w5m14-m15', 'w5m15-m16', 'w5m16-m17',
           'w5m17-m18', 'w5m18-m19', 'w5tu9-tu10', 'w5tu10-tu11',
           'w5tu11-tu12', 'w5tu12-tu13', 'w5tu13-tu14', 'w5tu14-tu15', 'w5tu15-tu16', 'w5tu16-tu17', 'w5tu17-tu18',
           'w5tu18-tu19', 'w5w9-w10', 'w5w10-w11', 'w5w11-w12',
           'w5w12-w13', 'w5w13-w14', 'w5w14-w15', 'w5w15-w16', 'w5w16-w17', 'w5w17-w18', 'w5w18-w19', 'w5th9-th10',
           'w5th10-th11', 'w5th11-th12', 'w5th12-th13', 'w5th13-th14',
           'w5th14-th15', 'w5th15-th16', 'w5th16-th17', 'w5th17-th18', 'w5th18-th19', 'w5f9-f10', 'w5f10-f11',
           'w5f11-f12', 'w5f12-f13', 'w5f13-f14', 'w5f14-f15', 'w5f15-f16',
           'w5f16-f17', 'w5f17-f18', 'w5f18-f19'

           ]

# In[11]:


morn_columns = [column for column in columns if (('9-' in column) or ('10-' in column) or ('11-' in column))]
de_columns = [column for column in columns if column not in morn_columns]

# In[12]:


new_df = pd.concat([ohp_df, pd.DataFrame(columns=columns)], axis=1)
new_df[columns] = 0
ohp_df = new_df

# In[ ]:


# In[13]:


for column in morn_columns:
    ohp_df.loc[:, column] = np.random.randint(5, 11, size=len(ohp_df))
for column in de_columns:
    ohp_df.loc[:, column] = np.random.randint(8, 20, size=len(ohp_df))

# In[14]:


oh_df

# In[15]:


sas = ['w1m9-m10', 'w2m9-m10', 'w3m9-m10', 'w4m9-m10', 'w1tu9-tu10', 'w2tu9-tu10', 'w3tu9-tu10', 'w4tu9-tu10',
       'w1w9-w10',
       'w2w9-w10', 'w3w9-w10', 'w4w9-w10', 'w1th9-th10', 'w2th9-th10', 'w3th9-th10', 'w4th9-th10']
sas1 = ['w1m18-m19', 'w2m18-m19', 'w3m18-m19', 'w4m18-m19', 'w1tu18-tu19', 'w2tu18-tu19', 'w3tu18-tu19', 'w4tu18-tu19',
        'w1w18-w19',
        'w2w18-w19', 'w3w18-w19', 'w4w18-w19', 'w1th18-th19', 'w2th18-th19', 'w3th18-th19', 'w4th18-th19']

# In[16]:


for id in office_ids:
    ohp_df.loc[oh_df['office_id'] == id, sas] = 0
for id in eoffice_ids:
    ohp_df.loc[oh_df['office_id'] == id, sas1] = 0
for id in foffice_ids:
    ohp_df.loc[oh_df['office_id'] == id, 'w1f17-f18'] = 0
    ohp_df.loc[oh_df['office_id'] == id, 'w2f17-f18'] = 0
    ohp_df.loc[oh_df['office_id'] == id, 'w3f17-f18'] = 0
    ohp_df.loc[oh_df['office_id'] == id, 'w4f17-f18'] = 0

# In[ ]:


# In[17]:


ohp_df

# предсказание для 9-10 утра на 5ой неделе

# In[18]:


features = ['w1m9-m10', 'w2m9-m10', 'w3m9-m10']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4m9-m10'])
ohp_df['w5m9-m10'] = model.predict(ohp_df[features]).round(0)

# In[19]:


features = ['w1tu9-tu10', 'w2tu9-tu10', 'w3tu9-tu10']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4tu9-tu10'])
ohp_df['w5tu9-tu10'] = model.predict(ohp_df[features]).round(0)

# In[20]:


features = ['w1w9-w10', 'w2w9-w10', 'w3w9-w10']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4w9-w10'])
ohp_df['w5w9-w10'] = model.predict(ohp_df[features]).round(0)

# In[21]:


features = ['w1th9-th10', 'w2th9-th10', 'w3th9-th10']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4th9-th10'])
ohp_df['w5th9-th10'] = model.predict(ohp_df[features]).round(0)

# In[22]:


features = ['w1f9-f10', 'w2f9-f10', 'w3f9-f10']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4f9-f10'])
ohp_df['w5f9-f10'] = model.predict(ohp_df[features]).round(0)

# предсказание 10-11 утра на пятой неделе

# In[23]:


features = ['w1m10-m11', 'w2m10-m11', 'w3m10-m11']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4m10-m11'])
ohp_df['w5m10-m11'] = model.predict(ohp_df[features]).round(0)
features = ['w1tu10-tu11', 'w2tu10-tu11', 'w3tu10-tu11']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4tu10-tu11'])
ohp_df['w5tu10-tu11'] = model.predict(ohp_df[features]).round(0)
features = ['w1w10-w11', 'w2w10-w11', 'w3w10-w11']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4w10-w11'])
ohp_df['w5w10-w11'] = model.predict(ohp_df[features]).round(0)
features = ['w1th10-th11', 'w2th10-th11', 'w3th10-th11']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4th10-th11'])
ohp_df['w5th10-th11'] = model.predict(ohp_df[features]).round(0)
features = ['w1f10-f11', 'w2f10-f11', 'w3f10-f11']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4f10-f11'])
ohp_df['w5f10-f11'] = model.predict(ohp_df[features]).round(0)

# предсказание 11-12 дня на пятой неделе

# In[24]:


features = ['w1m11-m12', 'w2m11-m12', 'w3m11-m12']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4m11-m12'])
ohp_df['w5m11-m12'] = model.predict(ohp_df[features]).round(0)
features = ['w1tu11-tu12', 'w2tu11-tu12', 'w3tu11-tu12']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4tu11-tu12'])
ohp_df['w5tu11-tu12'] = model.predict(ohp_df[features]).round(0)
features = ['w1w11-w12', 'w2w11-w12', 'w3w11-w12']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4w11-w12'])
ohp_df['w5w11-w12'] = model.predict(ohp_df[features]).round(0)
features = ['w1th11-th12', 'w2th11-th12', 'w3th11-th12']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4th11-th12'])
ohp_df['w5th11-th12'] = model.predict(ohp_df[features]).round(0)
features = ['w1f11-f12', 'w2f11-f12', 'w3f11-f12']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4f11-f12'])
ohp_df['w5f11-f12'] = model.predict(ohp_df[features]).round(0)

# предсказание 12-13 дня на пятой неделе

# In[25]:


features = ['w1m12-m13', 'w2m12-m13', 'w3m12-m13']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4m12-m13'])
ohp_df['w5m12-m13'] = model.predict(ohp_df[features]).round(0)
features = ['w1tu12-tu13', 'w2tu12-tu13', 'w3tu12-tu13']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4tu12-tu13'])
ohp_df['w5tu12-tu13'] = model.predict(ohp_df[features]).round(0)
features = ['w1w12-w13', 'w2w12-w13', 'w3w12-w13']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4w12-w13'])
ohp_df['w5w12-w13'] = model.predict(ohp_df[features]).round(0)
features = ['w1th12-th13', 'w2th12-th13', 'w3th12-th13']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4th12-th13'])
ohp_df['w5th12-th13'] = model.predict(ohp_df[features]).round(0)
features = ['w1f12-f13', 'w2f12-f13', 'w3f12-f13']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4f12-f13'])
ohp_df['w5f12-f13'] = model.predict(ohp_df[features]).round(0)

# предсказание 13-14 на 5ой неделе

# In[26]:


features = ['w1m13-m14', 'w2m13-m14', 'w3m13-m14']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4m13-m14'])
ohp_df['w5m13-m14'] = model.predict(ohp_df[features]).round(0)
features = ['w1tu13-tu14', 'w2tu13-tu14', 'w3tu13-tu14']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4tu13-tu14'])
ohp_df['w5tu13-tu14'] = model.predict(ohp_df[features]).round(0)
features = ['w1w13-w14', 'w2w13-w14', 'w3w13-w14']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4w13-w14'])
ohp_df['w5w13-w14'] = model.predict(ohp_df[features]).round(0)
features = ['w1th13-th14', 'w2th13-th14', 'w3th13-th14']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4th13-th14'])
ohp_df['w5th13-th14'] = model.predict(ohp_df[features]).round(0)
features = ['w1f13-f14', 'w2f13-f14', 'w3f13-f14']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4f13-f14'])
ohp_df['w5f13-f14'] = model.predict(ohp_df[features]).round(0)

# предсказание 14-15 на 5ой неделе

# In[27]:


features = ['w1m14-m15', 'w2m14-m15', 'w3m14-m15']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4m14-m15'])
ohp_df['w5m14-m15'] = model.predict(ohp_df[features]).round(0)
features = ['w1tu14-tu15', 'w2tu14-tu15', 'w3tu14-tu15']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4tu14-tu15'])
ohp_df['w5tu14-tu15'] = model.predict(ohp_df[features]).round(0)
features = ['w1w14-w15', 'w2w14-w15', 'w3w14-w15']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4w14-w15'])
ohp_df['w5w14-w15'] = model.predict(ohp_df[features]).round(0)
features = ['w1th14-th15', 'w2th14-th15', 'w3th14-th15']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4th14-th15'])
ohp_df['w5th14-th15'] = model.predict(ohp_df[features]).round(0)
features = ['w1f14-f15', 'w2f14-f15', 'w3f14-f15']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4f14-f15'])
ohp_df['w5f14-f15'] = model.predict(ohp_df[features]).round(0)

# предсказание 15-16 на 5ой неделе

# In[28]:


features = ['w1m14-m15', 'w2m14-m15', 'w3m14-m15']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4m14-m15'])
ohp_df['w5m15-m16'] = model.predict(ohp_df[features]).round(0)
features = ['w1tu14-tu15', 'w2tu14-tu15', 'w3tu14-tu15']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4tu14-tu15'])
ohp_df['w5tu15-tu16'] = model.predict(ohp_df[features]).round(0)
features = ['w1w14-w15', 'w2w14-w15', 'w3w14-w15']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4w14-w15'])
ohp_df['w5w15-w16'] = model.predict(ohp_df[features]).round(0)
features = ['w1th14-th15', 'w2th14-th15', 'w3th14-th15']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4th14-th15'])
ohp_df['w5th15-th16'] = model.predict(ohp_df[features]).round(0)
features = ['w1f14-f15', 'w2f14-f15', 'w3f14-f15']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4f14-f15'])
ohp_df['w5f15-f16'] = model.predict(ohp_df[features]).round(0)

# предсказание 16-17 на 5ой неделе

# In[29]:


features = ['w1m16-m17', 'w2m16-m17', 'w3m16-m17']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4m16-m17'])
ohp_df['w5m16-m17'] = model.predict(ohp_df[features]).round(0)
features = ['w1tu16-tu17', 'w2tu16-tu17', 'w3tu16-tu17']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4tu14-tu15'])
ohp_df['w5tu16-tu17'] = model.predict(ohp_df[features]).round(0)
features = ['w1w16-w17', 'w2w16-w17', 'w3w16-w17']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4w16-w17'])
ohp_df['w5w16-w17'] = model.predict(ohp_df[features]).round(0)
features = ['w1th16-th17', 'w2th16-th17', 'w3th16-th17']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4th16-th17'])
ohp_df['w5th16-th17'] = model.predict(ohp_df[features]).round(0)
features = ['w1f16-f17', 'w2f16-f17', 'w3f16-f17']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4f16-f17'])
ohp_df['w5f16-f17'] = model.predict(ohp_df[features]).round(0)

# предсказание 17-18 на 5ой неделе

# In[30]:


features = ['w1m17-m18', 'w2m17-m18', 'w3m17-m18']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4m16-m17'])
ohp_df['w5m17-m18'] = model.predict(ohp_df[features]).round(0)
features = ['w1tu17-tu18', 'w2tu17-tu18', 'w3tu17-tu18']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4tu17-tu18'])
ohp_df['w5tu17-tu18'] = model.predict(ohp_df[features]).round(0)
features = ['w1w17-w18', 'w2w17-w18', 'w3w17-w18']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4w17-w18'])
ohp_df['w5w17-w18'] = model.predict(ohp_df[features]).round(0)
features = ['w1th17-th18', 'w2th17-th18', 'w3th17-th18']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4th17-th18'])
ohp_df['w5th17-th18'] = model.predict(ohp_df[features]).round(0)
features = ['w1f17-f18', 'w2f17-f18', 'w3f17-f18']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4f17-f18'])
ohp_df['w5f17-f18'] = model.predict(ohp_df[features]).round(0)

# предсказание 18-19 на 5ой неделе

# In[31]:


features = ['w1m18-m19', 'w2m18-m19', 'w3m18-m19']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4m18-m19'])
ohp_df['w5m18-m19'] = model.predict(ohp_df[features]).round(0)
features = ['w1tu18-tu19', 'w2tu18-tu19', 'w3tu18-tu19']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4tu18-tu19'])
ohp_df['w5tu18-tu19'] = model.predict(ohp_df[features]).round(0)
features = ['w1w18-w19', 'w2w18-w19', 'w3w18-w19']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4w18-w19'])
ohp_df['w5w18-w19'] = model.predict(ohp_df[features]).round(0)
features = ['w1th18-th19', 'w2th18-th19', 'w3th18-th19']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4th18-th19'])
ohp_df['w5th18-th19'] = model.predict(ohp_df[features]).round(0)
features = ['w1f18-f19', 'w2f18-f19', 'w3f18-f19']
model = LinearRegression()
model.fit(ohp_df[features], ohp_df['w4f18-f19'])
ohp_df['w5f18-f19'] = model.predict(ohp_df[features]).round(0)

# In[32]:


first_50 = ohp_df.iloc[:, :1]
last_50 = ohp_df.iloc[:, -50:]
ndf = pd.concat([first_50, last_50], axis=1)

# In[33]:


ndf = ndf.applymap(lambda x: int(x) if isinstance(x, float) else x)

# In[34]:


ndf

# In[35]:


hours_predict = pd.DataFrame(
    columns=['office_id', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])

# Цикл по всем строкам исходного DataFrame
for i in range(len(oh_df)):
    # Добавляем новую строку в новый DataFrame
    hours_predict = pd.concat([hours_predict, pd.DataFrame({
        'office_id': [oh_df['office_id'].iloc[i]],
        'monday': [[]],
        'tuesday': [[]],
        'wednesday': [[]],
        'thursday': [[]],
        'friday': [[]],
        'saturday': [[]],
        'sunday': [[]]
    })], ignore_index=True)

# In[36]:


for i in oh_df['office_id']:
    index = hours_predict[hours_predict['office_id'] == i].index[0]
    hours_predict.loc[index, 'monday'] = [ndf['w5m9-m10'].loc[ndf['office_id'] == i],
                                          ndf['w5m10-m11'].loc[ndf['office_id'] == i],
                                          ndf['w5m11-m12'].loc[ndf['office_id'] == i],
                                          ndf['w5m12-m13'].loc[ndf['office_id'] == i],
                                          ndf['w5m13-m14'].loc[ndf['office_id'] == i],
                                          ndf['w5m14-m15'].loc[ndf['office_id'] == i],
                                          ndf['w5m15-m16'].loc[ndf['office_id'] == i],
                                          ndf['w5m16-m17'].loc[ndf['office_id'] == i],
                                          ndf['w5m17-m18'].loc[ndf['office_id'] == i],
                                          ndf['w5m18-m19'].loc[ndf['office_id'] == i]]

# In[37]:


for i in oh_df['office_id']:
    index = hours_predict[hours_predict['office_id'] == i].index[0]
    hours_predict.loc[index, 'tuesday'] = [ndf['w5tu9-tu10'].loc[ndf['office_id'] == i],
                                           ndf['w5tu10-tu11'].loc[ndf['office_id'] == i],
                                           ndf['w5tu11-tu12'].loc[ndf['office_id'] == i],
                                           ndf['w5tu12-tu13'].loc[ndf['office_id'] == i],
                                           ndf['w5tu13-tu14'].loc[ndf['office_id'] == i],
                                           ndf['w5tu14-tu15'].loc[ndf['office_id'] == i],
                                           ndf['w5tu15-tu16'].loc[ndf['office_id'] == i],
                                           ndf['w5tu16-tu17'].loc[ndf['office_id'] == i],
                                           ndf['w5tu17-tu18'].loc[ndf['office_id'] == i],
                                           ndf['w5tu18-tu19'].loc[ndf['office_id'] == i]]

# In[38]:


for i in oh_df['office_id']:
    index = hours_predict[hours_predict['office_id'] == i].index[0]
    hours_predict.loc[index, 'wednesday'] = [ndf['w5w9-w10'].loc[ndf['office_id'] == i],
                                             ndf['w5w10-w11'].loc[ndf['office_id'] == i],
                                             ndf['w5w11-w12'].loc[ndf['office_id'] == i],
                                             ndf['w5w12-w13'].loc[ndf['office_id'] == i],
                                             ndf['w5w13-w14'].loc[ndf['office_id'] == i],
                                             ndf['w5w14-w15'].loc[ndf['office_id'] == i],
                                             ndf['w5w15-w16'].loc[ndf['office_id'] == i],
                                             ndf['w5w16-w17'].loc[ndf['office_id'] == i],
                                             ndf['w5w17-w18'].loc[ndf['office_id'] == i],
                                             ndf['w5w18-w19'].loc[ndf['office_id'] == i]]

# In[39]:


for i in oh_df['office_id']:
    index = hours_predict[hours_predict['office_id'] == i].index[0]
    hours_predict.loc[index, 'thursday'] = [ndf['w5th9-th10'].loc[ndf['office_id'] == i],
                                            ndf['w5th10-th11'].loc[ndf['office_id'] == i],
                                            ndf['w5th11-th12'].loc[ndf['office_id'] == i],
                                            ndf['w5th12-th13'].loc[ndf['office_id'] == i],
                                            ndf['w5th13-th14'].loc[ndf['office_id'] == i],
                                            ndf['w5th14-th15'].loc[ndf['office_id'] == i],
                                            ndf['w5th15-th16'].loc[ndf['office_id'] == i],
                                            ndf['w5th16-th17'].loc[ndf['office_id'] == i],
                                            ndf['w5th17-th18'].loc[ndf['office_id'] == i],
                                            ndf['w5th18-th19'].loc[ndf['office_id'] == i]]

# In[40]:


for i in oh_df['office_id']:
    index = hours_predict[hours_predict['office_id'] == i].index[0]
    hours_predict.loc[index, 'friday'] = [ndf['w5f9-f10'].loc[ndf['office_id'] == i],
                                          ndf['w5f10-f11'].loc[ndf['office_id'] == i],
                                          ndf['w5f11-f12'].loc[ndf['office_id'] == i],
                                          ndf['w5f12-f13'].loc[ndf['office_id'] == i],
                                          ndf['w5f13-f14'].loc[ndf['office_id'] == i],
                                          ndf['w5f14-f15'].loc[ndf['office_id'] == i],
                                          ndf['w5f15-f16'].loc[ndf['office_id'] == i],
                                          ndf['w5f16-f17'].loc[ndf['office_id'] == i],
                                          ndf['w5f17-f18'].loc[ndf['office_id'] == i],
                                          ndf['w5f18-f19'].loc[ndf['office_id'] == i]]






