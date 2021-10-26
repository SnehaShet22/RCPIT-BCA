#SETS ARE UNORDERED 
'''
a = {'apple','banana','mango'}  #{'banana', 'mango', 'apple'}
l = ['apple','banana','mango']  # ['apple', 'banana', 'mango']

print(a) 
print(l) 

#DUPLICATES NOT ALLOWED 


a = {'apple','banana','mango','apple'}  
print(a)                              #{'banana', 'mango', 'apple'}  

print(len(a))   #3  does not count duplicate 

print(type(a))  # <class 'set'>

a = {'apple'}
print(type(a)) # <class 'set'>

#SET CAN CONTAIN DIFFERENT DATATYPE  

set1 = {1 , 2.5 , 'abc',True , 40}  

# the set constructor set()
this_set = set((1,2,3,4,5))   #notice the double parenthesis

this_set = set([1,2,3,4,5]) 
print(this_set)
type(this_set)   #<class 'set'> 


this_set = {'apple','banana','mango'} 

for x in this_set:
    print(x)  

\'''
mango
banana
apple
\'''  
#ACCESS SINGLE ELEMENT 
if "banana" in this_set:   #banana
    print("banana")
else:
    print("none")


if "kiwi" in this_set:   #none
    print("banana")
else:
    print("none")


# IN SETS WE CAN ADD OR REMOVE ELEMENTS

#ADD add()  can add 1 element at a time 


this_set = {'apple','banana','mango'} 

this_set.add('cherry')
print(this_set)        #{'apple', 'cherry', 'mango', 'banana'} 



this_set = {'apple','banana','mango'} 

this_set.add('apple')
print(this_set)          #{'banana', 'apple', 'mango'}   no changes bcz sets wont allow duplicate # no error 

#UPDATE update()   #ADD ANY ITERABLE 

this_set = {'apple','banana','mango'} 

this_set.update('apple')    #{'l', 'apple', 'e', 'mango', 'banana', 'p', 'a'}
print(this_set)             # make sure you go for list or tuple or set while using update function 


#USING TUPLE
this_set = {'apple','banana','mango'} 

this_set.update(('apple','cherry','mango'))    #{'cherry', 'mango', 'banana', 'apple'}
print(this_set)             # make sure you go for list or tuple or set while using update function 


#USING LIST
this_set = {'apple','banana','mango'} 

this_set.update(['apple','cherry','mango'])    #{'cherry', 'mango', 'banana', 'apple'}
print(this_set) 


#removing elements
# REMOVE remove()

this_set = {'apple','banana','mango'}  

this_set.remove("banana") 

print(this_set)    #{'apple', 'mango'} 

\'''
this_set = {'apple','banana','mango'}  

this_set.remove("kiwi") 

print(this_set)     #RAISE AN ERROR BECAUSE ELEMENT NOT PRESENT  " KeyError: 'kiwi' "
\'''


#DISCARD discard() 

this_set = {'apple','banana','mango'}  

this_set.discard("banana") 

print(this_set)    #{'apple', 'mango'} 


this_set = {'apple','banana','mango'}  

this_set.discard("kiwi") 

print(this_set)     # NO ERROR EVEN IF ELEMENT NOT PRESENT 
                    #{'apple', 'mango', 'banana'}



#the POP method 

this_set = {'apple','banana','mango'}  

this_set.pop()  #will remove random element if not given value 

print(this_set)   #{'mango', 'apple'} 
\'''
this_set.pop('apple')   # only takes index number cant take values 
print(this_set) 
\'''



#clear  this clears all elements of the set 

this_set = {'apple','banana','mango'}  
this_set.clear() 
print(this_set)  #set()  empty set   
\'''
del this_set
print(this_set)  #NameError: name 'this_set' is not defined  
\'''

\'''

for x in this_set:
    print(x)  

\'''
mango
banana
apple
 

# CAN'T USE WHILE LOOP IN SET BECAUSE WE DONT USE INDEX IN SETS 

# JOINING 2 SETS  union()  , update ()

#UNION union() 

set_1 = {1 , 2 , 3}
set_2 = {"s","n","o","w", 1, 2, 3} 

set_3 = set_1.union(set_2) #{1, 2, 3, 'o', 'n', 'w', 's'}

print(set_3)              # WONT PRINT SAME ELEMENTS TWICE 
 
#UPDATE 

set_1 = {1 , 2 , 3}
set_2 = {"s","n","o","w"} 

s= set_1.update(set_2) 

print(s)    #None 

# THE UPDATE METHOD UPDATES THE EXISTING SET AND DOES NOT CREATE A NEW SET 

print(set_1)  # UPDATED SET {1, 2, 3, 'o', 'n', 'w', 's'}
print(set_2)  #{'o', 's', 'n', 'w'} 

# set_1.update(set_2) affected only set_1 no changes in set_2 
# set_2.update(set_1) affected only set_2 no changes in set_1  


phone = {'REALME'} 
software_update = {"android 10"}

phone.update(software_update)  #install that update on your phone 

print(phone)   #{'REALME', 'android 10'}  phone got updated

print(software_update)    # {'android 10'} no changes in software update 

 
    # 1st                #2nd 
software_update.update(phone) 
print(phone)                   #{'REALME'} no changes 

print(software_update)         #{'android 10', 'REALME'} 

# only 1st set will get updated no changes on 2nd  

# KEEP ONLY DUPLICATES BETWEEN 2 SETS 


#keep ONLY the Duplicates 


# INTRERSECTION_ UPDATE VS INTERSECTION 

#BOTH WILL RETURN COMMON ELEMENTS OF THE 2 DIFFERENT SETS 
x = {"apple", "mango", " banana"}
y = {"google","microsoft","apple"} 

x.intersection_update(y)         # wont create new set but update existing one 

print(x)  #{'apple'}   only 1st set got affected
print(y)  # {'google', 'microsoft', 'apple'} 



x = {"apple", "mango", " banana"}
y = {"google","microsoft","apple"} 

z = x.intersection(y)    # create a new set , wont affect existing set 
print(x)  #{'mango', ' banana', 'apple'}
print(y)  #{'google', 'microsoft', 'apple'}
print(z)  #{'apple'} 
''' 

#keep ALL , but NOT the Duplicates 
# THIS WILL GIVE ME ALL ELEMENTS EXCEPT THE ELEMENT WHICH IS DUPLICATE 

# SYMETRIC_DIFFERENCE_ UPDATE VS SYMMETRIC_DIFFERENCE 


x = {"apple", "mango", " banana"}
y = {"google","microsoft","apple"} 

x.symmetric_difference_update(y)  

print(x)  #{' banana', 'google', 'mango', 'microsoft'} it didnt return "apple" bcz apple was present in another list too (duplicate)


x = {"apple", "mango", " banana"}
y = {"google","microsoft","apple"} 

z = x.symmetric_difference(y)  #{' banana', 'google', 'mango', 'microsoft'}

print(z) 

# UPDATE METHOD = NO NEED OF NEW VARIABLE , WILL UPDATE EXISTING SET 



#DIFFERENCE  

x = {"apple", "mango", " banana"}
y = {"google","microsoft","apple"} 

z = x.difference(y)   # {' banana', 'mango'}
print(z) 

m = y.difference(x)   #{'google', 'microsoft'} 
print(m)   
#DIFFERENCE  

x = {"apple", "mango", " banana"}
y = {"google","microsoft","apple"} 

x.difference_update(y)   # {' banana', 'mango'}
print(x)                 


