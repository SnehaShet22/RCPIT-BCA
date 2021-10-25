'''
#                  0           1       2 
this_tuple = ('strawberry','orange', 'kiwi') 

print(this_tuple)       #('strawberry', 'orange', 'kiwi') 

print(this_tuple[2])    #kiwi
print(this_tuple[-1])   #kiwi 

t = ( 'strawberry', 'pinapple', 'mango','grapes','pomogranate','papaya','kiwi','orange')  
print(t[2:5])  #('mango', 'grapes', 'pomogranate')

print(len(this_tuple))  #3 

t = ('strawberry')   
print(type(t))      #<class 'str'> 

t = ('strawberry',) 
print(type(t))      #<class 'tuple'> 

#to create a tuple with only one item , you have to add a comma after the item , 
# otherwise python will not recognize it as a tuple 

t = (" ", " ")  # we can take blank space as one element in tuple

print(len(t))   #2  

s = (1,2,3, 1.2 , 3.6 , 'string' , [1,2,3], (1,2,3), True , False , False ,True) # ALL DATATYPE ELEMENTS ARE ALLOWED 


#TUPLE()  CONSTRUCTOR
s = ["a",'b','c']  

b = tuple (s)  
print(b)       #('a', 'b', 'c') 

if 'a' in b :
    print("a is present")   #a is present
else:
    print("its not present")  

\'''
#                  0           1       2 
this_tuple = ('strawberry','orange', 'kiwi')  


this_tuple[2]= 'blueberry'  # this_tuple[2]= 'blueberry'
                            #TypeError: 'tuple' object does not support item assignment 
\'''
#                  0           1       2 
this_tuple = ('strawberry','orange', 'kiwi')  
print(this_tuple)     #('strawberry', 'orange', 'kiwi')

c = list(this_tuple)  #1st convert tuple into list 
c[2]= 'blueberry'     # do the changes you need 
this_tuple= tuple(c)  #finally convert list back to tuple 
print(this_tuple)            #('strawberry', 'orange', 'blueberry')  



t = ("strawberry", ' kiwi')
s = ('mango','banana')  

print(t+s)  #('strawberry', ' kiwi', 'mango', 'banana')

t = (1 , 2 , 3)
s = (4 ,)  

print(t+s)   #  (1, 2, 3, 4) 


t = (1 , 2 , 3)
s = ('string',)  

print(t+s)   #  (1, 2, 3, 'string')

#TUPLE UNPACKING

b = ('strawberry', ' kiwi', 'mango', 1 )  
(red,green,yellow,blue) = b 
print(red)    #strawberry
print (green) # kiwi
print(yellow) # mango
print(blue)   # 1 

\'''

t = ( 'strawberry', 'pinapple', 'mango','grapes','pomogranate','papaya','kiwi','orange')  
(red,green,yellow,blue) = t 
print(red)                   #(red,green,yellow,blue) = t
                             #ValueError: too many values to unpack (expected 4)
\''' 

t = ( 'strawberry', 'pineapple', 'mango','grapes','pomogranate','papaya','kiwi','orange')  
(red,green,yellow,*blue) = t 
print(red)      #strawberry
print (green)   #pineapple
print(yellow)   #mango
print(blue)     # ['grapes', 'pomogranate', 'papaya', 'kiwi', 'orange']  



t = ( 'strawberry', 'pineapple', 'mango','grapes','pomogranate','papaya','kiwi','orange')  
(red,green,*yellow,blue) = t 
print(red)      #strawberry
print (green)   #pineapple
print(yellow)   #['mango', 'grapes', 'pomogranate', 'papaya', 'kiwi']
print(blue)     # orange 



b = ('strawberry', ' kiwi', 'mango', 1 )  

for i in b :             
    print (i)  

for i in range(len(b)):
    print(b[i])

i = 0
while i< len(b):
    print(b[i])
    i+= 1 


b = ('strawberry', ' kiwi', 'mango', 1 )
t = b*2
print(t)  #('strawberry', ' kiwi', 'mango', 1, 'strawberry', ' kiwi', 'mango', 1)  



b = ('strawberry', ' kiwi', 'mango', 1 ,'strawberry','strawberry' )

print(b.count('strawberry'))  #3 


print(b.count('apple')) # 0 


print(b.index('strawberry'))  # 0  

print(b.index(1))  # 3   
\'''
print(b.index('apple'))      #print(b.index('apple'))
                             #ValueError: tuple.index(x): x not in tuple
\'''
'''


    # 0     1     2          3 
t = [100 , 200 , 300 ,  [ 10 , [20 ,30, 50 , 70]] ] 
                                 #  0            1
print(t[-1][1][2])                 # [ 10 , [20 ,30, 50 , 70]]


# 50


#EXERCISES 
#      0     1     2     3     4     5     6                      7 
t = [ 100 , 200 , 300 , 400 , 500 , 600 , 700 , [100 , 5 , 6 , 5 , 4 , ["a",'b','c'] ] ]

#OUTOUT = b 


t[-1]
t[7] 
# 0    1   2   3   4         5 
[100 , 5 , 6 , 5 , 4 , ["a",'b','c'] ]


t[-1][5]
t[7][5] 
# 0   1   2 
["a",'b','c']  


t[-1][5][1]
t[7][5][1]  

print(t[-1][5][1])   #b 

