#!/usr/bin/env python
# coding: utf-8

# # PART 5: Regression
# 
# Haoyu Yue, Department of Urban Design and Planning, University of Washington

# ## Preparation

# In[77]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import contextily as ctx
from matplotlib_scalebar.scalebar import ScaleBar
from matplotlib.patches import Patch
import math
import statsmodels.api as sm


# In[567]:


sf_demo_gen_pattern = gpd.read_file('data/regression/sf_demo_gen_pattern.geojson')
sf_invest = gpd.read_file('data/regression/sf_invest.geojson')


# In[568]:


invest_types = ['research and planning', 'fire prevention', 'climate action',
       'public transportation', 'housing', 'green space', 'others', 'vehicle',
       'building', 'utilities', 'agriculture', 'clean air']


# In[608]:


logistic_data = sf_invest.groupby('GEOID')[invest_types].sum()


# In[609]:


popu_area = sf_demo_gen_pattern.popu_2020 / 1000 * sf_demo_gen_pattern.area / 1000000
popu_area.index = logistic_data.index


# In[610]:


for i in invest_types:
    logistic_data.loc[:,i] = (logistic_data.loc[:,i]/popu_area).apply(np.log).replace(-np.inf,0) #((logistic_data.loc[:,i]+1).apply(np.log)/popu_area)  


# In[611]:


logistic_data = logistic_data.merge(sf_demo_gen_pattern[['GEOID','gentrified']],left_index=True,right_on='GEOID').replace(['Gentrified','Non-Gentrified'],[1,0])


# In[612]:


logistic_data = logistic_data.set_index('GEOID')


# In[613]:


logistic_data


# In[614]:


logistic_list = ['fire prevention', 'climate action',
       'public transportation', 'housing', 'green space', 'vehicle',
       'building', 'utilities',  'gentrified']
logistic_data = logistic_data[logistic_list]


# In[615]:


sf_demo_gen_pattern['white_rate'] = (sf_demo_gen_pattern['white_20']/sf_demo_gen_pattern['popu_2020'])/(sf_demo_gen_pattern['white_15']/sf_demo_gen_pattern['popu_2015'])-1
sf_demo_gen_pattern['edu_rate'] = (sf_demo_gen_pattern['edu_2020'])/(sf_demo_gen_pattern['edu_2015'])-1
sf_demo_gen_pattern['popu_rate'] = (sf_demo_gen_pattern['popu_2020'])/(sf_demo_gen_pattern['popu_2015'])-1
sf_demo_gen_pattern['income_rate'] = (sf_demo_gen_pattern['Median HH Income (in 2020 dollars)'])/(sf_demo_gen_pattern['Median HH Income (in 2015 dollars)'])-1
sf_demo_gen_pattern['rent_rate'] = (sf_demo_gen_pattern['Median Gross Rent 2020'])/(sf_demo_gen_pattern['Median Gross Rent 2015'])-1
sf_demo_gen_pattern['white_rate_15'] = sf_demo_gen_pattern['white_15']/sf_demo_gen_pattern['popu_2015']
sf_demo_gen_pattern['density'] = sf_demo_gen_pattern['popu_2015']/sf_demo_gen_pattern['area']


# In[616]:


ols_data = logistic_data.merge(sf_demo_gen_pattern[['white_rate','edu_rate','popu_rate','income_rate','rent_rate','GEOID']],left_index=True,right_on='GEOID',how='left')
logistic_data = logistic_data.merge(sf_demo_gen_pattern[['white_rate_15','density','edu_2015','Median Gross Rent 2015','GEOID']],left_index=True,right_on='GEOID',how='left')


# In[617]:


logistic_data = logistic_data.replace(np.inf,np.nan).dropna()
logistic_data['Median Gross Rent 2015'] = logistic_data['Median Gross Rent 2015'].apply(np.log)


# ## occupied data

# In[618]:


occupied = pd.read_csv('data/ACS_5Y/occupy/occupy.csv')


# In[619]:


occupied['geoid'] = occupied['GEOID'].str.slice(-12,)
occupied['ownership_rate'] = occupied['Owner occupied']/occupied['Total']
occupied = occupied[['geoid','ownership_rate']]


# In[620]:


logistic_data = logistic_data.merge(occupied,left_on='GEOID',right_on='geoid',how='left')
ols_data = ols_data.merge(occupied,left_on='GEOID',right_on='geoid',how='left')


# In[621]:


potential_area = pd.read_csv('potential_area.csv')
potential_area_list = list(potential_area['0'])


# In[622]:


logistic_data = logistic_data[logistic_data.index.isin(potential_area_list)]


# In[623]:


ols_data['gen_index'] = ((
    ols_data.edu_rate.mean() - ols_data.edu_rate)/(ols_data.edu_rate.std()) + (
        ols_data.income_rate.mean() - ols_data.income_rate)/(ols_data.income_rate.std()) + (
        ols_data.rent_rate.mean() - ols_data.rent_rate)/(ols_data.rent_rate.std()))/3


# In[624]:


ols_data = ols_data.dropna()


# In[625]:


logistic_data = logistic_data[['fire prevention', 'climate action', 'public transportation', 'housing',
       'green space', 'vehicle', 'building', 'utilities', 'gentrified',
       'white_rate_15','edu_2015', 'Median Gross Rent 2015','density',
       'GEOID', 'ownership_rate']]


# In[626]:


logistic_data


# In[628]:


logistic_data = logistic_data[logistic_data.density > 0.001]
logistic_data


# In[633]:


ols = logistic_data.merge(ols_data[['GEOID','gen_index']],how='left',on='GEOID')
ols.columns


# In[647]:


ols


# In[652]:


from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = logistic_data.drop(["gentrified",'GEOID'],1)
y = logistic_data["gentrified"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 0)


# In[559]:


from numpy import random
random.seed(3)

clf = linear_model.LogisticRegressionCV(cv = 5, Cs=[0.001,0.005,0.01, 0.1, 0.2, 0.5, 0.8, 1, 5, 10, 20, 50],max_iter=1000)
LogisticCV = clf.fit(X=X_train,y=y_train)

y_pred_train = LogisticCV.predict(X_train)

print('Intercept:', LogisticCV.intercept_)
print('Coefficients:',LogisticCV.coef_)
print('Penalty value', LogisticCV.C_)
print('Training Accuracy Score',accuracy_score(y_train,y_pred_train))


# In[649]:


X_train_log = sm.add_constant(X)
log_reg = sm.Logit(y, X_train_log).fit()
print(log_reg.summary())


# In[654]:


ols = ols.dropna()
X_ols = ols[['fire prevention', 'climate action', 'public transportation', 'housing',
       'green space', 'vehicle', 'building', 'utilities', 
       'white_rate_15', 'edu_2015', 'Median Gross Rent 2015', 'density','ownership_rate']]
y_ols = ols["gen_index"]

X_train_ols = sm.add_constant(X_ols)
ols_reg = sm.OLS(y_ols, X_train_ols).fit()
print(ols_reg.summary())


# In[640]:


X_train_ols.describe()


# In[641]:


y_ols.describe()


# In[186]:


y_hat = log_reg.predict(X_test)
prediction = list(map(round, y_hat))
 
# comparing original and predicted values of y
print('Actual values', list(y_test.values))
print('Predictions :', prediction)


# In[95]:


pre = pd.DataFrame(y_test.values,prediction).reset_index()


# In[100]:


pre['test'] = pre['index'] - pre[0]


# In[102]:


pre['test'].value_counts()


# In[199]:


sf_gen_index = sf_demo_gen_pattern[sf_demo_gen_pattern.gentrified=='Gentrified']


# In[200]:


sf_gen_index['edu_rate'] = (sf_gen_index['edu_2020']/sf_gen_index['edu_2015'])


# In[201]:


sf_gen_index['income'] = (sf_gen_index['Median HH Income (in 2020 dollars)']/sf_gen_index['Median HH Income (in 2015 dollars)'])


# In[202]:


sf_gen_index


# In[58]:


sf_invest


# In[531]:


import statsmodels.api as sm

X_train_ols = sm.add_constant(X_train)
results = sm.Logit(y_train,X_train_ols).fit() 
print(results.summary())


# In[532]:


results.summary()


# In[ ]:




