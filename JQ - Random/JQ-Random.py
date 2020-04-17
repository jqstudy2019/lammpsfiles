###############################################################################################################################
# JQ-Random - Example for SURF Presentation 
#
# By: John Quinn
#
# Date: 4/16/2020
#
# Summary of Code: (General Steps of code)
#   0. Import Packages 
#
#   1. Specify Parameters 
#		
#	2. Generate Random Atom Positons 
#
#   3. Write LAMMPS Data file 
#
# Apendix of Commands:
#	(Command -> commands function ; format( Command arg1 arg 2 . . .) ; more notes)
#		
# Refrences:
#   https://github.com/bdhuddleston/encodeventor
#
#   https://www.youtube.com/watch?v=16_CJeAN8t0
#
###############################################################################################################################

# 0. Import Packages 

import numpy as np


# 1. Specify Parameters 

num_atoms = 1000                                       # Number of Atoms to Wrtie/Generate

sys_size = 100                                      # Size of the Simulation Box (Will be set size in x,y,and z)


# 2. Generate Random Atom Positons

positions = []                                      # Creates Empty Vector to write random numbers too

for i in range(num_atoms):                             # Iterate for number of atoms set
    positions.append(np.random.rand(3)*sys_size)       # For each atom, write 3 random numbers on the end of the Positon Vector
    
    
# 3. Write LAMMPS Data File
 
 with open('JQ-random.data','w') as fdata:
	
    # First line is a comment line 
	fdata.write('Random Atoms - Written For JQ-Random - An exmaple made by: John Quinn\n\n')
	
	#--- Header ---#
	
    # Specify number of atoms and atom types 
	fdata.write('{} atoms\n'.format(num_atoms))
	fdata.write('{} atom types\n'.format(1))
	
    # Specify box dimensions
	fdata.write('{} {} xlo xhi\n'.format(0.0, sys_size))
	fdata.write('{} {} ylo yhi\n'.format(0.0, sys_size))
	fdata.write('{} {} zlo zhi\n'.format(0.0, sys_size))
	fdata.write('\n')


	# Atoms section
	fdata.write('Atoms\n\n')

	# Write each position 
	for i,pos in enumerate(positions):
		fdata.write('{} 1 {} {} {}\n'.format(i+1,*pos))

