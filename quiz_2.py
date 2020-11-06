# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint


try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE

## question 2

new_list=[]
new_key=[]
deleting_key=[]

map_length=len(mapping)
new_mapping={}

new_mapping.update(mapping)

for i in range (0,map_length):
     if(list(mapping)[i]==list(mapping.values())[i]):
         new_key.append(list(mapping)[i])
         cycles.append(list(new_key))
         deleting_key.append(list(mapping)[i])
     else:
          continue
     new_key.clear()    
     
for i in deleting_key:
    del mapping[i]
    map_length-=1

for i in range(1,len(mapping)+1):
    deleting_list=[]
    for keys,values in mapping.items():
        if values not in mapping.keys():
             deleting_list.append(keys)
    for elements in deleting_list:
        del mapping[elements]
        
deleting_list.clear()

for i in range(1,len(mapping)+1):
    deleting_list=[]
    for keys,values in mapping.items():
        if keys not in mapping.values():
            deleting_list.append(keys)
    for elements in deleting_list:
        del mapping[elements]

for keys,values in mapping.items():
     new_list.append(keys)
     
     
##########unsorted###############

#new_key=[]
#new_val=[]
#new=[]
#
#
#for keys,values in mapping.items():
#    new_key.append(keys)
#    new_val.append(values)
#    
#    
#print("new_key",new_key)
#print("new_val",new_val)    
#    
#for i in range(0,len(new_key)):
#    start_value=new_key[i]
#    print("sv",start_value)
#    final_value=new_val[i]
#    print("fv",final_value)
#    new.append(start_value)
#    new.append(final_value)
#    
##    new_key.remove(start_value)
#    print("rm_k",new_key)
##    new_val.remove(final_value)
#    print("rm_v",new_val)
#    if(final_value in new_key):
#        to_append_index_key=new_key.index(final_value)
#        to_append_index_val=new_val[to_append_index_key]
#        if(to_append_index_val not in new):
#            new.append(to_append_index_val)
#            final_value=to_append_index_val
#            continue
#        
#        
#    
#
#
#
#
#print("new",new)






########################     
     
     
     
     
if(new_list==[]):
    pass
else:
    cycles.append(new_list) 
cycles.sort()
    
   
## question 3

mapping.clear()    
mapping.update(new_mapping)
new_map_len=len(mapping)   

inverse_mapping={}
temp_inverse_mapping_list=[]

for keys, values in mapping.items():
    inverse_mapping[values] = inverse_mapping.get(values, [])
    inverse_mapping[values].append(keys)
    
for keys, values in inverse_mapping.items():        
  if(len(values) in reversed_dict_per_length):
        reversed_dict_per_length[len(values)][keys]=values
  else:
        reversed_dict_per_length[len(values)]={keys : values}          
    
print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
print(reversed_dict_per_length)