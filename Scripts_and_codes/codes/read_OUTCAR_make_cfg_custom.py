#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:19:45 2022

@author: Gaurav Arora, Ph.D Email: gauravarora.1100@gmail.com

This code takes OUTCAR file as input and converts it to a cfg file to be read by
MLIP code. Default command for converting OUTCAR to cfg file cannot be used as it 
does not recognizes the different elements used. This code only reads the last configuration.
Please mind with the name of potentials used, it could be different than actual element name. For
example Y can be Y_sv.
"""

def read_OUTCAR_make_cfg_last_config(filename):
    import linecache
    import numpy as np
    file = open(str(filename), 'r')
    
    #Storing indexes of line for different information
    ################################################
    
    num_of_atoms_index = []
    
    for index, line in enumerate(file):
        if "ions per type" in line:#used for extracting total types and number of atoms
            num_of_atoms_index.append(index + 1)
            
    # Number of atoms and number of atoms of each type
    num_of_atoms_line = linecache.getline(str(filename), num_of_atoms_index[0]).strip().split()
    num_of_atoms_array_str = num_of_atoms_line[4:]
    num_of_types_of_atoms = len(num_of_atoms_array_str)
    num_of_atoms_for_each_element = []
    
    for i in range(num_of_types_of_atoms):
        _ = int(num_of_atoms_array_str[i])
        num_of_atoms_for_each_element.append(_)
    total_num_of_atoms = sum(num_of_atoms_for_each_element)
    file.close()
    
    ################################################
    
    file = open(str(filename), 'r')
    #Types of atoms
    types_of_atoms_index = []
    
    for index, line in enumerate(file):  
        if "INCAR" in line:#used for extrating types of atoms
            for j in range(num_of_types_of_atoms):#extarct indexes based on number of types of atoms
                _  = index + 2 + j
                types_of_atoms_index.append(_)
                
    types_of_atoms = []          
    for j, k in enumerate(types_of_atoms_index):
        _ = linecache.getline(str(filename), types_of_atoms_index[j]).strip().split()
        __ = _[2]
        types_of_atoms.append(__)
    file.close()
    
    ################################################
    
    file = open(str(filename), 'r')
    #Extratcing x,y,z,fx,fy,fz from last step in OUTCAR
    coor_force_index = []
    
    for index, line in enumerate(file):
        if "TOTAL-FORCE" in line: #used for extarcting and forces
            _ = index + 3
            coor_force_index.append(_)
    
    #For last configuration
    coor_force_index = coor_force_index[-1]
    
    x_coor, y_coor, z_coor, f_x, f_y, f_z = [], [], [], [], [], []
    for k in range(total_num_of_atoms):
        _ = linecache.getline(str(filename), coor_force_index + k).strip().split()
        x, y, z, fx, fy, fz = float(_[0]), float(_[1]), float(_[2]), float(_[3]),\
            float(_[4]),float(_[5])
        x_coor.append(x)
        y_coor.append(y)
        z_coor.append(z)
        f_x.append(fx)
        f_y.append(fy)
        f_z.append(fz)
    file.close()
    ################################################   
    
    #Assigning the type depending upon the number of atoms of each type in the OUTCAR file
    #Making list of elements
    list_of_elements = []
    for i in range (len(types_of_atoms)):
            #print(type(num_of_atoms_for_each_element[i]))
            _ = [types_of_atoms[i]] * num_of_atoms_for_each_element[i]
            _ = np.asarray(_)
            list_of_elements.append(_)
    list_of_elements = np.concatenate(list_of_elements)
    
    #assigning elements unique identity
    elements_name = ['Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu',\
    'Zn', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', \
    'Hf', 'Ta', 'W', 'Os', 'Ir', 'Pt', 'Au', 'Hg',\
    'Al']
    ids = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',\
    '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',\
    '20', '21', '22', '23', '24', '25', '26', '27', \
    '28'] #Unique ids, change this according to the system you will be working on
    dict_of_elements = dict(zip(elements_name, ids))
    
    ################################################
    
    #Extracting energy from the system
    file = open(str(filename), 'r')
    
    energy_index = []
    for index, line in enumerate (file):
        if "energy(sigma" in line:
            energy_index.append(index + 1)
            
    #for last config energy
    energy_index = energy_index[-1]
    
    energy = float(linecache.getline(str(filename), energy_index).strip().split()[-1])
    file.close()
        
    ####################################################
    
    #Extracting Plusstresses
    file = open(str(filename), 'r')
    
    plusstress_index = []
    for index, line in enumerate(file):
        if 'Total' in line:
            _ = index + 1
            plusstress_index.append(_)
    
    #Extracting for last config (-2 index is used bcoz last index corresponds to time of simulation)
    plusstress_index = plusstress_index[-2]
    
    plusstress = linecache.getline(str(filename), plusstress_index).strip().split()
    plusstress_xx, plusstress_yy, plusstress_zz, plusstress_yz, plusstress_xz, plusstress_xy = \
        plusstress[1], plusstress[2], plusstress[3], plusstress[4], plusstress[5], plusstress[6]
    
    file.close()
    ######################################################
    #Extracting final box size
    file = open(str(filename), 'r')
    
    box_size_index = []
    
    for index, line in enumerate(file):
        if 'BASIS-vectors' in line:
            _ = index + 6
            box_size_index.append(_)
    
    #Extracting box size for last config
    box_size_index = box_size_index[-1]
    
    box_size = []
    for i in range(3):
        _ = linecache.getline(str(filename), box_size_index + i).strip().split()
        box_size.append(_)
    
    file.close()
    #######################################################
    
    ##Writing the cfg file
    f = open('output-' + str(filename) + '.cfg', 'w')
    f.writelines('BEGIN_CFG \n')
    f.writelines(' Size \n')
    f.writelines('  '+ str(total_num_of_atoms) + '\n')
    f.writelines(' Supercell \n')
    
    #Writing box dimensions read earlier
    f.writelines('         ' + str(float(box_size[0][0])) + ' ' + str(float(box_size[0][1])) 
                 + ' ' + str(float(box_size[0][2])) + '\n')
    f.writelines('         ' + str(float(box_size[1][0])) + ' ' + str(float(box_size[1][1])) 
                 + ' ' + str(float(box_size[1][2])) + '\n')
    f.writelines('         ' + str(float(box_size[2][0])) + ' ' + str(float(box_size[2][1])) 
                 + ' ' + str(float(box_size[2][2])) + '\n')
    f.writelines(' AtomData:  id type       cartes_x      cartes_y      cartes_z     fx    fy    fz\n')
        #Writing coordinates of each atoms read earlier in proper format
    for j in range (0,total_num_of_atoms):
        f.writelines('             ' + str(j+1) + '    ' + str(int(dict_of_elements[list_of_elements[j]]))
        + '       ' + str(x_coor[j]) + '      ' + str(y_coor[j]) + '      ' + str(z_coor[j]) + 
        '   ' + str(f_x[j]) + '   ' + str(f_y[j]) + '    ' + str(f_z[j]) + '\n')
    
    f.writelines('Energy \n')
    f.writelines(str(energy) + '\n')
    f.writelines(' PlusStress: xx yy zz yz xz xy \n')
    f.writelines(str(plusstress_xx) + ' ' + str(plusstress_yy) + ' ' + str(plusstress_zz) + ' ' + \
                 str(plusstress_yz) + ' ' + str(plusstress_xz) + ' ' + str(plusstress_xy) + '\n')
    f.writelines(' Feature   EFS_by   VASP \n')
    f.writelines('END_CFG \n')
    f.writelines('\n')
    f.close()
    return(f, dict_of_elements)

num_of_files = int(input("Enter the number of OUTCAR files: "))
filename_ = str(input("Enter the generic filename for OUTCAR (excluding the number extension): "))


filenames = []
for i in range (0,num_of_files):
    output, dicti =  read_OUTCAR_make_cfg_last_config(filename_ + str(i))
    filename = str(output)[25:-28] #extracting the name of the file
    filenames.append(filename)
    
from os import system
system('rm ' 'final.cfg') #remove final.cfg while if present
for i in range(0,num_of_files):
    system("cat " + str(filenames[i]) + ">> final.cfg" )
system('rm' 'output-OUTCAR-*')
