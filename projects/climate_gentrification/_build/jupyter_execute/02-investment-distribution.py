#!/usr/bin/env python
# coding: utf-8

# # PART 2: Investment Amount Distribution
# 
# Haoyu Yue, Department of Urban Design and Planning, University of Washington

# ## Preparation

# In[83]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon
import itertools
import contextily as ctx
from matplotlib_scalebar.scalebar import ScaleBar


# In[84]:


get_ipython().run_line_magic('matplotlib', 'widget')
#%matplotlib inline


# In[3]:


pd.set_option('display.max_columns', None)


# In[4]:


#census block groups data
sf_bg = gpd.read_file('data/sf_bg/sf_bg.geojson')
sf_bg_geo = sf_bg[['GEOID','geometry','TotalPopu','area']]


# In[5]:


#detailed carbon investment projects info
cci = pd.read_csv('data/cci_2021_all.csv')


# In[6]:


#carbon investment projects info from `01-data-processing`
sf_line_gdf = gpd.read_file('data/sf_project/sf_line.geojson')
sf_point_gdf = gpd.read_file('data/sf_project/sf_point.geojson')
sf_polygon_gdf = gpd.read_file('data/sf_project/sf_polygon.geojson')


# In[7]:


#define variables
YEARS = ['2015','2016','2017','2018','2019','2020']


# ## Types and impact radius of investment
# This part is only for the ouput of programs list, we will use this list to determine the radius of impact and the type of this project

# In[8]:


sf_line = sf_line_gdf.copy()
sf_point = sf_point_gdf.copy()
sf_polygon = sf_polygon_gdf.copy()


# ### Polygon

# In[9]:


sf_polygon_merge = sf_polygon[['proj_id','ReportingCycleName','SubProgramName','ProjectType',
                    'IsBenefitDisadvantagedCommunities','ProjectCompletionDate','TotalProgramGGRFFunding',
                    'geometry',"ProjectName","ProjectDescription"]]
sf_polygon_gdf_merge = sf_polygon_gdf[['proj_id','ReportingCycleName','SubProgramName',
                    'ProjectType','IsBenefitDisadvantagedCommunities','ProjectCompletionDate',
                    'TotalProgramGGRFFunding','geometry',"ProjectName","ProjectDescription"]]


# In[10]:


sf_polygon_merge.columns = ['proj_id', 'ReportingCycleName', 'SubProgramName', 
                            'ProjectType','IsBenefitDisadvantagedCommunities', 'ProjectCompletionDate',
                            'FundingSF', 'geometry',"ProjectName","ProjectDescription"]


# In[11]:


sf_polygon_gdf_merge.columns = ['proj_id', 'ReportingCycleName', 'SubProgramName', 'ProjectType',
                            'IsBenefitDisadvantagedCommunities', 'ProjectCompletionDate','FundingSF', 
                            'geometry',"ProjectName","ProjectDescription"]


# In[12]:


sf_polygon_merge['type'] = 'polygon'


# ### Line

# In[13]:


sf_line_merge = sf_line[['proj_id','ReportingCycleName','SubProgramName','ProjectType',
                    'IsBenefitDisadvantagedCommunities','ProjectCompletionDate','FundingSF',
                    'geometry',"ProjectName","ProjectDescription"]]
sf_line_gdf_merge = sf_line_gdf[['proj_id','ReportingCycleName','SubProgramName','ProjectType',
                    'IsBenefitDisadvantagedCommunities','ProjectCompletionDate','FundingSF',
                    'geometry',"ProjectName","ProjectDescription"]]


# In[14]:


sf_line_merge.columns = ['proj_id', 'ReportingCycleName', 'SubProgramName', 'ProjectType',
                     'IsBenefitDisadvantagedCommunities', 'ProjectCompletionDate','FundingSF', 
                     'geometry',"ProjectName","ProjectDescription"]


# In[15]:


sf_line_gdf_merge.columns = ['proj_id', 'ReportingCycleName', 'SubProgramName', 'ProjectType',
                     'IsBenefitDisadvantagedCommunities', 'ProjectCompletionDate','FundingSF', 
                     'geometry',"ProjectName","ProjectDescription"]


# In[16]:


sf_line_merge['type'] = 'line'


# ### Points

# In[17]:


#select the useful columns, other columns will come from cci dataset
sf_point = sf_point[['proj_id','reportingcyclename','subprogram_name',
                    'BENEFITS_PRIORITY_YN','Funding','geometry']]


# In[18]:


cci_p = cci[['ProjectIDNumber','ReportingCycleName','ProjectType',
            'ProjectCompletionDate',"ProjectName","ProjectDescription"]]
cci_p_filter = cci_p[cci_p['ReportingCycleName'].isin(['2015','2016','2017','2018',
                                                '2019','2020',2015,2016,2017,2018,2019,2020])].drop_duplicates()


# In[19]:


#select the cci within the point projects
cci_point = cci_p_filter[cci_p_filter.ProjectIDNumber.isin(list(sf_point.proj_id.unique()))]


# In[20]:


sf_point_merge = sf_point.merge(cci_point,how='left',
                                left_on=['proj_id','reportingcyclename'],
                                right_on=['ProjectIDNumber',"ReportingCycleName"])


# In[21]:


sf_point_merge = sf_point_merge[['proj_id','reportingcyclename','subprogram_name',
                                'ProjectType','BENEFITS_PRIORITY_YN','ProjectCompletionDate',
                                'Funding','geometry',"ProjectName","ProjectDescription"]]


# In[22]:


sf_point_merge.columns = ['proj_id', 'ReportingCycleName', 'SubProgramName', 'ProjectType',
                            'IsBenefitDisadvantagedCommunities', 'ProjectCompletionDate', 'FundingSF', 
                            'geometry',"ProjectName","ProjectDescription"]


# In[23]:


sf_point_merge['type'] = 'point'


# ### Stack point, line, polygon together

# In[27]:


sf_proj = pd.DataFrame(columns = ['proj_id', 'ReportingCycleName', 'SubProgramName',
                                    'ProjectType','IsBenefitDisadvantagedCommunities', 'ProjectCompletionDate',
                                    'FundingSF', 'geometry',"ProjectName","ProjectDescription"])
sf_proj = sf_proj.append(sf_line_merge).append(sf_point_merge).append(sf_polygon_merge)


# In[ ]:


sf_proj[['proj_id','ProjectName','ProjectDescription']].drop_duplicates().to_clipboard()
#classfiy the proj_id based on project description


# ## Additional Info (Types and impact radius)

# In[35]:


addinfo = pd.read_csv('data/sf_project/proj_id_type_impact.csv') 
addinfo_merge = addinfo[['proj_id','Type','Impact']]


# ### Project Statistic

# In[66]:


sf_proj_stat = sf_proj[['proj_id','ProjectName','ReportingCycleName','IsBenefitDisadvantagedCommunities','FundingSF','geometry']]


# In[67]:


sf_proj_stat = sf_proj_stat.merge(addinfo_merge,on='proj_id',how='left')


# In[68]:


sf_proj_stat.FundingSF = sf_proj_stat.FundingSF.astype('float')


# In[78]:


extre_housing = sf_proj[(sf_proj.proj_id=='44043') | (sf_proj.proj_id=='43922') ]


# In[92]:


sf_point_gdf[sf_point_gdf.proj_id=='44043'].proj_benefits_desc.values


# In[87]:




f, ax = plt.subplots(figsize=(9,5))
gpd.GeoDataFrame(extre_housing,geometry='geometry').plot(ax=ax)
#ca_bg.plot(ax=ax,bounday=sf_invest_all_year_type.boundary)
ctx.add_basemap(ax=ax, crs=sf_bg.crs, source=ctx.providers.Stamen.TonerLite)
#ax.set_title('The Map of Study Area',size=18)
ax.add_artist(ScaleBar(2.0,box_alpha=0,border_pad=1))
plt.axis('off')
plt.tight_layout()


# In[63]:


sf_proj_stat.groupby('Type')['FundingSF'].agg(['count','mean','median','sum']).to_clipboard()


# ### Make the empty for investment dataframe

# In[18]:


geo_bg_15 = sf_bg_geo.copy()
geo_bg_15['year'] = '2015'
geo_bg_16 = sf_bg_geo.copy()
geo_bg_16['year'] = '2016'
geo_bg_17 = sf_bg_geo.copy()
geo_bg_17['year'] = '2017'
geo_bg_18 = sf_bg_geo.copy()
geo_bg_18['year'] = '2018'
geo_bg_19 = sf_bg_geo.copy()
geo_bg_19['year'] = '2019'
geo_bg_20 = sf_bg_geo.copy()
geo_bg_20['year'] = '2020'

geo_bg_invest = geo_bg_15.append(geo_bg_16).append(geo_bg_17).append(geo_bg_18).append(geo_bg_19).append(geo_bg_20)
geo_bg_invest[list(addinfo.Type.unique())] = 0

geo_bg_invest = geo_bg_invest.reset_index().iloc[:,1:]


# ## Investment Index for Line Project

# In[29]:


sf_line_gdf_impact = sf_line_gdf_merge.merge(addinfo_merge,how='left',left_on='proj_id',right_on='proj_id')


# In[30]:


#all invests now is 0
geo_bg_invest[list(addinfo.Type.unique())] = 0
geo_bg = sf_bg_geo.copy()


# In[32]:


#preset the impact radius
impact_radius = {'isolated':1,'neighbor':1200,'regional':5000,'citywide':15000}


# In[34]:


for year,proj_type in itertools.product(sf_line_gdf_impact.ReportingCycleName.unique(),sf_line_gdf_impact.Type.unique()):
    #select projects in particular year and type
    sf_line_gdf_impact_selection = sf_line_gdf_impact[(sf_line_gdf_impact.ReportingCycleName==year)&(sf_line_gdf_impact.Type==proj_type)]
    if len(sf_line_gdf_impact_selection) == 0:
        None
    else:
        try:
            for i in range(len(sf_line_gdf_impact_selection)):
                proj = sf_line_gdf_impact_selection.iloc[i]
                geo_bg['dist'] = geo_bg['geometry'].distance(proj.geometry)#distances from this proj to each cbgs
                geo_bg_impact = geo_bg[geo_bg['dist']<=impact_radius[proj.Impact]]#select impacted cbgs
                index_sum = (geo_bg_impact.TotalPopu * geo_bg_impact.area/((geo_bg_impact.dist+1)**0.5)).sum()#the sum of weight index
                geo_bg_impact.loc[:,'invest_index'] = (geo_bg_impact.loc[:,'TotalPopu'] * geo_bg_impact.loc[:,'area'] / ((geo_bg_impact.loc[:,'dist']+1)**0.5))/index_sum
                #get the index of rows
                year_type_index = geo_bg_invest[(geo_bg_invest.GEOID.isin(geo_bg_impact.GEOID))&(geo_bg_invest.year==year)].index
                geo_bg_impact.index = geo_bg_invest.loc[year_type_index,proj_type].index
                geo_bg_invest.loc[year_type_index,proj_type] += geo_bg_impact.invest_index * proj.FundingSF
                geo_bg_invest = geo_bg_invest.fillna(0) 
        except:
            print('e')


# In[35]:


geo_bg_invest_line = geo_bg_invest.copy()
geo_bg_invest_line.to_file('data/invest_index/geo_bg_invest_line.geojson', driver='GeoJSON')


# ## Investment Index for Point Project

# ### Add addtional info

# In[36]:


sf_point_gdf_impact = sf_point_gdf[['proj_id','reportingcyclename','subprogram_name','BENEFITS_PRIORITY_YN','Funding','geometry','proj_name','proj_desc']]


# In[37]:


sf_point_gdf_impact = sf_point_gdf_impact.merge(addinfo_merge,how='left',left_on='proj_id',right_on='proj_id')


# In[38]:


sf_point_gdf_impact.columns = ['proj_id', 'ReportingCycleName', 'SubProgramName','IsBenefitDisadvantagedCommunities',
                               'FundingSF', 'geometry', 'ProjectName', 'ProjectDescription', 'Type','Impact']


# ### Distribute

# In[39]:


#geo_bg_invest[list(addinfo.Type.unique())] = 0
impact_radius = {'isolated':1,'neighbor':1200,'regional':5000,'citywide':15000}


# In[15]:


#all invests now is 0
geo_bg_invest[list(addinfo.Type.unique())] = 0
geo_bg = sf_bg_geo.copy()


# In[42]:


#for year,proj_type in itertools.product(['2016'],['public transportation']):
for year,proj_type in itertools.product(sf_point_gdf_impact.ReportingCycleName.unique(),sf_point_gdf_impact.Type.unique()):
    #select projects in particular year and type
    sf_point_gdf_impact_selection = sf_point_gdf_impact[(sf_point_gdf_impact.ReportingCycleName==year)&(sf_point_gdf_impact.Type==proj_type)]
    if len(sf_point_gdf_impact_selection) == 0:
        None
    else:
        try:
            for i in range(len(sf_point_gdf_impact_selection)):
                proj = sf_point_gdf_impact_selection.iloc[i]
                geo_bg['dist'] = geo_bg['geometry'].distance(proj.geometry)#distances from this proj to each cbgs
                geo_bg_impact = geo_bg[geo_bg['dist']<=impact_radius[proj.Impact]]#select impacted cbgs
                index_sum = (geo_bg_impact.TotalPopu * geo_bg_impact.area/((geo_bg_impact.dist+1)**0.5)).sum()#the sum of weight index
                geo_bg_impact.loc[:,'invest_index'] = (geo_bg_impact.loc[:,'TotalPopu'] * geo_bg_impact.loc[:,'area'] / ((geo_bg_impact.loc[:,'dist']+1)**0.5))/index_sum
                #get the index of rows
                year_type_index = geo_bg_invest[(geo_bg_invest.GEOID.isin(geo_bg_impact.GEOID))&(geo_bg_invest.year==year)].index
                geo_bg_impact.index = geo_bg_invest.loc[year_type_index,proj_type].index
                geo_bg_invest.loc[year_type_index,proj_type] += geo_bg_impact.invest_index * float(proj.FundingSF)
                geo_bg_invest = geo_bg_invest.fillna(0) 
        except:
            print('e')


# In[43]:


geo_bg_invest_point = geo_bg_invest.copy()
geo_bg_invest_point.to_file('data/invest_index/geo_bg_invest_point.geojson', driver='GeoJSON')


# ## Investment Index for Polygon Project

# In[50]:


sf_polygon_gdf_impact = sf_polygon_gdf_merge.merge(addinfo_merge,how='left',left_on='proj_id',right_on='proj_id')


# In[6]:


#sf_polygon_gdf_impact.to_file('data/invest_index/sf_polygon_gdf_impact.geojson', driver='GeoJSON')
sf_polygon_gdf_impact = gpd.read_file('data/invest_index/sf_polygon_gdf_impact.geojson')


# In[55]:


geo_bg = sf_bg_geo.copy()
geo_bg_invest[list(addinfo.Type.unique())] = 0
impact_radius = {'isolated':10,'neighbor':10,'regional':10,'citywide':10}


# In[57]:


for year,proj_type in itertools.product(year,proj_type):
#for year,proj_type in itertools.product(sf_polygon_gdf_impact.ReportingCycleName.unique(),sf_polygon_gdf_impact.Type.unique()):
    #select projects in particular year and type
    sf_polygon_gdf_impact_selection = sf_polygon_gdf_impact[(sf_polygon_gdf_impact.ReportingCycleName==year)&(sf_polygon_gdf_impact.Type==proj_type)]
    if len(sf_polygon_gdf_impact_selection) == 0:
        None
    else:
        try:
            for i in range(len(sf_polygon_gdf_impact_selection)):
                sf_polygon_gdf_impact_selection = sf_polygon_gdf_impact[(sf_polygon_gdf_impact.ReportingCycleName==year)&(sf_polygon_gdf_impact.Type==proj_type)]
                overlap = gpd.overlay(geo_bg,sf_polygon_gdf_impact_selection.iloc[i:i+1],how='intersection')
                overlap['overlap_area'] = overlap.area

                a = overlap.groupby('GEOID').sum('overlap_area')[
                    overlap.groupby('GEOID').sum('overlap_area')['overlap_area'] > overlap.groupby('GEOID').sum('overlap_area')['area'].min()]

                geo_bg_incbg = geo_bg[geo_bg.GEOID.isin(list(a.index))]

                fund = sf_polygon_gdf_impact_selection.iloc[i:i+1].FundingSF.iloc[0]
                geo_bg_incbg[proj_type] = fund * geo_bg_incbg['TotalPopu'] / (geo_bg_incbg['TotalPopu'].sum())
                geo_bg_incbg = geo_bg_incbg[['GEOID'] + [proj_type]]


                year_type_index = geo_bg_invest[(geo_bg_invest.GEOID.isin(geo_bg_incbg.GEOID))&(geo_bg_invest.year==year)].index
                geo_bg_incbg.index = geo_bg_invest.loc[year_type_index,proj_type].index
                geo_bg_invest.loc[year_type_index,proj_type] += geo_bg_incbg.loc[:,proj_type]
                geo_bg_invest = geo_bg_invest.fillna(0) 
        except:
            print('end')


# In[59]:


geo_bg_invest.to_csv('data/invest_index/polygon/vehicle2020.csv')

