# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



# COMP9021 19T3 - Rachid Hamadi
# Quiz 1 *** Due Thursday Week 2


import sys
from random import seed, randrange


try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 2, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

mapping_as_a_list = []
one_to_one_part_of_mapping = {}
nonkeys = []

# INSERT YOUR CODE HERE]
list_elem=[]  # List to stores values of the keys in the dictionary
one_to_one_part_of_mapping.update(mapping)

for elements in range(1, upper_bound):  # To calculate integers that are not keys
    if elements in mapping.keys():
       continue
    else:
        nonkeys.append(elements)
        
for i in range (0,upper_bound):    #To represent the keys in a list
    if i in mapping.keys():
        mapping_as_a_list.append(mapping.get(i))
        list_elem.append(mapping.get(i))
    if i not in mapping.keys():
        mapping_as_a_list.append(None)
 
for number in list_elem:
    if(list_elem.count(number)) ==1 :  #Checking the occurences of the particular value in values list
       continue
    else:
        duplicate_value_key = list(one_to_one_part_of_mapping.keys())[list(one_to_one_part_of_mapping.values()).index(number)] #Extracting the key of the dupliacte value present
        del one_to_one_part_of_mapping[duplicate_value_key]
        continue
    
print() 
print('The mappings\'s so-called \"keys\" make up a set whose number of elements is',len(mapping))
print('\nThe list of integers between 1 and', upper_bound - 1, 'that are not keys of the mapping is:')
print('  ', nonkeys)
print('\nRepresented as a list, the mapping is:')
print('  ', mapping_as_a_list)
# Recreating the dictionary, inserting keys from smallest to largest,
# to make sure the dictionary is printed out with keys from smallest to largest.
one_to_one_part_of_mapping = {key: one_to_one_part_of_mapping[key]
                                      for key in sorted(one_to_one_part_of_mapping)
                             }
print('\nThe one-to-one part of the mapping is:')
print('  ', one_to_one_part_of_mapping)


