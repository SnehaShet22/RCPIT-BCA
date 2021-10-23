'''                       #0 1 2 3 4 5 6 7 8 9 10
s = "HELLO WORLD"       #H E L L O   W O R L D 
                        #                    -1 
print ( s[6]) #W 

print(s[6:11])  


txt3 = "WE \tARE THE \bSO-CALLED \"VIKINGS\" FROM THE \n  NORTH."  
print(txt3) 


#LIST 
    
s = [1,2,3, 1.2 , 3.6 , 'string' , [1,2,3], (1,2,3), True , False , False ,True] # ALL DATATYPE ELEMENTS ARE ALLOWED 


This_list = [ 'strawberry', 'pinapple', 'mango']
print (This_list)  #['strawberry', 'pinapple', 'mango']

print(len(This_list))   #3  

print(type(This_list)) # <class 'list'> 

print(type(This_list[1])) #<class 'str'> 

t= ('strawberry', 'pinapple', 'mango') 

list_1 = list(t)   #CONVERT TUPLE INTO LIST 
print(list_1)       #['strawberry', 'pinapple', 'mango']  


            #      0            1          2       3          4           5        6      7 
This_list = [ 'strawberry', 'pinapple', 'mango','grapes','pomogranate','papaya','kiwi','orange'] 
 
print(This_list[0])    #strawberry 

print(This_list[2])  #mango
print(This_list[-1])  #mango

print(This_list[2:6])   #[start : end + 1]   last value is always excluded 

print(This_list[:] )  # whole list 


if 'strawberry' in This_list:
    print("yes its present")
else:
    print("no its not present")    #yes its present 

            #      0            1          2       3          4           5        6      7 
This_list = [ 'strawberry', 'pinapple', 'mango','grapes','pomogranate','papaya','kiwi','orange'] 
print(This_list)

This_list[6] = 'blueberry'     #UPDATED THE VALUE OF KIWI TO BLUEBERRY

print(This_list)

#This_list[2: 5] = 'blueberry'   #['strawberry', 'pinapple', 'b', 'l', 'u', 'e', 'b', 'e', 'r', 'r', 'y', 'papaya', 'blueberry', 'orange']
#print(This_list)

This_list[2: 5] = ['blueberry']   #['strawberry', 'pinapple', 'blueberry', 'papaya', 'blueberry', 'orange']
print(This_list)

This_list[2: 5] = ['blueberry', 40 , 'mango', 1 ]  #['strawberry', 'pinapple', 'blueberry', 40, 'mango', 1, 'orange']
print(This_list) 

This_list.insert(3 , 450.5)  #['strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange']
print(This_list) 

This_list.append("Sejal")  #['strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal']
print(This_list)


#This_list.append("Sejal", "Sonal")  # list.append() takes exactly one argument (2 given)
#print(This_list)



# TO ADD ELEMENTS IN THE LIST 
#1. APPEND (WILL ADD ONLY 1 ELEMENT)
This_list = ['strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal']
This_list.append(["Sejal", "Sonal"])  # ['strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal', ['Sejal', 'Sonal']]
print(This_list) 

#2. EXTEND (WILL ADD ELEMENTS OF THE SEQUENCE)

This_list.extend(["Sejal", "Sonal"])  #['strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal', ['Sejal', 'Sonal'], 'Sejal', 'Sonal']
print(This_list)

This_list.extend(("Sejal", "Sonal"))  #['strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal', ['Sejal', 'Sonal'], 'Sejal', 'Sonal']
print(This_list) 


#This_list.extend("Sejal", "Sonal")  #['strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal', ['Sejal', 'Sonal'], 'Sejal', 'Sonal']
#print(This_list)  #list.extend() takes exactly one argument (2 given)

# INSERT

This_list.insert(0 , 'Girase') 
print(This_list)        #['Girase', 'strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal', ['Sejal', 'Sonal'], 'Sejal', 'Sonal']



# TO REMOVE ELEMENTS 

#1. POP
T=['Girase', 'strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal', ['Sejal', 'Sonal'], 'Sejal', 'Sonal']

T.pop()  # if no index specified then will pop last element 
print(T)            #['Girase', 'strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal', ['Sejal', 'Sonal'], 'Sejal']

T.pop(0) # POP THROUGH INDEX 
print(T)  #['strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal', ['Sejal', 'Sonal'], 'Sejal'] 

#2. DELETE
#del T[9]   #remove through index
#print(T)    #['strawberry', 'pinapple', 'blueberry', 450.5, 40, 'mango', 1, 'orange', 'Sejal', 'Sejal']  

#3. REMOVE 
T.remove( 450.5)  # remove through name of element 
print(T)    #['strawberry', 'pinapple', 'blueberry', 40, 'mango', 1, 'orange', 'Sejal', ['Sejal', 'Sonal'], 'Sejal']

# del can del the whole list
#del T        
#print (T)  #NameError: name 'T' is not defined
 
T.clear() #CLEAR WHOLE LIST / RETURN EMPTY LIST [] 
print(T)



#LIST CONCATENATION 
L1 =[1, 2, 3] 
L2 =[4, 5, 6]
L3 = L1+ L2 
print(L3)   #[1, 2, 3, 4, 5, 6]  
'''

L3 = [1, 2, 3, 4, 5, 6, 1 , 5 , 3, 5, 8] 
'''
print(L3.count(5))  # count the number of times element occured in list 
print(max(L3))
print(min(L3)) 

L3 = [1, 2, 3, 4, 5, 6, 1 , 5 , 3, 5, 8] 
L3.sort()
print(L3)   #[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 8] 

L3.reverse()
print(L3)   #[8, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1] 
'''




This_list = [ 'strawberry', 'pinapple', 'mango'] 
for i in This_list:
    print(i)

This_list = [ 'strawberry', 'pinapple', 'mango'] 
for i in range(0, len(This_list)):
    print(This_list[i])

'''strawberry
pinapple
mango''' 



i = 0 
while i< len(This_list):
    print (This_list[i])
    i +=1 

# list comprehension 

[ print(i) for i in This_list] 
'''
strawberry
pinapple
mango'''


l=This_list.copy()  #['strawberry', 'pinapple', 'mango']

print(l)



This_list = [ 'strawberry', 'pinapple', 'mango'] 
for i in This_list:
    print(i)


[ print(i)  for i in This_list]  

fruits = ['apple','strawberry', 'pinapple', 'mango', "kiwi"] 
new = [x for x in fruits if 'a' in x] 
print (new)

for x in fruits:
    if 'a' in x :
        new.append(x)   


