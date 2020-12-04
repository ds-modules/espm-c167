"""
This script is written to create a widget for use in notebook 2.
"""

import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
from datascience import *
from matplotlib.colors import ListedColormap
import re
# Helps the maps display nicely in the notebook:
plt.rcParams['figure.figsize'] = [30, 20]
# Tells the notebook not to display warnings:
import warnings
warnings.filterwarnings('ignore')
from IPython.display import IFrame
from matplotlib import cm
import contextily as ctx
###


# Create a ListedColormap object called holc_cmap, pass in the list of colors
from matplotlib.colors import ListedColormap
GrBlYlRd = ListedColormap(['green', 'blue', 'yellow', 'red'])

# Import data and convert to a specific map projection
holc_5072_original = gpd.read_file('holc_ca_epsg5072_treecov')
holc_5072 = holc_5072_original.to_crs(epsg=3857)



inp = widgets.Dropdown(
    options=['Los Angeles', 'Fresno', "San Francisco", "San Jose", "Stockton", "San Diego", 'Oakland'],
    value='Oakland',
    description='City:',
    disabled=False)

def f(inp):
    if inp != "Oakland":
        city_tree = holc_5072[holc_5072['area']== inp]

    else:
        oakland_area = ['Alameda', 'Albany', 'Berkeley', 'Emeryville', 'Oakand', 'Oakland','Piedmont', 'San']
        city_tree = holc_5072[holc_5072['area'].isin(oakland_area)]
    
    fig = plt.figure(figsize=[25,20]);
    ax1=plt.subplot(2, 2, 1);
    ax2=plt.subplot(2, 2, 2);
    
    base_1 = city_tree.plot(ax = ax1, column="holc_grade", alpha=0.4, cmap = GrBlYlRd, legend=True);
    ax1.set_title("HOLC Areas", size = "x-large");
    ax1.get_xaxis().set_visible(False);
    ax1.get_yaxis().set_visible(False);

    base_2 = city_tree.plot(ax = ax2, column="_mean", alpha=0.6, cmap = cm.get_cmap('Greens'), legend=True);
    ax2.set_title("Tree Canopy Average Coverage Per Area", size = "x-large");
    ax2.get_xaxis().set_visible(False);
    ax2.get_yaxis().set_visible(False);      
    
    ctx.add_basemap(base_1, url=ctx.providers.Stamen.TonerLite)
    ctx.add_basemap(base_2, url=ctx.providers.Stamen.TonerLite)
        
#     plt.subplots_adjust(left = 0.3, wspace = 0.06);

    
out = widgets.interactive_output(f, {'inp': inp})


