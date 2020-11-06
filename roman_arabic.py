# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:04:04 2019

@author: Anjali Unni
"""

#import sys
import re

########################## Part 3 ##############################

def minimallyconverter(min_convert):
    
    
   if(min_convert[0]==min_convert[-1]):
          print("Hey, ask me something that's not impossible to do!")
   elif (min_convert[0]==min_convert[4]):
          print("Hey, ask me something that's not impossible to do!")
   else: 
    new_min_convert=min_convert
    #print("new_min_convert" , new_min_convert)
    
    min_convert=''.join([j for i,j in enumerate(min_convert) if j not in min_convert[:i]])
    #print("foo" , foo)
    min_con=[]
    new_min_con=[]
    mincon_index=[]
    #print("min_convert" , min_convert)
    
    for i in min_convert:
        min_con.append(i)
        
    for i in new_min_convert:
        new_min_con.append(i)    
    #print("new_min_con" , new_min_con)
    
    for i in range(0,len(min_con)):
        if(i==0):
            mincon_index.append(1)
            
            
        elif(i==1):
            mincon_index.append(5)
                      

        else:
            if(i%2==0):   # even position powers of 10
                mincon_index.append(10*pow(10,(i//2 -1)))
                
            else:  
                mincon_index.append(50*pow(10,(i//2 -1))) # odd positions powers of 5
                
    
    mincon_index=mincon_index[::-1]
    #print("mincon_index" , mincon_index)
    
    min_dictionary={}
    min_dictionary = dict(zip(min_con, mincon_index)) 
    #print("min_dictionary" , min_dictionary)
    
    answer=0
    
    pattern = re.compile("[A-Za-z]+")
    
    if(pattern.fullmatch(new_min_convert)):
     i=0
     
     while(i<len(new_min_con)-1):
        string_1=new_min_con[i]
        if(i+1 < len(new_min_con)):
           string_2=new_min_con[i+1]
           if(min_dictionary.get(string_1) != None and min_dictionary.get(string_2) !=None): 
            if(min_dictionary.get(string_1)>=min_dictionary.get(string_2)):   # also put both are not none
                answer+=min_dictionary.get(string_1) + min_dictionary.get(string_2)
                i+=2
            else:
                answer+= min_dictionary.get(string_2) - min_dictionary.get(string_1)
                i+=2
           else:
               print("Hey, ask me something that's not impossible to do!")
               break    
        else:
            pass
     if(len(new_min_con)%2==0):
                #if(((five_list_sum + (4*ten_list_sum)) - ten_list[-1])>=answer):
                   print("Sure! It is",answer,"using" ,min_convert)
                #else:
                   #print("Hey, ask me something that's not impossible to do!") 
     else:
         if(min_dictionary.get(string_1) != None and min_dictionary.get(string_2) != None):
                answer+=min_dictionary.get(min_con[-1])
                #if(((five_list_sum + (4*ten_list_sum)) - ten_list[-1])>answer):
                print("Sure! It is",answer,"using" ,min_convert) 
                  #check_validity(answer , dictionary , position_index , sc_list , first_convert)
                #else:
                    #print("Hey, ask me something that's not impossible to do!")
         else:
             pass
    
########################## Part 2 ##############################

def check_validity (answer , dictionary , position_index , sc_list , first_convert):
        new_answer=answer
        temp = []
        Roman = ""
        
        for i in range(0, len(position_index)):
             temp.append(0)
             if (answer/position_index[i]):
                quo = answer//position_index[i]
                answer = answer%position_index[i]
                temp[-1] = quo
                if quo == 4:
                    if temp[-2] == 1:
                        Roman = Roman[:-1]
                        Roman += sc_list[i] + sc_list[i-2]
                    else:
                        Roman += sc_list[i] + sc_list[i-1]
                else:
                    for j in range(0, quo):
                        Roman += sc_list[i]
        
        
        if(Roman==first_convert):
            print("Sure! It is" , new_answer)
        else:
            print("Hey, ask me something that's not impossible to do!")
            

def converter(first_convert , second_convert):
    fc_list=[]  #number before using
    sc_list=[]   #number after using
    ten_list=[]
    five_list=[]

    for i in first_convert:
      fc_list.append(i)
    for j in second_convert:
      sc_list.append(j)  

    position_index=[]
    
    for i in range(0,len(second_convert)):
        if(i==0):
            position_index.append(1)
            ten_list.append(1)
            
        elif(i==1):
            position_index.append(5)
            five_list.append(5)           

        else:
            if(i%2==0):   # even position powers of 10
                position_index.append(10*pow(10,(i//2 -1)))
                ten_list.append(10*pow(10,(i//2 -1)))
            else:  
                position_index.append(50*pow(10,(i//2 -1))) # odd positions powers of 5
                five_list.append(50*pow(10,(i//2 -1)))
               
    position_index=position_index[::-1]
    #print("pi_rev",position_index)
    
    ten_list_sum=0
    five_list_sum=0
    
    for i in ten_list:
        ten_list_sum+=i
    for i in five_list:
        five_list_sum+=i    

    dictionary={}
    dictionary = dict(zip(sc_list, position_index))    #converting to dictionary
    #print("dictionary" , dictionary)

    answer=0
    
    pattern = re.compile("[A-Za-z]+")
    pattern_num = re.compile("[0-9]+")
    
    if(pattern.fullmatch(first_convert)):
     i=0
     while(i<len(fc_list)-1):
        string_1=fc_list[i]
        if(i+1 < len(fc_list)):
           string_2=fc_list[i+1]
           if(dictionary.get(string_1) != None and dictionary.get(string_2) !=None): 
            if(dictionary.get(string_1)>=dictionary.get(string_2)):   # also put both are not none
                answer+=dictionary.get(string_1) + dictionary.get(string_2)
                i+=2
            else:
                answer+= dictionary.get(string_2) - dictionary.get(string_1)
                i+=2
           else:
               print("Hey, ask me something that's not impossible to do!")
               break    
        else:
            pass
     if(len(fc_list)%2==0):
                if(((five_list_sum + (4*ten_list_sum)) - ten_list[-1])>=answer):
                   print("Sure! It is",answer)
                else:
                   print("Hey, ask me something that's not impossible to do!") 
     else:
         if(dictionary.get(string_1) != None and dictionary.get(string_2) != None):
                answer+=dictionary.get(fc_list[-1])
                if(((five_list_sum + (4*ten_list_sum)) - ten_list[-1])>answer):
                  #print("Sure! It is",answer) 
                  check_validity(answer , dictionary , position_index , sc_list , first_convert)
                else:
                    print("Hey, ask me something that's not impossible to do!")
         else:
             pass
    
    elif(pattern_num.fullmatch(first_convert)):
        first_convert=int(first_convert)

        temp = []
        Roman = ""
        
        for i in range(0, len(position_index)):
             temp.append(0)
             #temp.append("")
             #while(first_convert/position_index[i]):
             if (first_convert/position_index[i]):
                quo = first_convert//position_index[i]
                first_convert = first_convert%position_index[i]
                temp[-1] = quo
                if quo == 4:
                    if temp[-2] == 1:
                        Roman = Roman[:-1]
                        Roman += sc_list[i] + sc_list[i-2]
                    else:
                        Roman += sc_list[i] + sc_list[i-1]
                else:
                    for j in range(0, quo):
                        Roman += sc_list[i]
        
        print("Sure! It is" , Roman)
    else:
         print("Hey, ask me something that's not impossible to do!")   
         

def check_duplicate(second_convert):
     for i in second_convert:
         if(second_convert.count(i)>1):
           return True

########################## Part 1 ##############################

def converttoDecimal(string):

    temp=0
    i=0
    Roman_list=["I","V","X","L","C","D","M"]
    Decimal_list=[1,5,10,50,100,500,1000]

    while(i<len(string)):  
        fn=" "
        sn=" "
        fn=string[i]
        fn_index=Roman_list.index(fn)   #index of the first string
        if(i+1 < len(string)):
            sn=string[i+1]
            sn_index=Roman_list.index(sn)   #index of the second string
        else:
            temp+=Decimal_list[fn_index]
            i+=1
            break

        if(Decimal_list[fn_index]>=Decimal_list[sn_index]):
            temp+=Decimal_list[fn_index]
            i+=1
            
        else:
            temp+=Decimal_list[sn_index] - Decimal_list[fn_index]
            i+=2
        
    print("Sure! It is",temp)

        
def converttoRoman(number):
    RomanNumeral=""
    toRoman={1000:"M",
         900:"CM",
         500:"D",
         400:"CD",
         100:"C",
         90:"XC",
         50:"L",
         40:"XL",
         10:"X",
         9:"IX",
         5:"V",
         4:"IV",
         1:"I"
         } 
    while(number>0):
     for keys in toRoman.keys():
        if(number // keys):
            RomanNumeral+=toRoman.get(keys)
            number=number-keys
            break       
    
    print("Sure! It is",RomanNumeral)  
    
###################### main ######################################      

flag=0
ip_string = input("How can I help you? ")
ip_list=ip_string.split()


for i in ip_string:
    if(i.isdigit()and len(ip_list)==3):
        flag+=1
    else:
        pass
    
# alter here main if statements
if(flag>0):
    number_check_one=ip_list[-1]
    number=int(number_check_one)
    if(number>0 and number<4000 and len(ip_list)==3 and "Please convert " in ip_string and number_check_one[0]!="0"):                    #main if statements 
           converttoRoman(number)
    elif("please convert" in ip_string):
        print("I don't get what you want, sorry mate!")
    else:
         print("Hey, ask me something that's not impossible to do!")

elif(len(ip_list)==3 and ip_list[-1].isupper() and "Please convert " in ip_string):
    pattern = "^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    Roman=ip_list[-1]
    if re.search(pattern, Roman):
       converttoDecimal(Roman)
    else:
        print("Hey, ask me something that's not impossible to do!")
       
elif("using" in ip_string and len(ip_list)==5 and "Please convert " in ip_string):
    first_convert=ip_list[-3]
    second_convert=ip_list[-1]
    pattern = re.compile("[A-Za-z0-9]+")
    if(pattern.fullmatch(first_convert) and pattern.fullmatch(second_convert)):
        if(not check_duplicate(second_convert)):
          converter(first_convert , second_convert)
        else:  
            print("Hey, ask me something that's not impossible to do!")
    else:
        print("Hey, ask me something that's not impossible to do!")
        
elif("Please convert " and "minimally" in ip_string and len(ip_list)==4):
    min_convert = ip_list[-2]
    pattern = re.compile("[A-Za-z]+")
    if(pattern.fullmatch(min_convert)):
        minimallyconverter(min_convert)
    else:
        print("Hey, ask me something that's not impossible to do!")
        
else:
    print("I don't get what you want, sorry mate!")
