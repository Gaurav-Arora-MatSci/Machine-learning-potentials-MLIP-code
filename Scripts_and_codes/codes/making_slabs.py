#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 17:07:32 2022

@author: Gaurav Arora Email: gauravarora.1100@gmail.com
This code is used for making slabs from the POSCAR file. Input for this 
code include filename and miller index. Rest of the input can also be changed 
by modifying the code
"""

def make_slab():
    import pymatgen
    from pymatgen.io.vasp import Poscar
    from pymatgen.core.surface import SlabGenerator
    
    file = input(str('Enter filename of the POSCAR file: '))
    poscar = Poscar.from_file(str(file))
    structure = poscar.structure
    
    miller_index = input('Please enter miller index values: ')
    #spliting the input values by space
    miller_index = tuple(int(val) for val in miller_index.split())
    
    slabgen = SlabGenerator(structure,
                           miller_index=miller_index,
                           min_slab_size=10,
                           min_vacuum_size=10)
    slabs = slabgen.get_slabs()
    
    
    surf_file = pymatgen.io.vasp.Poscar(slabs[0])
    surf_file.write_file(filename = 'POSCAR_surf' + str(miller_index))
    return()


make_slab()
