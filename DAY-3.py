
#STRING 
"""
print(" HELLO ")
print(' HELLO ') 


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


"""  
'''

for x in "banana":
    print(x) 
''
b
a
n
a
n
a
''

s = "HELLO WORLD"  

print (len(s))     #11 

if "HELLO" in s :
    print("YES")
else:
    print('NO!')  



                        #0 1 2 3 4 5 6 7 8 9 10
s = "HELLO WORLD"       #H E L L O   W O R L D
                       #-11-10-9-8-7-6-5-4-3-2-1 

print (s[2:5])   #LLO                            i=2
                                                #while i<5:
                                                #    print ( s[i] ) 
                                                #    i+=1 
print(s[6:9])  

  # python excludes the last element in range 

#[start :  last element +1 ]  

print(s[9:11]) 

print(s[:])    # [start : len(string)]

print(s[2:])  

print(s[:9]) 


                        #0 1 2 3 4 5 6 7 8 9 10
s = "HELLO WORLD"       #H E L L O   W O R L D
                       #-11-10-9-8-7-5-4-3-2-1 
print(s[-5:-2])

i=-5                    # -5  -4  -3  -2
                         # w   o   r   ignored 
while i>-2:
    print ( s[i] ) 
    i+=1 


s = 'Hello world' 

b= s.upper()    #HELLO WORLD
print(b)

c= s.lower()    #hello world 
print(c)

n =  "         SONAL      "
print(n)
c=n.strip(" ") #remove spaces from start and end not the middle ones
print(c)


n =  "ssssssssssss  sss  SONAL  sss  ssssssssssss"
print(n)
print(n.strip("s"))   



s = 'Hello world' 
print ( s.replace('w','S')  )  #Hello Sorld
print ( s.replace('world','Students')  )  #Hello Students

print(s.replace("r",' '))   #Hello wo ld 

print ( s.replace("r", '1' ))   #Hello wo1ld

print(s.replace("s","x"))    #Hello world   it will return original string if the letter is not present in the string 

print(s.replace("H",'z'))   #zello world   


s = 'Hello,world'                                       #      Hello world' 
g = s.split(',')   # returns a list   ['Hello', 'world']
print(g)

k = s.split('l')                                # He   o,wor   d' 
print(k)            #['He', '', 'o,wor', 'd']   



a = 'HELLO' 
b = 'WORLD' 

c= a +' '+ b   #HELLO WORLD

print(c)
#can only concatenate str (not "int") to str
d= '1' 
print(c+d)  #HELLO WORLD1 

#FORMAT METHOD 

age = 20 
txt = "My name is Sejal , and I am {} years old".format(age)
print(txt)    #My name is Sejal , and I am 20 years old  


quantity = 3 
item = 56 
price = 500 
my_order = " I want {2} pieces of item {1} for {0} rupees"
                      #  0      1       2 
print(my_order.format(price , item , quantity))  # I want 3 pieces of item 56 for 500 rupees  

'''

age = "SONAL IS MY GOOD FRIEND"
txt = "My name is Sejal , and {}".format(age)
print(txt)    #My name is Sejal , and SONAL IS MY GOOD FRIEND


#ESCAPE CHARACTERS 

#txt = "WE ARE THE SO-CALLED "VIKINGS" FROM THE NORTH." 

txt1 = 'WE ARE THE SO-CALLED "VIKINGS" FROM THE NORTH.' 

txt2 = "WE ARE THE SO-CALLED 'VIKINGS' FROM THE NORTH." 

txt3 = "WE ARE THE SO-CALLED \"VIKINGS\" FROM THE NORTH."  

print(txt1)
print(txt2)
print(txt3) 

txt3 = "WE ARE \bTHE \n SO-CALLED \"VIKINGS\" FROM THE \t NORTH."  
print(txt3) 

