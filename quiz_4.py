# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys

def check(a_list):
    temp_list=[]

    if(a_list.count(",")==arity-1):
        return True
    else:
        return False
    
    for i in range(len(a_list)):
        if(a_list[i].isalpha()):
            temp_list.append(word[i])
     
    for i in a_list:
        if(ord(i)==95):
            return True
    
    if(len(temp_list)==arity):
        return True
    else:
        return False
            
            
def is_valid(word, arity):
   without_change_word=word
   count=0
   if(arity==0):    #check for words
     for i in word:
        if((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)or (ord(i)==95) or (ord(i)==32)):
            count+=1
     if(count==len(word)):
        return True
     else:
        return False
   else:  
    stack=[]
    new_list=[]
    i = 0
    while True:
        #print("i",i)
        if i >= len(word):
            break
        if(word[i]!=")"):
            stack.append(word[i])
            #print("appending_stack",stack)
        elif(word[i]==")"):
            j = i
            while(word[i]!="("):
                stack.pop()
                #print("popping_stack",stack)
                i-=1
                #print("decrement_i",i)
            new_list = word[i:j+1]
            #print("appending_newlist",new_list)
            word = word[:i]+word[j+1:]
#            print("wording",word)
#            print("new_list",new_list)
#            print("word",word)
            check(new_list)
            #print("checking",check(new_list))
            if(check(new_list)):
              continue
            else:
              break
            
            i = 0
        i+=1

  # print("word",word) 
   for i in range(len(word)):
       if((word[i]=="(") or (word[i]==" ")):
           return False
       
   
   if(check(new_list) and word):
       if(word != without_change_word):
            return True
   else:
       return False
   
try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')

