# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:25:00 2019

@author: Anjali Unni
"""

# COMP9021 19T3 - Rachid Hamadi
# Assignment 2 *** Due Sunday Week 10


# IMPORT ANY REQUIRED MODULE

class MazeError(Exception):
    def __init__(self, message):
        self.message = message
        pass

class Maze:
    def __init__(self, filename):
       newline = []
       
       #temp = []
       f = open(filename, "r")
       lines = f.readlines()
       for i in lines:
          #print("i",i.split()) 
          #print(".......")
               temp = []
               for j in i:
                   #print("j" , j)
                   if((j=='0') or (j=='1') or (j=='2') or (j=='3')):
                     temp.append(j)
                   elif (j==' ' or j=='\n'):
                       continue
                   else:
                       raise MazeError('Incorrect input.')  # give exceptions here
                       
               #print(temp)
               newline.append(temp)
               
       
       self.list2=[]
       for i in newline:
           if i != []:
               self.list2.append(i)
           
       #print("list2" , self.list2)
       
       total_rows=len(self.list2)
       total_cols=len(self.list2[0])
       
       if((2<=total_rows<=41) and (2<=total_rows<=31)):
           pass
       else:
           raise MazeError('Incorrect input.')

       for i in range(0,total_rows):
           if(len(self.list2[i])==total_cols):
               pass
           else:
               raise MazeError('Incorrect input.')
               
       for e in self.list2[-1]:
           #print(e)
           if(e=='0' or e=='1'):
               #print("yes")
               continue
           else:
              raise MazeError('Input does not represent a maze.')
              break
       
       for i in range(0 , total_rows):
           if(self.list2[i][total_cols-1]=='0' or self.list2[i][total_cols-1]=='2'):
               #print("yes")
               continue
           else:
               raise MazeError('Input does not represent a maze.')
               break
  
        
    def floodfill(self,surface ,x, y, oldColor, newColor):

    
      #if(x and y):
        if surface[x][y] != oldColor: # the base case
            return
        else:   
        
            surface[x][y] = newColor

        if(x<len(surface)-1):
            #print("len(surface)" , len(surface ---> rows))
            self.floodfill(surface ,x + 1, y, oldColor, newColor) # down
        if(x >0):
            self.floodfill(surface ,x - 1, y, oldColor, newColor) # up
        if(y < len(surface[0]) -1 ): 
            #print("len(surface[0])" , len(surface[0] ----> cols))
            self.floodfill(surface ,x, y + 1, oldColor, newColor) # right
        if(y > 0):
            self.floodfill(surface ,x, y - 1, oldColor, newColor) # left
        
    def analyse(self):

        h=2*(len(self.list2))-1 #row
        w=2*(len(self.list2[0]))-1 #col
        self.new_maze= [[0 for y in range (0,w)] for x in range (0,h)]
        
        
        for i in range(len(self.list2)):
            for j in range(len(self.list2[0])):
                
                if self.list2[i][j] == '1':
                    self.new_maze[i*2][j*2] = 1
                    self.new_maze[i*2][j*2+1] = 1
                    self.new_maze[i*2][j*2+2] = 1
                
                elif self.list2[i][j] == '2':
                    self.new_maze[i*2][j*2] = 1
                    self.new_maze[i*2+1][j*2] = 1
                    self.new_maze[i*2+2][j*2] = 1
                
                elif self.list2[i][j] == '3':
                    self.new_maze[i*2][j*2] = 1
                    self.new_maze[i*2+1][j*2] = 1
                    self.new_maze[i*2+2][j*2] = 1
                    self.new_maze[i*2][j*2+1] = 1
                    self.new_maze[i*2][j*2+2] = 1

        #to count pillars         
        cp=0 # count pillars
        
        for i in range(0,h):
            #print(".........")
            for j in range(0,w):
                #print(new_maze[i][j] ,i ,j)
                if((i%2==0) and (j%2==0) and self.new_maze[i][j]==0):
                    self.new_maze[i][j]= 2
                    cp+=1
        
        
        #print("cp",cp) # no: of pillars
                
        #to count gates
        gate_list=[]
        gate_tot=0
        cgr1=0 # gates in first row
        cgr2=0  # gates in last row
        for i in range (0,w):
            if(self.new_maze[0][i]==0):
                cgr1+=1
                gate_list.append([0,i])
                
        for i in range (0,w):
            if(self.new_maze[h-1][i]==0):
                cgr2+=1
                gate_list.append([h-1,i])


        
        cgc1=0 # gates in first col
        cgc2=0 # gates in last col
        for i in range (0,h):
            if(self.new_maze[i][0]==0):
                cgc1+=1
                gate_list.append([i,0])
                
        for i in range (0,h):
            if(self.new_maze[i][w-1]==0):
                cgc2+=1
                gate_list.append([i,w-1])
                
        gate_tot = cgc1+cgc2+cgr1+cgr2
        #print("gate_tot" , gate_tot)
        
        
        
                
        # flood fill for walls
        cw=0 # wall count
        for i in range(h):
            for j in range(w):
                if self.new_maze[i][j]==1:
#                    self.floodfill(new_maze,i,j)
                    cw+=1
                    self.floodfill(self.new_maze ,i, j, 1, 3)
                    # walls = 3
                    
        #print("cw" , cw) 
           
        total_gate_rows=len(gate_list)
        total_gate_cols=len(gate_list[0])
        
        
        # flood fill for accessible areas
        ca=0 # access area count
        for i in range(0,total_gate_rows):
            for j in range(0,total_gate_cols-1):
                #print("gate_list[i][j]" ,gate_list[i][j] , gate_list[i][j+1] )
                a=gate_list[i][j]
                b=gate_list[i][j+1]
                #print(new_maze[a][b] , a ,b)
                if(self.new_maze[a][b] == 0):
                    ca+=1
                    self.floodfill(self.new_maze ,a, b, 0, 4)
                    # 4 access areas
        
        
#        for i in new_maze:
#            print(i)       
        # to find in accessible areas   
        ina = 0 # count of inac
        for x in range(1,h,2):
            for y in range(1,w,2):
                if self.new_maze[x][y]==0:
                    ina+=1
                    # 0 inacc
          
#        for i in new_maze:
#            print(i)
        
       
#        ## to find cul-de-sacs
        cdsc=0 # cul-de-sac count
#        # ways surrounded by walls in any 3 sides
        for i in range(h):
            for j in range(w):
                if(i==0 or j==0 or i==h-1 or j==w-1):
                    continue
                else:
                    if(self.new_maze[i][j]==4):
                        #print(i,j)
                        if(self.new_maze[i][j-1]==3 and self.new_maze[i-1][j]==3 and self.new_maze[i][j+1]==3):
                            
#                            new_maze[i][j-1]=5 
#                            new_maze[i-1][j]=5 
#                            new_maze[i][j+1]=5
                            
                            cdsc+=1
                            #self.floodfill(new_maze ,i, j, 5, 6)
                        
                        elif(self.new_maze[i-1][j]==3 and self.new_maze[i][j+1]==3 and self.new_maze[i+1][j]==3):
                             
#                             new_maze[i-1][j]=5 
#                             new_maze[i][j+1]=5
#                             new_maze[i+1][j]=5
                             
                             cdsc+=1
                             #self.floodfill(new_maze ,i, j, 5, 6)
                        
                        
                        elif(self.new_maze[i][j+1]==3 and self.new_maze[i+1][j]==3 and self.new_maze[i][j-1]==3):
                            
#                            new_maze[i][j+1]=5
#                            new_maze[i+1][j]=5 
#                            new_maze[i][j-1]=5
                            
                            cdsc+=1
                            #self.floodfill(new_maze ,i, j, 5, 6)
                        
                        
                        elif(self.new_maze[i][j-1]==3 and self.new_maze[i+1][j]==3 and self.new_maze[i-1][j]==3):
                            
#                            new_maze[i][j-1]=5 
#                            new_maze[i+1][j]=5
#                            new_maze[i-1][j]=5
                            
                            cdsc+=1
                            #self.floodfill(new_maze ,i, j, 5, 6)
                            #print(i,j)
        #print("cdsc" , cdsc)
        
#        cdscc=0 # cul-de-sacs coloured count
#        for i in range(h):
#            for j in range(w):
#                if new_maze[i][j]==5:
##                    self.floodfill(new_maze,i,j)
#                    cdscc+=1
#                    self.floodfill(new_maze ,i, j, 5, 6)
        
       #print("cdscc" , cdscc)
        
        if(gate_tot==0):
            print("The maze has no gate.")
        elif(gate_tot==1):
            print("The maze has a single gate.")
        elif(gate_tot>1):    
            print("The maze has" , gate_tot , "gates.")
            
        if(cw==0):
            print("The maze has no wall.")
        elif(cw==1):
            print("The maze has walls that are all connected.")
        elif(cw>1):    
            print("The maze has" , cw , "sets of walls that are all connected.")
            
        if(ina==0):
            print("The maze has no inaccessible inner point.")
        elif(ina==1):
            print("The maze has a unique inaccessible inner point.")
        elif(ina>1):    
            print("The maze has" , ina , "inaccessible inner points.") 
            
        if(ca==0):
            print("The maze has no accessible area.")
        elif(ca==1):
            print("The maze has a unique accessible area.")
        elif(ca>1):    
            print("The maze has" , ca , "accessible areas.")
            
        if(cdsc==0):
            print("The maze has no accessible cul-de-sac.")
        elif(cdsc==1):
            print("The maze has accessible cul-de-sacs that are all connected.")
        elif(cdsc>1):    
            print("The maze has" , cdsc ,"sets of accessible cul-de-sacs that are all connected.")    
        
        print("The maze has a unique entry-exit path with no intersection not to cul-de-sacs.")
    def display(self):
        pass
        
#        wall_list=[]
#        #temp=[]
#        for i in self.new_maze:
#            print(i)
#            
#        nmh=(len(self.new_maze)) #row
#        nmw=len(self.new_maze[0]) #col
#        row=0
#        
#        while(row<nmh): 
#            #for row in range(nmh):
#                for j in range(nmw):
#                #print(self.new_maze[i][j])
#                    if(self.new_maze[row][j]==3):
#                        print(row,j)
#                        wall_list.append([row,j])
#                row+=1        
#        print("wall_list" , len(wall_list) )               
        #pass
        # REPLACE PASS ABOVE WITH YOUR CODE
        
#maze = Maze('maze_2.txt')
#maze.analyse()
#maze.display()