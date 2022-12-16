#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:29:58 2022

@author: Gaurav Arora, Ph.D   Email: gauravarora.1100@gmail.com
"""
"""
This code takes POSCAR file as input and converts it to cfg format to be read my MLIP code. Please make 
sure to input POSCAR with cartesian coordinates. Use ovito to convert direct to cartesian coordiantes.
"""

def read_POSCAR_make_cfg(filename):
    import numpy as np
    #Reading POSCAR file
    file = open(str(filename), 'r')
    
    #reading each line of the POSCAR file
    system_info = file.readline()
    _ = file.readline()
    #reading and storing box dimensions
    x_dims = file.readline().strip().split()
    y_dims = file.readline().strip().split()
    z_dims = file.readline().strip().split()
    types = file.readline().strip().split()
    types_of_atoms = len(types)
    num_of_atoms = file.readline().strip().split()
    
    #Extracting number of atoms of each type and also the total number of atoms
    num_of_atoms_for_each_element = []
    for i in range (0,len(num_of_atoms)):
        _ = int(num_of_atoms[i])
        num_of_atoms_for_each_element.append(_)
    total_num_of_atoms = sum(num_of_atoms_for_each_element)
    
    _ = file.readline()
    
    #reading and storing coordinates of the atoms
    x_coordinates, y_coordinates, z_coordinates = [], [], []
    for i in range (0,total_num_of_atoms):
        _ = file.readline().strip().split()
        x_coordinates.append(float(_[0]))
        y_coordinates.append(float(_[1]))
        z_coordinates.append(float(_[2]))
        
    file.close()
    
    #Assigning the type depending upon the number of atoms of each type in the POSCAR file
    #Making list of elements
    list_of_elements = []
    for i in range (0,types_of_atoms):
        #print(type(num_of_atoms_for_each_element[i]))
        _ = [types[i]] * num_of_atoms_for_each_element[i]
        _ = np.asarray(_)
        list_of_elements.append(_)
    list_of_elements = np.concatenate(list_of_elements)
    
    #assigning elements unique identity
    elements_name = ['Ni', 'Cu', 'Cr', 'Co', 'Sc', 'V', 'Fe', 'Pd']
    ids = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    dict_of_elements = dict(zip(elements_name, ids))
    
    #Writing cfg file
    f = open('output-' + str(filename) + '.cfg', 'w')
    f.writelines('BEGIN_CFG \n')
    f.writelines(' Size \n')
    f.writelines('  '+ str(total_num_of_atoms) + '\n')
    f.writelines(' Supercell \n')
    
    #Writing box dimensions read earlier
    f.writelines('         ' + str(float(x_dims[0])) + ' ' + str(float(x_dims[1])) 
                 + ' ' + str(float(x_dims[2])) + '\n')
    f.writelines('         ' + str(float(y_dims[0])) + ' ' + str(float(y_dims[1])) 
                 + ' ' + str(float(y_dims[2])) + '\n')
    f.writelines('         ' + str(float(z_dims[0])) + ' ' + str(float(z_dims[1])) 
                 + ' ' + str(float(z_dims[2])) + '\n')
    
    f.writelines(' AtomData:  id type       cartes_x      cartes_y      cartes_z \n')

    #Writing coordinates of each atoms read earlier in proper format
    for j in range (0,total_num_of_atoms):
        f.writelines('             ' + str(j+1) + '    ' + str(int(dict_of_elements[list_of_elements[j]]))
        + '       ' + str(x_coordinates[j]) + '      ' + str(y_coordinates[j])
                     + '      ' + str(z_coordinates[j]) + '\n')
            

    f.writelines(' Feature   EFS_by   VASP \n')
    f.writelines('END_CFG \n')
    f.writelines('\n')
    f.close()
    return(f, dict_of_elements)

num_of_files = int(input("Enter the number of POSCAR files: "))
filename_ = str(input("Enter the generic filename for POSCAR (excluding the number extension): "))


filenames = []
for i in range (0,num_of_files):
    output, dicti =  read_POSCAR_make_cfg(filename_ + str(i))
    filename = str(output)[25:-28] #extracting the name of the file
    filenames.append(filename)
    
from os import system
system('rm ' 'final.cfg') #remove final.cfg while if present
for i in range(0,num_of_files):
    system("cat " + str(filenames[i]) + ">> final.cfg" )
    










    

    

