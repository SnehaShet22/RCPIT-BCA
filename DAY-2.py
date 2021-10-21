"""

void main()
{
int a , b
for(i=0;i<=1;i++);    \\
{

}
}
""" 
'''
a=1
b=2 
if a>b :
    print("jhh")
    print()

#this is a comment 
'''
'''

#VARIABLE
'''
'''
x=5 
y= 'john'
print(x)
print(y)
'''
'''
x=4 
x= "sally"
print(x)


# TYPE CASTING
x= 5.89 
a = int(x) 
print(a)         # 5

x= 5
a = float(x) 
print(a)      #5.0

x= 5 
a= str(x)

print(a)

x= '8654645'
a=int(x)
b=float(x)

print(a,b)

x= 45465.0

print(type(x))



# variable can start with _ , alphabet a-z , A-Z
# variable can not start with digits 0-9
#variable cannot be any  keyword , RESERVED WORDS 
# it can't have space between them


#my var 

myvar=0 
my_var = 2
_my_var = 1
myVar = 3
MyVar = 4 
MYVAR = 5 
my_var2 = 6 

#ILLEGAL VARIABLE NAMES
"""
2myvar = 0 
my-var = 0 
my var =0 
"""

x , y , z = "orange" , 'mango' , 'apple'
print(x)
print(y)
print(z)


x = y = z = 'orange'
print(x)
print(y)
print(z)  

print ( x , y , z) # single line print

x , y , z = "orange" , 'mango' , 'apple'
print("HELLO STUDENTS")
print("these are your favorite fruits :", x, y , z )
print("these are your favorite fruits :"+ x + y + z )



x = 'chocolate '
y= 'milkshake'
z= x + y 
print(z)     #chocolatemilkshake  #chocolate milkshake by using space 



x = 'chocolate '
y=  '2'  
z= x + y 
print(z)       #CANNOT ADD INT WITH STRING  CONVERT INT TO STRING  

# COMPLEX NO = A + iB 



x, y  = 5 , 10  

print("addition : " ,x + y)               # 15  10+5
print("subtraction : " ,x - y)            #5-10 -5 
print("multiplication : " ,x * y)         # 50
print("division : " ,x / y)               # 0.5   : quotient
print("Exponentiation : " ,x **  y)       # 5 raised to 10 (5*5*5 ... 10 times)
print("Floor division : " ,x // y)        # 0 
print('modulus :' , x % y)                # 5 : remainder         

'''
'''
    0      = quotient  
   ____
10)   5
-----------
       5    = remainder
      


'''
'''
x = 2
print (x) 

x += 3       #x = x+3 
print(x) 

x -= 2       #x = x-2 
print(x) 

x *= 3       #x = x * 3 
print(x) 

x /= 2       #x = x/2 
print(x) 

x %= 3       #x = x % 3 
print(x) 

x //= 2       #x = x//2 
print(x) 

x **= 3       #x = x ** 3 
print(x) 

x = 5 
y = 10 

if x is not 5 :
    print(" yes it is true")
else:
    print("it is not true")  


a = [1 , 2 , 3 , 4]

if 1 not in a:
    print("1 is present")
else:
    print("it is not true")  


'''

                        #0 1 2 3 4 5 6 7 8 9 10
s = "HELLO WORLD"       #H E L L O  W O R L D
                        #                    -1 
print ( s[6])
print(s[3])
print(s[-1])   # -1 will return the last value 
print(s[10])


# SLICING 

print (s[2:5])      # python excludes the last element in range 

# ( start :  index of element +1 )

