# WILL RETURN TRUE IF NO ITEMS IN SET X IS PRESENT IN SET Y 
#Because  if they have common element , its not a disjoint
'''
x = {"apple", "mango", " banana"}
y = {"google","microsoft","apple"}  

z = x.isdisjoint(y)   #False 

print(z)  


#SUBSET RETURN TRUE IF ALL ITEMS IN SET X ARE PRESENT IN SET Y 

x= {'a','b','c'}
y = {'f','g','h','a','b','c'}

z = x.issubset(y)    #True
print(z) 


#SUPERSET RETURN TRUE IF ALL ITEMS IN SET Y ARE PRESENT IN SET X 

x = {'f','g','h','a','b','c'} 
y = {'a','b','c'}
r= {"a",'b','x'}
z = x.issuperset(y)    #True
g = x.issuperset(r)    #False
print(z) 
print(g) 



# DICTIONARY   key:value (key:value)=item   

l =[1,2,3,4]

this_Dict = {'brand' : 'Ford', 'model' : "Mustang" , 'year': 1964  }

this_Dict = {'brand' : 'Ford',
             'model' : "Mustang" , 
             'year': 1964  }  

#does not allow duplicates  

this_Dict = {'brand' : 'Ford',
             'model' : "Mustang" , 
             'year': 1964 ,
             'year':2000 }  

print(this_Dict)    #{'brand': 'Ford', 'model': 'Mustang', 'year': 2000}
\'''
this_Dict = {'brand' : 'Ford',
             'model' : "Mustang" , 
             'year': 1964 ,
             'year':'Ford' }  

print(this_Dict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 'Ford'}  
\'''

print(this_Dict['model'])   #Mustang  

print(this_Dict['brand'])   #Ford 

#print(this_Dict['price'])   #KeyError: 'price'  if key not present  

print(len(this_Dict))        #3 



this_Dict = {'brand' : 'Ford', 'model' : "Mustang" , 'year': 1964  }


this_Dict = {'brand' : 'ODI',
             'model' : "Mustang" , 
             'year': 1964  ,
             'colors': ['red','blue','green']
             }  

print(type(this_Dict))   #<class 'dict'> 

#ACCESSING ELEMENTS 


print(this_Dict['model'])   #Mustang  

print(this_Dict['brand'])   #Ford  


#GET get()  

x = this_Dict.get('model')   #Mustang  
print(x)

#FOR ACCESSING ONLY KEY  key()

x = this_Dict.keys()
print(x)               #dict_keys(['brand', 'model', 'year', 'colors']) 


#FOR ACCESSING ONLY VALUE value()

x = this_Dict.values()
print(x)               #dict_values(['Ford', 'Mustang', 1964, ['red', 'blue', 'green']]) 
                       #dict_values(['ODI', 'Mustang', 1964, ['red', 'blue', 'green']])


#FOR ACCESSING BOTH KEY AND VALUE  items()

x = this_Dict.items()
print(x)              #dict_items([('brand', 'ODI'), ('model', 'Mustang'), ('year', 1964), ('colors', ['red', 'blue', 'green'])])      



#CHECK IF KEY IN DICTIONNARY 

if 'model' in this_Dict:
    print('yes')          #yes 
else:
    print("no") 


# CHANGE VALUES IN DICTIONARY  / ADD ITEMS


this_Dict = {'brand' : 'ODI',
             'model' : "Mustang" , 
             'year': 1964  ,
             'colors': ['red','blue','green']
             }  

this_Dict['year'] = 2000 
print(this_Dict)              #{'brand': 'ODI', 'model': 'Mustang', 'year': 2000, 'colors': ['red', 'blue', 'green']}

this_Dict['milage'] = 250

print(this_Dict)              #{'brand': 'ODI', 'model': 'Mustang', 'year': 2000, 'colors': ['red', 'blue', 'green'], 'milage': 250}



#UPDATE DICTIONARY  update() (can add new key:value or change existing one)

this_Dict.update({'cost': '5 lakhs'})  # {'brand': 'ODI', 'model': 'Mustang', 'year': 2000, 'colors': ['red', 'blue', 'green'], 'milage': 250, 'cost': '5 lakhs'}
print(this_Dict)   


# REMOVING ITEMS 

#pop 

this_Dict.pop('cost')
print(this_Dict)       #{'brand': 'ODI', 'model': 'Mustang', 'year': 2000, 'colors': ['red', 'blue', 'green'], 'milage': 250}


#popitem()   removes last element

this_Dict.popitem() 
print(this_Dict)           #{'brand': 'ODI', 'model': 'Mustang', 'year': 2000, 'colors': ['red', 'blue', 'green']}

#this_Dict.pop()     #pop expected at least 1 argument, got 0  error
#print(this_Dict)

del this_Dict['colors']        #{'brand': 'ODI', 'model': 'Mustang', 'year': 2000}
print(this_Dict)           

#clear()
this_Dict.clear()
print(this_Dict)     #{}  empty dictionarty



#LOOPING THROUGH DICTIONARY 
this_Dict = {'brand' : 'ODI',
             'model' : "Mustang" , 
             'year': 1964  ,
             'colors': ['red','blue','green']
             }  
for x in this_Dict:
    print(x)  

#brand
#model   it prints key 
#year
#colors
  

for x in this_Dict:
    print(this_Dict[x])         #this_Dict[x]
#ODI
#Mustang
#1964
#['red', 'blue', 'green'] 

# FOR ITEMS
for x in this_Dict.items():
    print(x)

# FOR KEYS
for x in this_Dict.keys():
    print(x)

# FOR VALUES
for x in this_Dict.values():
    print(x)

#copy()


d1 = {'name':"Sonal"}
d2 = d1 

print(d1,d2)    #{'name': 'Sonal'} {'name': 'Sonal'}

d1['name']='Sejal'
print(d1,d2)    #{'name': 'Sejal'} {'name': 'Sejal'}  


d2=d1.copy() 
print(d2)     #{'name': 'Sejal'} 

d1['name']= 'Sonal'
print(d1)  #{'name': 'Sonal'}
print(d2)  #{'name': 'Sejal'} 
'''

# another method 

d1 = {'name':"Gavrav"} 
d2 = dict(d1)
print(d1,d2)  #{'name': 'Gavrav'} {'name': 'Gavrav'}

d1['name']='raghav'

print(d1,d2)   #{'name': 'raghav'} {'name': 'Gavrav'} 

myfamily = {
    'child1': { 'name':'Sonal'

              },

    "child2":{
        'name':"sejal"
             },

    "child3": {
        "name": 'Mayuri'
              }
    

}


child1= { 'name':'Sonal'}

child2= {'name':"sejal"}

child3= {"name": 'Mayuri'} 

myfamily= {'child1': child1 ,
           'child2': child2 ,       
           'child3': child3 } 



    