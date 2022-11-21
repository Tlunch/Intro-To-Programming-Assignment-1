# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:55:08 2019

@author: Calum Lynch
"""

import sys
import copy as c
import numpy as np

#Task 1
a,b = input("Please enter two CSVs for the start position: ").split(",")
a = int(a);b = int(b)
start = [a,b]
a,b = input("Please enter two CSVs for the final position: ").split(",")
a = int(a);b = int(b)
end = [a,b]

#Task 2
file_to_open = input("Input the map matrix file to open: ") #opening file
roads = open(file_to_open,"r")
print()

M = []  #setting up matrice
M = roads.readlines()

for x in range(len(M)): #cleaning up matrice
    y = M[x].strip()
    M[x] = y
for x in range(len(M)):
    y = M[x].split()
    M[x] = y
    
city_map = np.array(M, dtype = "int32") #switching to a np array and assigninng to var name city_map

#Task 3
def check_bounds(coord_pos):
    """Checks if a initial starting value is within bounds"""
    if   file_len(roads)-1 < coord_pos or 0 > coord_pos:
        sys.exit("Error: Initial values outwith city_map!")
    return

def file_len(d):
    """returns number of lines in the file"""
    d.seek(0)
    l = len(d.readlines())
    return l

check_bounds(start[0]); check_bounds(start[1]); check_bounds(end[0]); check_bounds(end[1])

#Task 4
def is_valid(fpath, fcity_map, fc_pos, n_pos):
    """decides if next position is valid"""
    if fcity_map[fc_pos[0]][fc_pos[1]] > fcity_map[n_pos[0]][n_pos[1]] and n_pos not in fpath:
        return 1
    return 0

#Task 5
def find_path():
    """calls sets up and calls functions to find path"""
    global c_pos
    global c_path
    global path
    global output
    c_pos = c.copy(start)
    c_path = []
    path = []
    output = None
    procedure()
    return
        
def procedure():
    """iterates the algorithem and runs checks"""
    global c_pos
    global path
    global c_path
    global output
    path.append(c.copy(c_pos))
    c_path.append(c.copy(c_pos))    
    if c_pos == end:
        output = True
    if output != None:
        return
    move()
    procedure()

def move():
    """deciding which direction to move"""
    global c_pos
    if is_valid(path, city_map, c_pos, north(c_pos)) == 1:
        c_pos = north(c_pos)
        return
    elif is_valid(path, city_map, c_pos, east(c_pos)) == 1:
        c_pos = east(c_pos)
        return
    elif is_valid(path, city_map, c_pos, south(c_pos)) == 1:
        c_pos = south(c_pos)
        return
    elif is_valid(path, city_map, c_pos, west(c_pos)) == 1:
        c_pos = west(c_pos)
        return
    c_pos = backtrack()
    return

"""These functions return the position moved by one space"""
def north(position):
    fpos = c.copy(position)
    fpos[0] = fpos[0]-1
    fpos = perodic_boundary(fpos)
    return fpos
def east(position):
    fpos = c.copy(position)
    fpos[1] = fpos[1]+1
    fpos = perodic_boundary(fpos)
    return fpos
def south(position):
    fpos = c.copy(position)
    fpos[0] = position[0]+1
    fpos = perodic_boundary(fpos)
    return fpos
def west(position):
    fpos = c.copy(position)
    fpos[1] = fpos[1]-1
    fpos = perodic_boundary(fpos)
    return fpos

def perodic_boundary(fx):
    """This function checks if the inputed coorinates has passed the edge of the map and need to loop"""
    if fx[0] > file_len(roads) - 1:
        fx[0] = fx[0] - file_len(roads)
    if fx[1] > file_len(roads) - 1:
        fx[1] = fx[1] - file_len(roads)
    if fx[0] < 0:
        fx[0] = fx[0] + file_len(roads)
    if fx[1] < 0:
        fx[1] = fx[1] + file_len(roads)
    return fx

def backtrack():
    """backs up the current position and removes the move from the current path"""
    global c_path
    global output
    c_path.pop()
    if c_path == []:
        output = False
        return
    pos = c_path[-1]
    c_path.pop()
    return pos
        
find_path()

#Task 6
if output == False:
    print("No sutiable paths exist")
    
if output == True: #checks the output from task 5
    print("Path found with {} steps.".format(len(c_path)))

#Task 7
    for x1 in range(file_len(roads)): #define the number of rows going to be printed
        print()
        for y1 in range(file_len(roads)):#defines number of columns (same as rows as city_map is a square matrix)
            if [x1,y1] in c_path:
                print("{:^3}".format(c_path.index([x1,y1])+1), end="")
            else:
                print("__ ",end="")



roads.close()
