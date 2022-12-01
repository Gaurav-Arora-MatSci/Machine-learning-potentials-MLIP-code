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
    #Reading POSCAR file
    file = open(str(filename), 'r')
    
    #readin each line of the POSCAR file
    system_info = file.readline()
    _ = file.readline()
    #reading and storing box dimensions
    x_dims = file.readline().strip().split()
    y_dims = file.readline().strip().split()
    z_dims = file.readline().strip().split()
    types = file.readline().strip().split()
    types_of_atoms = len(types)
    num_of_atoms = int(file.readline().strip().split()[0])
    _ = file.readline()
    
    #reading and storing coordinates of the atoms
    x_coordinates, y_coordinates, z_coordinates = [], [], []
    for i in range (0,num_of_atoms):
        _ = file.readline().strip().split()
        x_coordinates.append(float(_[0]))
        y_coordinates.append(float(_[1]))
        z_coordinates.append(float(_[2]))
        
    file.close()
    
    #Writing cfg file
    f = open('output-' + str(filename) + '.cfg', 'w')
    f.writelines('BEGIN_CFG \n')
    f.writelines(' Size \n')
    f.writelines('  '+ str(num_of_atoms) + '\n')
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
    if types_of_atoms == 1: #When type of atoms is one
        for j in range (0,num_of_atoms):
            f.writelines('             ' + str(j+1) + '    0' + '       ' + 
                         str(x_coordinates[j]) + '      ' + str(y_coordinates[j])
                         + '      ' + str(z_coordinates[j]) + '\n')
            
    f.writelines(' Feature   EFS_by   VASP \n')
    f.writelines('END_CFG \n')
    f.writelines('\n')
    f.close()
    return(f)

num_of_files = int(input("Enter the number of POSCAR files: "))
filename_ = str(input("Enter the generic filename for POSCAR (excluding the number extension): "))

filenames = []
for i in range (0,num_of_files):
    output =  read_POSCAR_make_cfg(filename_ + str(i))
    #filename = str(output)[25:43]
    filename = str(output)[25:-28]
    filenames.append(filename)
    
from os import system
for i in range(0,num_of_files):
    system("cat " + str(filenames[i]) + ">> final.cfg" )
    










    

    

