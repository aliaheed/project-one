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


