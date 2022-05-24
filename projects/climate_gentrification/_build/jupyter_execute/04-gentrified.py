#!/usr/bin/env python
# coding: utf-8

# # PART 4: Gentrified Identification
# 
# Haoyu Yue, Department of Urban Design and Planning, University of Washington

# ## Preparation

# In[526]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import contextily as ctx
from matplotlib_scalebar.scalebar import ScaleBar
from matplotlib.patches import Patch


# In[620]:


get_ipython().run_line_magic('matplotlib', 'widget')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[528]:


pd.set_option('display.max_columns', None)


# ## Import the datasets

# In[529]:


sf_bg = gpd.read_file('data/sf_bg/sf_bg.geojson')

popu_2015 = pd.read_csv('data/ACS_5Y/population/ACSDT5Y2015.B01003.csv')
popu_2020 = pd.read_csv('data/ACS_5Y/population/ACSDT5Y2020.B01003.csv')

education_2015 = pd.read_csv('data/ACS_5Y/education/ACSDT5Y2015.B15003.csv')
education_2020 = pd.read_csv('data/ACS_5Y/education/ACSDT5Y2020.B15003.csv')

income_2015 = pd.read_csv('data/ACS_5Y/income/ACSDT5Y2015.B19013.csv')
income_2020 = pd.read_csv('data/ACS_5Y/income/ACSDT5Y2020.B19013.csv')

rent_2015 = pd.read_csv('data/ACS_5Y/rent/ACSDT5Y2015.B25064.csv')
rent_2020 = pd.read_csv('data/ACS_5Y/rent/ACSDT5Y2020.B25064.csv')

whiteonly_2015 = pd.read_csv('data/ACS_5Y/whiteonly/ACSDT5Y2015.B02008.csv')
whiteonly_2020 = pd.read_csv('data/ACS_5Y/whiteonly/ACSDT5Y2020.B02008.csv')


# In[530]:


popu_2015['geoid'] = popu_2015['id'].str.slice(-12,)
popu_2020['geoid'] = popu_2020['id'].str.slice(-12,)

education_2015['geoid'] = education_2015['id'].str.slice(-12,)
education_2020['geoid'] = education_2020['id'].str.slice(-12,)

income_2015['geoid'] = income_2015['id'].str.slice(-12,)
income_2020['geoid'] = income_2020['id'].str.slice(-12,)

rent_2015['geoid'] = rent_2015['id'].str.slice(-12,)
rent_2020['geoid'] = rent_2020['id'].str.slice(-12,)

whiteonly_2015['geoid'] = whiteonly_2015['id'].str.slice(-12,)
whiteonly_2020['geoid'] = whiteonly_2020['id'].str.slice(-12,)


# ## Data Preprocessing

# In[531]:


sf_bg = sf_bg[['GEOID','area','geometry']]


# ### Total Population

# In[532]:


popu_2015 = popu_2015.iloc[:,[0,4]]
popu_2020 = popu_2020.iloc[:,[0,4]]


# In[533]:


popu_2015.columns = ['popu_2015','GEOID']
popu_2020.columns = ['popu_2020','GEOID']


# ### Mean Education Years

# In[534]:


education_2015 = education_2015.iloc[:,[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,52]]
education_2020 = education_2020.iloc[:,[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,52]]


# In[535]:


edu_table = education_2015.copy()
edu_mean = (edu_table.iloc[:,4] * 1 + edu_table.iloc[:,5] * 2 + edu_table.iloc[:,6] * 3 + edu_table.iloc[:,7] * 4 + edu_table.iloc[:,8] * 5 +edu_table.iloc[:,9] * 6 + edu_table.iloc[:,10] * 7 + edu_table.iloc[:,11] * 8 + edu_table.iloc[:,12] * 9 + edu_table.iloc[:,13] * 10 + edu_table.iloc[:,14] * 11 + edu_table.iloc[:,15] * 12 + edu_table.iloc[:,16] * 12 + edu_table.iloc[:,17] * 12 + edu_table.iloc[:,18] * 13 + edu_table.iloc[:,19] * 15 + edu_table.iloc[:,20] * 15 + edu_table.iloc[:,21] * 16 + edu_table.iloc[:,22] * 18 + edu_table.iloc[:,23] * 20 + edu_table.iloc[:,24] * 22) / edu_table.iloc[:,0]
edu_attain_2015 = pd.concat([edu_table.iloc[:,-1], edu_mean], axis=1)
edu_attain_2015.columns = ['GEOID','edu_2015']

edu_table = education_2020.copy()
edu_mean = (edu_table.iloc[:,4] * 1 + edu_table.iloc[:,5] * 2 + edu_table.iloc[:,6] * 3 + edu_table.iloc[:,7] * 4 + edu_table.iloc[:,8] * 5 +edu_table.iloc[:,9] * 6 + edu_table.iloc[:,10] * 7 + edu_table.iloc[:,11] * 8 + edu_table.iloc[:,12] * 9 + edu_table.iloc[:,13] * 10 + edu_table.iloc[:,14] * 11 + edu_table.iloc[:,15] * 12 + edu_table.iloc[:,16] * 12 + edu_table.iloc[:,17] * 12 + edu_table.iloc[:,18] * 13 + edu_table.iloc[:,19] * 15 + edu_table.iloc[:,20] * 15 + edu_table.iloc[:,21] * 16 + edu_table.iloc[:,22] * 18 + edu_table.iloc[:,23] * 20 + edu_table.iloc[:,24] * 22) / edu_table.iloc[:,0]
edu_attain_2020 = pd.concat([edu_table.iloc[:,-1], edu_mean], axis=1)
edu_attain_2020.columns = ['GEOID','edu_2020']


# ### Median income

# In[536]:


income_2015 = income_2015.iloc[:,[0,4]]
income_2020 = income_2020.iloc[:,[0,4]]

income_2015.columns = ['Median HH Income (in 2015 dollars)','GEOID']
income_2020.columns = ['Median HH Income (in 2020 dollars)','GEOID']


# In[537]:


str = ["250,000+",'-']
num = [300000,np.nan]
for replace_str,replace_num in zip(str,num):
    replace_index = income_2015[income_2015['Median HH Income (in 2015 dollars)'] == replace_str].index
    income_2015.iloc[replace_index,0] = replace_num
income_2015['Median HH Income (in 2015 dollars)'] = income_2015['Median HH Income (in 2015 dollars)'].astype('float')

str = ["250,000+",'-','2,500-']
num = [300000,np.nan,2000]
for replace_str,replace_num in zip(str,num):
    replace_index = income_2020[income_2020['Median HH Income (in 2020 dollars)'] == replace_str].index
    income_2020.iloc[replace_index,0] = replace_num
income_2020['Median HH Income (in 2020 dollars)'] = income_2020['Median HH Income (in 2020 dollars)'].astype('float')  * 1.08 #inflation


# ### Rent

# In[538]:


rent_2015 = rent_2015.iloc[:,[0,4]]
rent_2020 = rent_2020.iloc[:,[0,4]]

rent_2015.columns = ['Median Gross Rent 2015','GEOID']
rent_2020.columns = ['Median Gross Rent 2020','GEOID']


# In[539]:


str = ["3,500+",'-']
num = [4000,np.nan]
for replace_str,replace_num in zip(str,num):
    replace_index = rent_2020[rent_2020['Median Gross Rent 2020'] == replace_str].index
    rent_2020.iloc[replace_index,0] = replace_num
rent_2020['Median Gross Rent 2020'] = rent_2020['Median Gross Rent 2020'].astype('float')

str = ["3,500+",'-','100-']
num = [4000,np.nan,'0']
for replace_str,replace_num in zip(str,num):
    replace_index = rent_2015[rent_2015['Median Gross Rent 2015'] == replace_str].index
    rent_2015.iloc[replace_index,0] = replace_num
rent_2015['Median Gross Rent 2015'] = rent_2015['Median Gross Rent 2015'].astype('float') * 1.08


# ### White Only

# In[540]:


whiterate_2015 = whiteonly_2015.iloc[:,[0,4]]
whiterate_2015.columns = ['white_15','GEOID']


# In[541]:


whiterate_2020 = whiteonly_2020.iloc[:,[0,4]]
whiterate_2020.columns = ['white_20','GEOID']


# ### Merge All

# In[542]:


sf_demo_2015 = sf_bg.merge(popu_2015,how='left',on='GEOID').merge(edu_attain_2015,how='left',on='GEOID').merge(income_2015,how='left',on='GEOID').merge(rent_2015,how='left',on='GEOID').merge(whiterate_2015,how='left',on='GEOID')
sf_demo_2020 = sf_bg.merge(popu_2020,how='left',on='GEOID').merge(edu_attain_2020,how='left',on='GEOID').merge(income_2020,how='left',on='GEOID').merge(rent_2020,how='left',on='GEOID').merge(whiterate_2020,how='left',on='GEOID')


# ## Mismatch of block groups
# 
# We can see that here are some 2020 geoid cannot be matched to 2015. So we need to import the census block group 2020 to get the mean values of each missing block group.

# In[543]:


cbg_2020 = gpd.read_file('data/tl_2020_06_bg/tl_2020_06_bg.shp')
cbg_2020 = cbg_2020.to_crs('EPSG:3857')

sf_boundary = gpd.read_file('data/sf_boundaries.gpkg')
sf_boundary = sf_boundary.to_crs('EPSG:3857')


# In[544]:


ca_demo_2020_base = cbg_2020.merge(
    popu_2020,how='left',on='GEOID').merge(
        edu_attain_2020,how='left',on='GEOID').merge(
            income_2020,how='left',on='GEOID').merge(
                rent_2020,how='left',on='GEOID').merge(
                    whiterate_2020,how='left',on='GEOID') #merge them


# In[545]:


sf_demo_2020_base = ca_demo_2020_base.clip(sf_boundary)
#remove some nonsense shapes
sf_demo_2020_base = sf_demo_2020_base[(sf_demo_2020_base.geometry.type != 'LineString')&(sf_demo_2020_base.geometry.type != 'GeometryCollection')&(sf_demo_2020_base.geometry.type != 'Point')]


# In[546]:


sf_demo_2020_na = sf_demo_2020[sf_demo_2020.popu_2020.isnull()] #filter the NA rows


# In[547]:


sf_demo_2020_empty = pd.DataFrame(columns=sf_demo_2020_na.columns)

for i in range(0,len(sf_demo_2020_na)):
    sf_demo_na_i = sf_demo_2020_na.iloc[i:i+1]
    inter_result = sf_demo_2020_base.overlay(sf_demo_na_i,how='intersection')

    groupby_sum = inter_result.groupby('GEOID_2')[['popu_2020_1']].mean()
    groupby_mean = inter_result.groupby('GEOID_2')[['edu_2020_1','Median HH Income (in 2020 dollars)_1','Median Gross Rent 2020_1','white_20_1']].mean()

    sf_demo_na_i_full = sf_demo_na_i[['GEOID','area','geometry']].merge(groupby_sum,left_on='GEOID', right_index = True).merge(groupby_mean, left_on='GEOID', right_index = True)
    sf_demo_na_i_full.columns = sf_demo_2020_empty.columns
    sf_demo_2020_empty = sf_demo_2020_empty.append(sf_demo_na_i_full)


# In[548]:


sf_demo_2020_all = sf_demo_2020[~sf_demo_2020.popu_2020.isnull()].append(sf_demo_2020_empty)


# In[549]:


sf_demo = sf_demo_2015.merge(sf_demo_2020_all,on='GEOID')


# In[550]:


sf_demo = sf_demo[['GEOID', 'area_x', 'geometry_x', 'popu_2015', 'edu_2015',
       'Median HH Income (in 2015 dollars)', 'Median Gross Rent 2015',
       'white_15', 'popu_2020', 'edu_2020',
       'Median HH Income (in 2020 dollars)', 'Median Gross Rent 2020',
       'white_20']]
sf_demo.columns = ['GEOID', 'area', 'geometry', 'popu_2015', 'edu_2015',
       'Median HH Income (in 2015 dollars)', 'Median Gross Rent 2015',
       'white_15', 'popu_2020', 'edu_2020',
       'Median HH Income (in 2020 dollars)', 'Median Gross Rent 2020',
       'white_20']


# In[551]:


sf_demo = gpd.GeoDataFrame(sf_demo, crs="EPSG:3857", geometry=sf_demo.geometry)


# In[553]:


sf_demo


# ## Choose the gentrified region by using thresholds

# In[554]:


rent_increase_rate = (sf_demo['Median Gross Rent 2020']/sf_demo['Median Gross Rent 2015']).mean()
edu_increase_rate = (sf_demo['edu_2020']/sf_demo['edu_2015']).mean()
income_increase_rate = (sf_demo['Median HH Income (in 2020 dollars)']/sf_demo['Median HH Income (in 2015 dollars)']).mean()


# In[557]:


rent_increase_rate


# ### Income Below 40% in 2015

# In[559]:


income_threshold_2015 = sf_demo.sort_values('Median HH Income (in 2015 dollars)').iloc[int(0.4*len(sf_demo)):int(0.4*len(sf_demo)+1),5]


# In[719]:


income_threshold_2015


# In[720]:


lowerincome_15_index = sf_demo[sf_demo['Median HH Income (in 2015 dollars)'] < income_threshold_2015.values[0]].index
lowerincome_15_index


# ### Edu or income increase from 2015 to 2020

# In[561]:


high_edu_increaes_index = sf_demo[(sf_demo['edu_2020']/sf_demo['edu_2015']) > edu_increase_rate].index


# In[562]:


high_income_increaes_index = sf_demo[(sf_demo['Median HH Income (in 2020 dollars)']/sf_demo['Median HH Income (in 2015 dollars)']) > income_increase_rate].index


# ### Rent Increase from 2015 to 2020

# In[563]:


high_rent_increaes_index = sf_demo[(sf_demo['Median Gross Rent 2020']/sf_demo['Median Gross Rent 2015']) > rent_increase_rate].index


# ### All three requirements

# In[564]:


gentrified_index = ((high_edu_increaes_index | high_income_increaes_index) & high_rent_increaes_index) & lowerincome_15_index


# In[565]:


sf_gentrified = sf_demo.iloc[gentrified_index]


# In[566]:


sf_gentrified


# In[755]:


#add the density restriction
sf_gentrified_plot = sf_gentrified.copy()
sf_gentrified_plot['density'] = (sf_gentrified.popu_2015/sf_gentrified.area)
sf_gentrified_density = sf_gentrified_plot[sf_gentrified_plot['density']>0.0001]


# In[732]:


pd.DataFrame(lowerincome_15_index).to_csv('potential_area.csv')


# In[733]:


sf_gentrified_density.plot()


# ## Cluster

# In[734]:


cluster_data = sf_gentrified_density.copy()
cluster_data = cluster_data[['popu_2015', 'edu_2015',
       'Median HH Income (in 2015 dollars)', 'Median Gross Rent 2015',
       'white_15', 'popu_2020', 'edu_2020',
       'Median HH Income (in 2020 dollars)', 'Median Gross Rent 2020',
       'white_20', 'density']]


# In[735]:


cluster_data['white_rate'] = (cluster_data['white_20']/cluster_data['popu_2020'])/(cluster_data['white_15']/cluster_data['popu_2015'])
cluster_data['rent_rate'] = cluster_data['Median Gross Rent 2020']/cluster_data['Median Gross Rent 2015']
cluster_data['income_rate'] = cluster_data['Median HH Income (in 2020 dollars)']/cluster_data['Median HH Income (in 2015 dollars)']
cluster_data['popu_rate'] = cluster_data['popu_2020']/cluster_data['popu_2015']
cluster_data['edu_rate'] = cluster_data['edu_2020']/cluster_data['edu_2015']


# In[736]:


cluster_data


# In[737]:


normalized_list = ['rent_rate', 'white_rate','income_rate','popu_rate','edu_rate']
Normalized_data = cluster_data[normalized_list]


# In[738]:


for i in normalized_list:
    Normalized_data[i] = Normalized_data[i].astype(float)
    Normalized_data[i] = (Normalized_data[i] - np.mean(Normalized_data[i]))/np.std(Normalized_data[i])


# In[739]:


cluster_data = Normalized_data.dropna()


# In[740]:


cluster_data = cluster_data[['rent_rate','income_rate','edu_rate']]
cluster_data


# In[741]:


import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn.cluster import MiniBatchKMeans

SSE = []
for k in range(1,16):
    k_means = cluster.KMeans(n_clusters=k,random_state=12)
    k_means.fit(cluster_data)
    SSE.append(k_means.inertia_)

plt.plot(range(1,16), SSE)

plt.xlabel('Number of Clusters')
plt.ylabel('SSE')

plt.show()


# In[744]:


from sklearn.metrics import silhouette_score

import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn.cluster import MiniBatchKMeans

silhouette = []
for k in range(2,15):
    k_means = cluster.MiniBatchKMeans(n_clusters=k,random_state=12)
    k_means.fit(cluster_data)
    silhouette.append(silhouette_score(cluster_data, k_means.labels_))

plt.plot(range(2,15), SSE)

plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Scores')

plt.show()


# In[745]:


#fit the clustering
k_means = cluster.KMeans(n_clusters=3, max_iter=50, random_state=5)
k_means.fit(cluster_data) 


# In[746]:


# print the centroids of all clusters
dfCenters = pd.DataFrame(data=k_means.cluster_centers_, columns=cluster_data.columns)
ClusterName = ['Pattern A', 'Pattern B', 'Pattern C'] #,'Pattern D','Pattern E','Pattern F','Pattern G','Pattern H'] 
  
dfCenters['ClusterName'] = ClusterName
dfCenters


# In[747]:


#using heatmap to visualize the clustering results
import plotly
import plotly.graph_objs as go
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
heatmap = min_max_scaler.fit_transform(k_means.cluster_centers_)

heatmap = pd.DataFrame(data=heatmap, columns=cluster_data.columns) 
heatmap['ClusterName'] = ClusterName

data = [go.Heatmap(z=heatmap.values.tolist(), 
                   y=ClusterName,
                   x=cluster_data.columns,
                   colorscale='inferno')]

plotly.offline.iplot(data, filename='pandas-heatmap')


# In[748]:


cluster_data["pattern"] = k_means.labels_
cluster_data


# In[749]:


sf_cluster = sf_bg.merge(cluster_data,left_index=True,right_index=True,how='left')
sf_cluster


# ## Descriptive Statistics

# ### Gentrified VS Non-Gentrified

# In[581]:


sf_demo['gentrified'] = 0


# In[583]:


sf_demo.iloc[sf_gentrified_density.index,-1] = 1


# In[588]:


sf_demo['gentrified'].value_counts()


# In[589]:


sf_demo


# In[593]:


sf_demo['popu_2020'] = sf_demo['popu_2020'].replace(0,1)
sf_demo['popu_2015'] = sf_demo['popu_2015'].replace(0,1)


# In[594]:


sf_demo['white_rate_20'] = (sf_demo['white_20']/sf_demo['popu_2020'])
sf_demo['white_rate_15'] = sf_demo['white_15']/sf_demo['popu_2015']


# In[611]:


sf_demo['white_rate_20'] = sf_demo['white_rate_20'].astype('float')


# In[612]:


sf_demo.groupby('gentrified').mean()


# ### Patterns

# In[703]:


sf_cluster.dropna(subset=['pattern']).merge(sf_demo,how='left',on="GEOID").groupby('pattern').mean().to_clipboard()


# In[709]:


sf_cluster.dropna(subset=['pattern']).pattern.value_counts()


# ## Gentrification Visualization

# In[750]:


sf_demo_gen = sf_demo.copy()
sf_demo_gen['gentrified'] = np.nan


# In[751]:


sf_demo_gen.loc[list(sf_gentrified_density.index),'gentrified'] = 'Gentrified'
sf_demo_gen.gentrified = sf_demo_gen.gentrified.fillna('Non-Gentrified')


# In[752]:


sf_demo_gen_pattern = sf_demo_gen.merge(cluster_data[['pattern']],how='left',left_index=True,right_index=True)
pattern_colors = {0:"Pattern A",1:'Pattern B',2:'Pattern C',3:'Pattern D',4:'Pattern E',5:'Pattern F',6:'Pattern G',7:'Pattern H'}
colors = ["#AE4E4F",'#795F4F','#FFD37A','#579592','#94B059','#23192B']
sf_demo_gen_pattern['color'] = sf_demo_gen_pattern['pattern']
sf_demo_gen_pattern = sf_demo_gen_pattern.replace({"color": pattern_colors})


# In[753]:


f,ax=plt.subplots(figsize=(15,15))
sf_demo_gen_pattern.plot(ax=ax,edgecolor='#A3814E',linewidth=0.1,legend=True,alpha=0.2,facecolor='#FFC66E')
sf_gentrified_density.plot(ax=ax,facecolor='#005B85',alpha=0.9,linewidth=0)
ctx.add_basemap(ax=ax, crs=sf_bg.crs, source=ctx.providers.Stamen.TonerLite)
ax.add_artist(ScaleBar(4.0,box_alpha=0.6,border_pad=1))

legend_elements = [Patch(facecolor='#005B85', alpha=0.9,edgecolor='gray',label='Gentrified Census Block Groups'),
                    Patch(edgecolor='#A3814E',alpha=0.2,facecolor='#FFC66E',label='Non-Gentrified Census Block Groups')]
ax.legend(handles=legend_elements, loc=[0.01,0.04],fontsize=16)
plt.axis('off')


# In[754]:


f,ax=plt.subplots(figsize=(80,80))
sf_demo_gen_pattern.plot(ax=ax,edgecolor='white',linewidth=0.4,alpha=0.2,facecolor='#FFC66E')
sf_demo_gen_pattern.plot(ax=ax,column='color',linewidth=0.4,alpha=1,legend=True,categorical=True,cmap='tab10',legend_kwds={'loc': [0.02,0.03],'fontsize':16})
ctx.add_basemap(ax=ax, crs=sf_bg.crs, source=ctx.providers.Stamen.TonerLite)
ax.add_artist(ScaleBar(4.0,box_alpha=0,border_pad=1))
plt.axis('off')


# In[718]:


sf_demo_gen_pattern.to_file('data/regression/sf_demo_gen_pattern.geojson', driver='GeoJSON')


# In[ ]:




