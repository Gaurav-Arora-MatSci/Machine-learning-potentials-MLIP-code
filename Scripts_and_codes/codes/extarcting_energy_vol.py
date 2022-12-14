#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:26:15 2022

@author: Gaurav Arora, Ph.D Email:gauravarora.1100@gmail.com
"""

"""
This code reads the file of the cfg format (which is used to developing machine learning package using MTP)
and extract volume and energy per atom from the cfg file.
"""
def read_cfg_extract_EV(filename):
    
    import linecache
    import math
    import numpy as np
    
    #Storing index of lines for extracting box size
    index_of_line_start, index_of_line_end = [], []
    
    #Storing index of lines for extracting energy values
    energy_line_number = []

    #Storing index of lines for extracting number of ataoms for each configuration
    num_of_atoms_line_number = []

    
    #Opening the file for reading
    file = open(filename,'r')
    
    #Going through all the lines in a file to look for keywords
    for index, line in enumerate(file):
        if 'Supercell' in line:#Looking for 'Supercell' keyword
            index_of_line_start.append(index + 1) #Storing index for next line once keyword is found
            index_of_line_end.append(index + 3)
            
        if 'Energy' in line: #Searching for 'Energy' keyword
            energy_line_number.append(index + 1)

        if 'Size' in line: #Searching for 'Size' keyword
            num_of_atoms_line_number.append(index + 1)
     
    #Arrays for storing volume, energies, and num_of_atoms
    volumes, energies, num_of_atoms = [], [], []
    
    #Extracting box size information for the indexes stored earlier while looking for the keywords
    for i in range(len(index_of_line_start)):
        x_len = linecache.getline(filename, index_of_line_start[i] + 1).strip().split()
        y_len = linecache.getline(filename, index_of_line_start[i] + 2).strip().split()
        z_len = linecache.getline(filename, index_of_line_start[i] + 3).strip().split()
        
        xx, xy, xz = float(x_len[0]), float(x_len[1]), float(x_len[2])
        yx, yy, yz = float(y_len[0]), float(y_len[1]), float(y_len[2])
        zx, zy, zz = float(z_len[0]), float(z_len[1]), float(z_len[2])
        
        #Calculating volume
        volume = math.sqrt((xx**2 + xy**2 + xz**2) + (yx**2 + yy**2 + yz**2)
                           + (zx**2 + zy**2 + zz**2))
        volumes.append(volume)
        
        #Getting energies
        energy = linecache.getline(filename, energy_line_number[i] + 1)
        energies.append(float(energy))

        #Getting number of atoms
        num_of_atom = linecache.getline(filename, num_of_atoms_line_number[i] + 1)
        num_of_atoms.append(int(num_of_atom))

        #converting system total energy to energy per atom
        energies_per_atom = []
        for j in range(0,len(energies)):
            energy_per_atom = energies[j] / num_of_atoms[j]
            energies_per_atom.append(energy_per_atom)

    
    #Stacking volumes and energies and saving it to the text file
    data = np.vstack((volumes, energies_per_atom))
    data = data.transpose()
    np.savetxt('E-V_data-' + filename + '.txt', data)
    
    #plotting the EV graph
    import matplotlib.pyplot as plt
    plt.plot(volumes, energies_per_atom,'*--')
    plt.xlabel('Volume')
    plt.ylabel('Energy per atom')
    plt.savefig('E-V_curve-' + filename + '.pdf')
    return()
    
filename = str(input('Enter file name: '))
read_cfg_extract_EV(filename)    
        
        
        
        
        
        
                    
            
    
