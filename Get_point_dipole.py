#!/usr/bin/env python

import sys

import linecache
import re
import numpy as np
from numpy import linalg

outname = sys.argv[1]

filename = './' + outname + '.out'
filename_xyz = './' + outname + '-n.xyz'

regex_begin = re.compile(r'#\s+Z\s+covCN\s+q\s+C6AA\s+')

def get_atoms_num(filename_xyz):
    
    atoms_xyz_mat = []
    atoms_num = linecache.getline(filename_xyz, 1)
    
    return int(atoms_num)

def last_entry(filename):

    entry_p = []
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            if re.search(regex_begin, line):
                entry_p += [num]
    
    return entry_p[-1]

def get_charges(filename, atom_num = get_atoms_num(filename_xyz)):
    
    entry_p = last_entry(filename) + 1
    charges_vec = []
    
    for line_num in range(entry_p, entry_p + atom_num):
        charges_vec += [float(linecache.getline(filename, line_num).split()[4])]
    
    return np.array(charges_vec)

def get_atom_xyz(filename_xyz, atom_num = get_atoms_num(filename_xyz)):
    
    atoms_xyz_mat = []
    
    for line_num in range(3, 3 + atom_num):
        atoms_xyz_mat += [linecache.getline(filename_xyz, line_num).split()[1:4]]
    
    return np.float_(atoms_xyz_mat)

def XYZ_dipoles(atom_num = get_atoms_num(filename_xyz),
                charges = get_charges(filename),
                XYZ_mat = get_atom_xyz(filename_xyz, atom_num = get_atoms_num(filename_xyz))):
    
    XYZ_dipoles = []
    
    for line_num in range(atom_num):
        XYZ_dipoles += [XYZ_mat[line_num] * charges[line_num]]

    return np.array(XYZ_dipoles)

def dipole_total():
    
    dipole_tot_XYZ = [.0, .0, .0]
    
    for vec_dip in XYZ_dipoles():
        dipole_tot_XYZ += vec_dip
#        print(vec_dip, dipole_tot_XYZ)
        
    return dipole_tot_XYZ


print(linalg.norm(dipole_total()))