# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:43:55 2019

@author: hnambur
"""

## import required packages
from pathlib import Path
import os
from scipy import stats
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#Uncomment the line below to get xkcd style plots
#plt.xkcd() 

# Learn more about using Path (recommended)
# https://pbpython.com/pathlib-intro.html

data_file = Path(r"sample_data.csv")
data_frame = pd.read_csv(data_file)

# create two data frames that separates out males and females
males_df = data_frame[data_frame.Gender=='Male']

#TODO: create data_frame that contains only females
females_df = 
#create a figure with three plots
fig, ax = plt.subplots(1,3)
ax = ax.flatten() # always add this so that the ax will have shape (1*2,)
                  # and can be easily iterated
# plot the height vs weight for males and females on the first axis
# you can use numpy arrays/series/lists of same size as the first and second
# arguments
ax[0].plot(males_df['Height'],males_df['Weight'],'ro',label="Males")
#TODO: plot the data for females

#label the x and y axis
ax[0].set_xlabel("Height")
ax[0].set_ylabel("Weight")
# diaply the legend
ax0_lg = ax[0].legend(loc="upper left")
ax0_lg.draggable(True)
# plot heights distribution on second axis
data_frame.groupby("Gender").Height.plot(kind='hist',ax=ax[1])
ax[1].set_xlabel("Height")
ax[1].set_ylabel("distribution")
ax0_lg = ax[1].legend(loc="upper left")
ax0_lg.draggable(True)
#TODO: plot weights distribution on third axis

# plot the box/whisker plots
fig2,ax2 = plt.subplots(1,1)
data_frame.groupby("Gender").boxplot(ax=ax2)

# plot Q-Q plot
fig3,ax3 = plt.subplots(2,2)
ax3=ax3.flatten()
# Picking the data
data_pick = ["Male"]*2 + ["Female"]*2
feature_pick = ["Height","Weight"]*2 

for i,ax3_i in enumerate(ax3):
    stats.probplot(data_frame[data_frame.Gender==data_pick[i]][feature_pick[i]],plot=ax3_i)

#show the plot
plt.show()

