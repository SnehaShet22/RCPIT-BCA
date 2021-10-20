'''
void main()
{
int a , b , temp;
a = 6;
b = 5 ;

temp = a ;
a=b ;
b=temp;

printf("%d,%d", &a , &b)
}


'''

a = 5
b = 6
a, b = b, a 
print( a , b ) 

# PYTHON USES INTREPRETER 


print('HELLO WORLD!')
print("HELLO WORLD!") 

if a>b:
    print("hoo")

elif a==b:
    print("hhgh")

else:
    print("hvjv")

'''
for (i=0; i<=10 ; i++)
{

    printf("%d",i)
}
'''
for i in range(0,11):
    print (i)
    print("hii")
print(i)