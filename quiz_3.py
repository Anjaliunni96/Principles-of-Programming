# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
x=0
y=0
all_cordinates=[[0,0]]
duplicate_values=[]

number='0' * nb_of_leading_zeroes +f'{int(code):o}'

def reverse(num):
    return num[::-1]

r=reverse(number) 

for i in r:
    xy_cordinates=[]
    if(i=='0'):
       y+=1
    elif(i=='1'):
        x+=1
        y+=1
    elif(i=='2'):
        x+=1
    elif(i=='3'):
        x+=1
        y-=1
    elif(i=='4'):
        y-=1
    elif(i=='5'):
        x-=1
        y-=1
    elif(i=='6'):
        x-=1
    elif(i=='7'):
        x-=1
        y+=1
    xy_cordinates=[x,y]
    all_cordinates.append(xy_cordinates)
    
        
#print("all_cordinates : ",all_cordinates)  

for elements in all_cordinates:
    if(all_cordinates.count(elements)>1):
        duplicate_values.append(elements)
        
#print("duplicate_values :",duplicate_values)

x_cordinates=[]
y_cordinates=[]

plotted_list=[]
plotted_list_2=[]

for elements in all_cordinates:
    if(elements not in duplicate_values):
        plotted_list.append(elements)
    else:
        if((duplicate_values.count(elements))%2==0):
            continue
        else:
            plotted_list.append(elements)
            
#print("plotted_list :",plotted_list)            
            
if plotted_list == []:
  print('')
  pass  
  sys.exit()              
            
for x,y in plotted_list:
    x_cordinates.append(x)
    y_cordinates.append(y)

#print("x_cordinates",x_cordinates)
#print("y_cordinates",y_cordinates) 

max_x_cord=max(x_cordinates)
max_y_cord=max(y_cordinates) 

#print("maxx",max_x_cord)  
#print("maxy",max_y_cord)  

min_x_cord=min(x_cordinates)
min_y_cord=min(y_cordinates)

#print("minx",min_x_cord)  
#print("miny",min_y_cord) 
#
#print("pl",plotted_list)

for j in range(min_y_cord,max_y_cord+1):
    temporary_plotted_list=[]
    for i in range(min_x_cord,max_x_cord+1):
        if [i,j] in plotted_list:
#            print("[i,j]",[i,j])
            temporary_plotted_list.append(on)
#            print("temporary_plotted_list-on :" ,temporary_plotted_list)
        else:
            temporary_plotted_list.append(off)
#            print("[i,j]",[i,j])
#            print("temporary_plotted_list-off :" ,temporary_plotted_list)
    plotted_list_2.append(temporary_plotted_list) 
#    print("plotted_list_2:",plotted_list_2)
    
reverse_plotted_list_len=reversed(range(len(plotted_list_2)))

#print(".................")
for elements in reverse_plotted_list_len:
     print(''.join(plotted_list_2[elements])) 


