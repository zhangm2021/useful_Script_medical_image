#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 22:18:01 2024

@author: zhangm
"""
import nibabel as nib
from matplotlib import pyplot as plt
import numpy as np

def save_fig(data,aspect=1,save_name=None,vmin=-0.1,vmax=0.1):
    fig = plt.figure()
    if vmin==None and vmax==None:
        plt.imshow(data,cmap='gray',aspect=aspect) #auto
    else:
        plt.imshow(data,cmap='gray',aspect=aspect,vmin=vmin,vmax=vmax)

    plt.axis('off')
    ax = plt.gca()
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
    
    fig.savefig(fname=save_name, 
                format='tiff', 
                dpi=1000, 
                bbox_inches='tight', pad_inches=-0.1)


if __name__ == "__main__":
    d1 = nib.load('COSMOS.nii') #resolution=1x1x2 mm^3
    d1 = d1.get_fdata()
    data1 = np.rot90(d1[105,9:-9,4:56],1)
    data1 = data1[:,::-1] #resolution=1x2 mm^2
    scale_factor = 2
    save_name = 'ax_view.tiff'

    save_fig(data1,aspect=scale_factor,save_name=save_name,vmin=-0.1,vmax=0.1)
