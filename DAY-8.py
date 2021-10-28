# IF ELSE LOOP 

'''
CHECK IF EQUAL A==B
CHECK IF NOT EQUAL  A!=B
        LESS THAN   A<B 
        GREATER THAN  A>B 
        LESS THAN EQUAL TO  A<=B
        GREATER THAN EQUAL TO  A>=B 
'''
'''

a = 33 
b = 200 

if a > b :                       #condition false
    print("a is greater than b") 
    print(a)
else :
    print("b is greater than a ")
    print(b)  


\'''
a = 33 
b = 200 

if a > b :                       
print("a is greater than b") #IndentationError: expected an indented block
print(a)

\''' 

# ELIF IS SAME AS ELSE-IF

a = 33
b = 33 

if a > b :
    print("a is greater than b")
elif a==b:                         #a is equal to b
    print("a is equal to b")   
else:
    print("b is greater than a") 


#shortcut  if you have only one statement after condition 

a , b = 7 , 6

if a > b :  print("a is greater") 
elif a==b : print("a is equal")
else : print(b) 


# short hand if else 
a , b =2 , 330 

print(a) if a>b else print(b)  


a = 200 
b = 33 
c = 500 
# AND KEYWORD 
if a > b and c > a : 
    print("both condition are true")  
else:
    print("either both or one condition is false")

# OR KEYWORD 
if a > b or c > a : 
    print("either both or one condition is true")  
else:
    print("both condition are false")  



x =41 

if x>10 :                                             #above 10
                                                      #and also above 20
    print("above 10")
    if x>20 :
        print("and also above 20")
    else:
        print("but not above 20")



# while  
# initialize i  then condition then increment i if you dont increment i you will face infinite loop  

i = 1                                   
while i < 6 : 
    print(i)
    i += 1       

\'''
1
2
3
4
5
\''' 

# break statement 
i = 1 
while i < 6 :        #  1  2  3 
    print (i) 
    if i == 3 :
        break 
    i += 1 

\'''
1
2
3
\''' 


# continue statement 

i = 0 
while i < 6 :
    i += 1       # 1  2  3  4  5 6 
    if i == 3 :
        continue 
    print(i)      # 1 2 4 5 6  
      


# FOR LOOP 
         #                         i 
fruits = [ 'apple' , 'banana' , 'cherry']

# fruits[0]



for i in fruits:    
    print (i)   # apple   banana    cherry 

# for (i = 0 ; i< 3 ; i++ )  


fruits = [ 'apple' , 'banana' , 'cherry']
for i in range(0 , len(fruits) ) :  # for i in range (len(fruits)):      for i in range (3)
    print(fruits[i])                        # range (start , end+1 )




         #   0           1          2
fruits = [ 'apple' , 'banana' , 'cherry']
for i in range(0 , 2 ) :  # range (start , end+1 )
    print(fruits[i])  


for i in range (6) :   # starting parameter by default 0 (0 , 6)
    print(i)    


for i in range (2 , 6) :    
    print(i)  

# (start , end , count )   default value ( 0 , end , 1)

for i in range ( 0 , 11 , 2):    
    print(i)                  # 0 2 4 8 10 



for i in range ( 0 , 5):
    print(5 * i)



for i in range (6):
    for j in range (i+1): 
        print("*",end=" ")
    print("\r")
    


s = 'Sonal'  
for i in s : 
    print (i)


s = '1254886'  
for i in s : 
    print (i) 


# print table of 2 from 1 to 10  #  2 * 1 = 2
                                 #  2 * 2 = 4 

for i in range (1, 11):
    print (2 * i )  
 

num = 2
for i in range(1,11):
   print(num,"*", i, '=', num*i)


number = 2 
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)


for i in range (1 , 11):
    print ("2 * ", i , '=' , 2 * i )  


i=1
while i<11:
      print(2*i)
      i += 1




input() 
int()


a = int(input("input a number : "))
print(a)  

number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
count = 1    
print ("The Multiplication Table of: ", number)    
while count <= 10:    
    number = number * 1    
    print (number, 'x', count , '=', number * count)    
    count += 1

'''

a=int(input("enter no. ")) 
b=int(input("last limit till what u want to print the table ")) 
i=1
while i<=b:
    print(a,"x",i,"=",a*i)
    i=i+1
