#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import datetime
from Parser.TableParser import TableParser
from Parser.HolidaysParser import HolidaysParser


# In[4]:

def create_ML_model():
    all_df = []
    source = 'Datasets/processed_xlsx/'
    for directory in os.listdir(source):
        for filepath in os.listdir(source + directory):
            df = pd.read_excel(source + directory + '/' + filepath)
            all_df.append(df)


    # In[5]:


    df = pd.concat(all_df)


    # In[6]:


    df.info()


    # In[7]:


    df = df.drop(['Unnamed: 0', 'patient', 'hospitalized', 'executive', 'brigade', 'address', 'number', 'called by'], axis=1)


    # In[8]:


    df.info()


    # In[9]:


    df = df.dropna()


    # In[10]:


    df.info()


    # In[11]:


    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofweek'] = df['date'].dt.dayofweek


    # In[12]:


    all_weather_dfs = []
    for year in [2020, 2021, 2022]:
        weather_df = pd.read_excel(f'additionalData/weather/{year}.xls', skiprows=6)
        all_weather_dfs.append(weather_df)
    df_weather = pd.concat(all_weather_dfs)


    # In[13]:


    df_weather = df_weather.rename({'Местное время в Нижнем Новгороде':'datetime'}, axis=1)
    df_weather['datetime'] = pd.to_datetime(df_weather['datetime'])


    # In[14]:


    df_weather['date'] = df_weather['datetime'].dt.date.astype('datetime64')


    # In[15]:


    df_weather['date']


    # In[16]:


    df_weather = df_weather.groupby('date')[['T', 'Po', 'U']].mean()


    # In[17]:


    df_weather.info()


    # In[18]:


    df.info()


    # In[19]:


    holidays = []
    for year in (2020, 2021, 2022):
        holidays.extend(HolidaysParser.get_holidays(year))


    # In[20]:


    holidays = [datetime.datetime.strptime(holiday, "%d.%m.%Y") for holiday in holidays]


    # In[41]:


    holidays_df = pd.DataFrame({'holiday day': 1, 'date': holidays})


    # In[42]:


    total_df = df.merge(df_weather, on='date', how='left').merge(holidays_df, on='date', how='left')


    # In[43]:


    total_df['holiday day'] = total_df['holiday day'].fillna(0)


    # In[44]:


    total_df['day'] = total_df['date'].dt.day
    total_df['month'] = total_df['date'].dt.month
    total_df['year'] = total_df['date'].dt.year


    # In[45]:


    total_df = total_df.iloc[:, -9:]


    # In[47]:


    statistic_for_period = total_df.groupby(['year','month', 'day']).count()['dayofyear']


    # In[49]:


    result_df = total_df.merge(statistic_for_period, on=['month', 'year', 'day'], how='left')


    # In[51]:


    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score


    # In[52]:


    result_df = result_df.rename({'dayofyear_y': 'calls'}, axis=1)


    # In[53]:


    result_df = result_df.dropna()


    # In[54]:


    X = result_df.drop('calls', axis=1)
    y = result_df['calls']


    # In[55]:


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)


    # In[56]:


    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    r2_score(y_test, pred)




