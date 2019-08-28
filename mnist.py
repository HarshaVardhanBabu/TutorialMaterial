# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:47:23 2019

@author: hnambur
"""
from matplotlib import pyplot as plt 
from sklearn.datasets import load_digits

# load the digits data set set
digits = load_digits()

# data is available in data member and labels are available in targets member
data = digits.data
targets = digits.target
# TODO: print the shape of data and targets


# change the plot to false if you donot want to see the sample data
plot = True
if(plot):
    fig, ax = plt.subplots(3,3)# Create plots in a grid of 3 rows and 3 cols
    ax = ax.flatten()
#Tip: enumerate will help you iterate through an array along with the index
    for i,ax in enumerate(ax):
# TODO: reshape the data to 8X8 and assign to reshape_data variable
        reshape_data = 
        ax.imshow(reshape_data)
        ax.set_title(targets[i])
        ax.axis('off')
    plt.show()




