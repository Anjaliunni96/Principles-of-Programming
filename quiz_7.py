# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).


from random import seed, randrange
import sys


dim = 10
flagone = 2
global row
global col
spikes = 0
maximum=0


def display_grid():
    for row in grid:
        print('   ', *row) 
        
def DSF_recur(grid, row, col, visited, count):
    rowNbr = [-1 , 0 ,1 ,0] 
    colNbr = [0 ,-1 , 0 ,1] 
    for k in range(4): 
        if (isSafe(grid, row + rowNbr[k], 
				col + colNbr[k], visited)): 
            count[0] += 1
            DFS(grid, row + rowNbr[k], 
                col + colNbr[k], visited, count)
    
def isSafe(grid, row, col, visited): 
	return ((row >= 0) and (row < 10) and
			(col >= 0) and (col < 10) and
			(grid[row][col] and not visited[row][col])) 

def DFS(grid, row, col, visited, count):
	global flagone
	
	visited[row][col] = True
    
	max_number_of_spikes(row,col)
    
	DSF_recur(grid, row, col, visited, count)
    
	#grid[row][col] = flagone

def largestRegion(M): 
	global flagone
	global spikes
	global maximum
	visited = [[0] * dim for i in range(dim)] 
#	for i in range(dim):
#		visited = [0] * dim
        
	result = -999999999999
	for i in range(dim): 
		for j in range(dim): 
			# If a cell with value 1 is not visited
			if (grid[i][j] and not visited[i][j]): 
				count = [1] 
				#print("indices")
				spikes = 0
				DFS(grid, i, j, visited , count)
				#print("maximum" , maximum) 
				flagone+=1
				result = max(result , count[0]) 
	return result 

def colour_shapes():
    global maximum

    largestRegion(grid)
    #print("largestRegion(grid)" , largestRegion(grid))
    
    print("The maximum number of spikes of some shape is:" , maximum)
    #print("@@@@@@@@@@@")
     #display_grid()	

def max_number_of_spikes(row , col):
    #print(row,col)
    
    global spikes
    global maximum
    
    if (row==0 and col==0 ):
        if((grid[row+1][col]==1 and grid[row][col+1]!=1) 
        or
        (grid[row+1][col]!=1 and grid[row][col+1]==1)):
            spikes+=1
            #print("grid[row+1][col] , grid[row][col+1]",grid[row+1][col] , grid[row][col+1])
            
    elif(row==dim-1 and col==0):
        if((grid[row-1][col]==1 and grid[row][col+1]!=1) 
        or
        (grid[row-1][col]!=1 and grid[row][col+1]==1)):
            spikes+=1
            #print("grid[row-1][col] , grid[row][col+1]",grid[row-1][col] , grid[row][col+1])
            
    elif(row==0 and col==dim-1):
        if((grid[row+1][col]==1 and grid[row][col-1]!=1) 
        or
        (grid[row+1][col]!=1 and grid[row][col-1]==1)):
            spikes+=1
            #print("grid[row+1][col] , grid[row][col-1]",grid[row+1][col] , grid[row][col-1])
            
    elif(row==dim-1 and col==dim-1):
        if((grid[row-1][col]==1 and grid[row][col-1]!=1) 
        or
        (grid[row-1][col]!=1 and grid[row][col-1]==1)):
            spikes+=1    
            #print("grid[row-1][col] , grid[row][col-1]",grid[row-1][col] , grid[row][col])
            
    elif(row==0):
        if((grid[row+1][col]==1 and grid[row][col-1]!=1 and grid[row][col+1]!=1) 
        or
        (grid[row+1][col]!=1 and grid[row][col-1]==1 and grid[row][col+1]!=1)
        or
        (grid[row+1][col]!=1 and grid[row][col-1]!=1 and grid[row][col+1]==1)):
            spikes+=1
            #print("grid[row+1][col] , grid[row][col-1]",grid[row+1][col] , grid[row][col-1])
            
    elif(col==0):
        if((grid[row-1][col]==1 and grid[row][col+1]!=1 and grid[row+1][col]!=1) 
        or
        (grid[row-1][col]!=1 and grid[row][col+1]==1 and grid[row+1][col]!=1)
        or
        (grid[row-1][col]!=1 and grid[row][col+1]!=1 and grid[row+1][col]==1)):
            spikes+=1
            #print("grid[row-1][col] , grid[row][col+1] ,grid[row+1][col]",grid[row-1][col] , grid[row][col+1] , grid[row+1][col])
            
    elif(row==dim-1):
        if((grid[row-1][col]==1 and grid[row][col-1]!=1 and grid[row][col+1]!=1) 
        or
        (grid[row-1][col]!=1 and grid[row][col-1]==1 and grid[row][col+1]!=1)
        or
        (grid[row-1][col]!=1 and grid[row][col-1]!=1 and grid[row][col+1]==1)):
            spikes+=1
            #print("grid[row-1][col] , grid[row][col-1] , grid[row][col+1]",grid[row-1][col] , grid[row][col-1] , grid[row][col+1])
            
    elif(col==dim-1):
        if((grid[row-1][col]==1 and grid[row][col-1]!=1 and grid[row+1][col]!=1) 
        or
        (grid[row-1][col]!=1 and grid[row][col-1]==1 and grid[row+1][col]!=1)
        or
        (grid[row-1][col]!=1 and grid[row][col-1]!=1 and grid[row+1][col]==1)):
            spikes+=1 
            #print("grid[row-1][col],grid[row][col-1],grid[row+1][col]" , grid[row-1][col],grid[row][col-1],grid[row+1][col])
            
    else:
        if(((grid[row-1][col]==1 and grid[row+1][col]!=1) 
        and (grid[row][col+1]!=1 and grid[row][col-1]!=1))
        or
        ((grid[row-1][col]!=1 and grid[row+1][col]==1) 
        and (grid[row][col+1]!=1 and grid[row][col-1]!=1))
        or
        ((grid[row-1][col]!=1 and grid[row+1][col]!=1) 
        and (grid[row][col+1]==1 and grid[row][col-1]!=1))
        or
        ((grid[row-1][col]!=1 and grid[row+1][col]!=1) 
        and (grid[row][col+1]!=1 and grid[row][col-1]==1))
        ):
            spikes+=1
            #print("grid[row-1][col],grid[row+1][col],grid[row][col+1] ,grid[row][col-1]",grid[row-1][col],grid[row+1][col],grid[row][col+1] ,grid[row][col-1])
    

    #print("Spikes" , spikes) 
    if(maximum<spikes):
        maximum=spikes
#    print("maximum" , maximum)     
    #print("list" , max(spikes_list))



try: 
    global row 
    global col
    
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
nb_of_shapes = colour_shapes()
#print('The maximum number of spikes of some shape is:',
#      max_number_of_spikes(row , col)
#     )
