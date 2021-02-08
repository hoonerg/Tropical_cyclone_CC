#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import numpy.ma as ma
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import scipy as sp
import netCDF4 as nc
from netCDF4 import Dataset
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy
import iris
import xarray
import iris.quickplot as qplt
import iris.plot as iplt
import iris.coord_categorisation
import cartopy.feature as cfeature
import time
import statsmodels.api as sm
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker


# In[44]:


filename = 'IBTrACS.WP.v04r00.nc'
cubes = iris.load(filename)
cubes_con = iris.load(filename, ['season', 'wmo_pres', 'iso_time'])


# In[37]:


print(cubes)


# In[41]:


print(cubes_con)


# In[21]:


ncfile = Dataset('IBTrACS.WP.v04r00.nc')


# In[22]:


print(list(ncfile.variables))


# In[23]:


print(ncfile.variables)


# In[24]:


time = ncfile.variables['time']
year = ncfile.variables['season']
pres = ncfile.variables['wmo_pres']
lat = ncfile.variables['lat']
lon = ncfile.variables['lon']
#hgt = ncfile.variables['height']
#tas = ncfile.variables['tas']
#lat <- list.reverse(lat)
#lat = flipud(rot180(lat))


# In[25]:


plt.plot(year, pres)
plt.show()

