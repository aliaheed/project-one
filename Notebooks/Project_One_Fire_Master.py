#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Notebooks'))
	print(os.getcwd())
except:
	pass

#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sqlite3
import gmaps
from config import (gkey)


#%%
# conn = sqlite3.connect('./FPA_FOD_20170508.sqlite')

# c = conn.cursor()

# data = c.execute('Select * from Fires;')
# master_df = pd.DataFrame(data.fetchall())
# master_df.head()


#%%
# master_header_df = master_df.rename(columns={
#     0:"OBJECTID", 
#     1:"FOD_ID", 
#     2:"FPA_ID", 
#     3:"SOURCE_SYSTEM_TYPE", 
#     4:"SOURCE_SYSTEM", 
#     5:"NWCG_REPORTING_AGENCY", 
#     6:"NWCG_REPORTING_UNIT_ID",  
#     7:"NWCG_REPORTING_UNIT_NAME",  
#     8:"SOURCE_REPORTING_UNIT", 
#     9:"SOURCE_REPORTING_UNIT_NAME", 
#     10:"LOCAL_FIRE_REPORT_ID", 
#     11:"LOCAL_INCIDENT_ID",  
#     12:"FIRE_CODE",  
#     13:"FIRE_NAME", 
#     14:"ICS_209_INCIDENT_NUMBER", 
#     15:"ICS_209_NAME", 
#     16:"MTBS_ID",  
#     17:"MTBS_FIRE_NAME",  
#     18:"COMPLEX_NAME", 
#     19:"FIRE_YEAR",  
#     20:"DISCOVERY_DATE", 
#     21:"DISCOVERY_DOY",  
#     22:"DISCOVERY_TIME", 
#     23:"STAT_CAUSE_CODE", 
#     24:"STAT_CAUSE_DESCR",  
#     25:"CONT_DATE", 
#     26:"CONT_DOY",  
#     27:"CONT_TIME", 
#     28:"FIRE_SIZE", 
#     29:"FIRE_SIZE_CLASS", 
#     30:"LATITUDE", 
#     31:"LONGITUDE", 
#     32:"OWNER_DESCROWNER_CODE", 
#     33:"OWNER_DESCR", 
#     34:"STATE",  
#     35:"COUNTY",  
#     36:"FIPS_CODE", 
#     37:"FIPS_NAME", 
#     38:"Shape",
# })
# master_header_df.head()


#%%
# group_main_df = master_header_df[["FOD_ID", "FIRE_NAME", "FIRE_YEAR", "DISCOVERY_DATE", "DISCOVERY_DOY", "DISCOVERY_TIME", 
#                                "STAT_CAUSE_CODE", "STAT_CAUSE_DESCR", "FIRE_SIZE", "FIRE_SIZE_CLASS", 
#                                 "LATITUDE", "LONGITUDE", "STATE", "COUNTY"]]


#%%
# size_over_one = group_main_df.loc[group_main_df["FIRE_SIZE"]>1,:]


#%%
# Created Main database for group to start using.  THIS DATABASE INCLUDES AK, PR, HI
# ===============================================================
# size_over_one.to_csv("Fire_Data_Over_1.csv")


#%%
file = "Fire_Data_Over_1.csv"
df = pd.read_csv(file)


#%%
us_df = df.loc[(df.loc[:,'STATE']!='AK') & (df.loc[:,'STATE']!='HI') & (df.loc[:,'STATE']!='PR')]


#%%
lat_max = us_df["LATITUDE"].max()
lat_min = us_df["LATITUDE"].min()
lat_interval = (lat_max - lat_min)/3

lon_max = us_df["LONGITUDE"].max()
lon_min = us_df["LONGITUDE"].min()
lon_interval = (lon_max - lon_min)/3


lat_bin = [lat_min, (lat_min + lat_interval), (lat_min + 2*lat_interval), lat_max]
lon_bin = [lon_min, (lon_min + lon_interval), (lon_min + 2*lon_interval), lon_max]

lon_name = ["West", "Central", "East"]
lat_name = ["South", "Central", "North"]


#%%
us_df["LON_REGION"] = pd.cut(us_df["LONGITUDE"], lon_bin, labels=lon_name)


#%%
us_df["LAT_REGION"] = pd.cut(us_df["LATITUDE"], lat_bin, labels=lat_name)
us_df.head()


#%%
lat_df = us_df.groupby("LAT_REGION")
lat_list_bar = lat_df.FOD_ID.count()

lat_list_bar.plot(kind="barh", facecolor="red", align="edge")
plt.title("Wildfires by Lattitude")
plt.xlabel("Number of Fires")
plt.ylabel("Latitude Region")
plt.grid()
plt.savefig("Wildfires_By_Latitude.png", bbox_inches="tight")
plt.show()


#%%
lon_df = us_df.groupby("LON_REGION")
lon_list_bar = lon_df.FOD_ID.count()
lon_list_bar.plot(kind="bar", facecolor="blue", align="edge")
plt.title("Wildfires by Longitude")
plt.xlabel("Number of Fires")
plt.ylabel("Longitude Region")
plt.grid()
plt.xticks(rotation=45)
plt.savefig("Wildfires_By_Longitude.png", bbox_inches="tight")
plt.show()


#%%
plt.scatter(us_df["LONGITUDE"], us_df["FIRE_SIZE"], marker="o", facecolors="red", edgecolors="black")
plt.title("Longitude Vs. Wildfire Size")
plt.xlabel("Longitude")
plt.ylabel("Fire Size (Acres)")
plt.grid()
plt.savefig("Longitude_Vs_Wildfire_Size.png", bbox_inches="tight")
plt.show()


#%%



#%%
# Configure gmaps with API key
gmaps.configure(api_key=gkey)
# Store 'Lat' and 'Lng' into  locations 
locations = us_df[["LATITUDE", "LONGITUDE"]].astype(float)

# Convert Poverty Rate to float and store
# HINT: be sure to handle NaN values
fire_size = us_df["FIRE_SIZE"].astype(float)


#%%
fig = gmaps.figure()

heat_layer = gmaps.heatmap_layer(locations, weights=fire_size, 
                                 dissipating=False, max_intensity=558198,
                                 point_radius = 1)

# Adjust heat_layer setting to help with heatmap dissipating on zoom
heat_layer.dissipating = False
heat_layer.max_intensity = 558198
heat_layer.point_radius = 1

fig.add_layer(heat_layer)

fig


#%%
larger = us_df.loc[us_df["FIRE_SIZE"]>10000,:]
larger
plt.scatter(larger["LONGITUDE"], larger["FIRE_SIZE"], marker="o", facecolors="red", edgecolors="black")
plt.title("Longitude Vs. Wildfires > 10,000 Acres")
plt.xlabel("Longitude")
plt.ylabel("Fire Size (Acres)")
plt.grid()
plt.savefig("Lng_vs_fire_gtrtenk.png", bbox_inches="tight")
plt.show()


#%%
lon_df = larger.groupby("LON_REGION")
lon_list_bar = lon_df.FOD_ID.count()
lon_list_bar.plot(kind="bar", facecolor="blue", align="edge")
plt.title("Wildfires > 10,000 Acres by Longitude")
plt.xlabel("Number of Fires")
plt.ylabel("Longitude Region")
plt.grid()
plt.xticks(rotation=45)
plt.savefig("Fire_grt_tenK_vs_lon.png", bbox_inches="tight", pad_inches=0.5)
plt.show()


#%%
lat_df = larger.groupby("LAT_REGION")
lat_list_bar = lat_df.FOD_ID.count()

lat_list_bar.plot(kind="barh", facecolor="red", align="edge")
plt.title("Wildfires > 10,000 Acres by Lattitude")
plt.xlabel("Number of Fires")
plt.ylabel("Latitude Region")
plt.grid()
plt.savefig("Fire_grt_tenK_vs_lat.png", bbox_inches="tight")
plt.show()


#%%
means = years["FIRE_SIZE"].mean()
standard_errors = years["FIRE_SIZE"].sem()


fig, ax = plt.subplots()
x_axis = size_year.index
ax.errorbar(x_axis, means, standard_errors, fmt="o", color="red")


plt.title("Wildfire Size By Year")
plt.xlabel("Year")
plt.ylabel("Average Size of Fire")
plt.grid()
plt.savefig("Wildfire_Size_By_Year.png", bbox_inches="tight")


plt.show()


