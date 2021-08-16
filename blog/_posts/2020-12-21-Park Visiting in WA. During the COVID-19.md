---
layout: post
title: "Park Visiting Patterns in WA. During the COVID-19 Pandemic"
author: "Haoyu"
tags: [COVID-19,travel pattern,Washington State]

---



At the beginning of 2020, COVID-19 began to become pandemic all over the world. Governments proposed shelter in place orders to restrict social distance and the use of public space to prevent the spread of the virus. CDC proposed that during the pandemic urban green space, such as parks, are important to the mental and physical health of citizens. Although the orders restrict all people, such restrictions will have a severe impact on some socio-economic disadvantaged groups. So, I would like to explore the relationships between the distance of park visiting and socio-economic status before and during the pandemic. ArcMap, ArcCatalog, Excel, and R will be used. 

## Data Description                             

* [**ALPACA Census Block Group (2018)**](https://geo.wa.gov/datasets/WSDOT::wsdot-alpaca-census-block-group-2018?geometry=-126.311%2C46.611%2C-118.609%2C47.916) (2020/2/19)

US Census 5-year American Community Survey, from Washington State Geospatial Data Portal, including much socio-economic information in Washington State by block group level. 

* [**Street Address**](https://gis-kingcounty.opendata.arcgis.com/datasets/street-address-st-address-line) (2020/10/21) 

All streets in King County, from King County Open GIS Data, including the mid-points of street parcels, the types of streets, etc. 

* [**King County Political Boundary**](https://gis-kingcounty.opendata.arcgis.com/datasets/king-county-political-boundary-no-waterbodies-kingco-area) (2018/12/4)

The boundary of King County, from King County Open GIS Data.

* [**Park visitors and Blocks**](https://www.safegraph.com/weekly-foot-traffic-patterns) (2020/6)

The foot traffic counts for parks in King County, from SafeGraph, including park visiting counts recorded by census block groups in the last weeks of April 2019/2020. (Visitor_count = 4 means in this week, the number of visitors is less than 5.)

## Methods and Process                     

### Data Preparation

#### (1)  King County Only

Use **Selection by Location** to select the King County data from *Census Block Group* by *the boundary of King County*. Use **Excel** to select the park data within King County from *Park visitors and Blocks*. 

#### (2)  Preparation for Next Step

Use **Excel** to reorganize the data and make two versions, one is for R and regression, including all information, named *KC_2020_All**, KC_2019_All* respectively. Another is for ArcMap, only including the XYs of Parks and Census Block Groups, named *KC_2020, KC_2019* respectively.

#### (3)  Import Data

**Import** *Street Address* named *KC_Streets*, Census Block Group (2018) named *KC_Census*. **Import** *KC_2020*, and *KC_2019*. By the way, **import** above all into a geodatabase called *OD.gdb*, Meanwhile, remove other useless data from ArcMap. 

### Network Analysis

####  (4)  Network Dataset

**Create** a new File Geodatabase Feature Dataset called *Road_2020*, then move *KC_streets*, *KC_2020* into the *Road_2020*. **Create** a new Network Dataset called *Road_ND_2020* in ArcMap.

#### (5)  Routes Analysis

Active **Network Analyst** and then **Create Route** called *Routes_2020*. **Load location** *KC_2020* for *Stops* then click **Solve**.

![routes_analysis](routes_analysis.png)

#### (6)  Output

After the analysis, use **Spatial Join** to give *GEOID* to the result. Then use **Table To Excel** to output the results *Routes_2020_Output* as an Excel file.

### Regression

#### (7)  Vlookup

Use **Vlookup** in Excel to connect the *Routes_2020_Output* and *KC_2020_All.* Because the range of *Routes_2020_Output* is limited to King County, only 2610 pairs can be found. Then **Save as** *KC_2020_all.csv*.

#### (8)  Correlations and Multiple Regression in R

**Import** the *KC_2020_all.csv*. **Identify** and **remove** influential data points and NA values. **Calculate** the correlation coefficients and **build** the regression model (Distance ~ Percent of Non-White + Percent of Over 65 + Percent of Poverty).

### Visualization

#### (9) Park Visiting Pattern

Use **XY to Line** to make a figure for presenting the park visiting pattern this week. Data *KC_2020_All* will be used.

### Model Building

#### (10) Auto Get Distance

Since I need to redo the whole process for 2019, I would like to make a *model* that can be used to analyze the distance of park visiting with input specific data. However, because some functions cannot be found in *ArcToolBox*, I can only make a simple one to import the data and make some preparations.

#### (11) Redo All for 2019

Use the data in 2019/4 to redo the analysis and then compare the results before and during the pandemic. 

## Result         

### Visiting Pattern - 2019                         

![pattern_2019](pattern_2019.png)

### Visiting Pattern - 2020 

![pattern_2020](pattern_2020.png)

### Regression Results - 2019

|                          | **Est.** | **SD** | **Std. Error** | **T** | **P** |
| ------------------------ | ------------ | ---------------- | -------------- | ----------- | ----------- |
| **Percent of Non-White** | 560.5        | 0.047          | 360.6          | 1.554       | 0.1204      |
| **Percent of Over 65**   | -2944        | -0.103          | 806.1          | -3.652      | 0.0003   |
| **Percent of Poverty**   | -1576        | -0.084         | 576.6          | -2.734      | 0.0063    |

### Regression Results - 2020

|                           | **Est.** | **SD** | **Std. Error** | **T** | **P** |
| ------------------------- | ------------ | ---------------- | -------------- | ----------- | ----------- |
| **Percent  of Non-White** | -30.25       | -0.016         | 41.1          | -0.737     | 0.4615      |
| **Percent of Over 65**    | -391.3       | -0.086         | 89.9           | -4.352      | 1.4e-05     |
| **Percent of Poverty**    | -63.09       | -0.020         | 66.1          | -0.954     | 0.3398      |

## Discussion

By summarizing the data, we can know that the number of parks visiting decreases from 59070 to 19073 (-68%). At the same time, I also found that the more people over 65 years old in the community, the more likely they are to visit the park in a shorter distance during the COVID-9. However, the impact of percent of poverty and percent of non-white on Park selection is still unclear, and more research is needed.

In the lab, there are many problems in operation, which need to be corrected or improved in the future. There are a lot of cross-county or even cross-state visiting activities, but I do not handle them well. There are different levels and conditions of streets, which should be treated differently, but it may be more reasonable to use Google Maps to plan the route in the future. In the regression model, due to the data, I only select the percent of non-white, percent of over 65, percent of poverty as independent variables. We can add more such as the education level, Internet access. The whole lab does not make full use of the count data between each line (census block groups - parks), so I do not maximize the use of data.

The lab is an interesting try, not only using a lot of GIS functions but also self-taught other functions such as network analysis, combining regression analysis and R learned in URBDP 520 Quantitative Method. Although the result is not very perfect, and there are some imperfections in the process, but this is the meaning of the independent lab.

 
