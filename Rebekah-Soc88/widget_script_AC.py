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

###


from matplotlib.colors import ListedColormap
# Create a ListedColormap object called holc_cmap, pass in the list of colors
GrBlYlRd = ListedColormap(['green', 'blue', 'yellow', 'red'])

holc_5072 = gpd.read_file('holc_ca_epsg5072_treecov')



inp = widgets.Dropdown(
    options=['Los Angeles', 'Fresno', "San Francisco", "San Jose", "Stockton", "San Diego", 'Oakland'],
    value='Los Angeles',
    description='City:',
    disabled=False)

def f(inp):
    if inp != "Oakland":
        city_tree = holc_5072[holc_5072['area']== inp]

    else:
        oakland_area = ['Alameda', 'Albany', 'Berkeley', 'Emeryville', 'Oakand', 'Oakland','Piedmont', 'San']
        city_tree = holc_5072[holc_5072['area'].isin(oakland_area)]
        
    fig = plt.figure();
    ax1=plt.subplot(2, 2, 1);
    ax2=plt.subplot(2, 2, 2);
    
    city_tree.plot(ax = ax1, column="holc_grade",  cmap = GrBlYlRd, legend=True);
    ax1.set_title("HOLC Areas", size = "x-large");
    ax1.get_xaxis().set_visible(False);
    ax1.get_yaxis().set_visible(False);

    city_tree.plot(ax = ax2, column="_mean", cmap = cm.get_cmap('Greens'), legend=True);
    ax2.set_title("Tree Canopy Average Coverage Per Area", size = "x-large");
    ax2.get_xaxis().set_visible(False);
    ax2.get_yaxis().set_visible(False);      
        
    plt.subplots_adjust(left = 0.3, wspace = 0.06);

    
out = widgets.interactive_output(f, {'inp': inp})

