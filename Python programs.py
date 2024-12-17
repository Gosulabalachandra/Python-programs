"""num=int(input("enter the no of rows:"))
for i in range(1,num+1):
    for j in range(1,i):
        print("*",end="")
    print()

n=5
for i in range(1,n+1):
    print(" "*(n-i)+"* " *i)



n=4
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
        num+=1
    print()

for i in range(1,11):
    if i==5:
        continue
    if i==11:
        break
    print(i)


l="balu","nari","mahe"
s=list(str(l))
print(s)


def pal(num):
    if num==num[::-1]:
        print("The given is palindrom")
    else:
        print("The given is not pallindrom")
num=input("Enter any number:")
r=pal(num)

sum=lambda i,j:i+j
print(sum(10,20))


#fibonaaci series

def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        result=fib(n-2)+fib(n-1)
n=input("Enter a number:")
for x in n:
    print(x)


l=[1,2,3,4,5,6]
for x in l:
      l1=lambda x:x*x
print(l1)

def even(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
num=int(input("Enter any number:"))
r=even(num)


t=("apple","banana","mango","orange")
s="-".join(t)
print(s)


s=input("Enter any one:")
print(' '.join(reversed(s)))



s="acbabsabbsdbadbs"
print(s.count("b"))



s="python is a very esay to learn"
print(s.find("n"))

fname=input("Enter any name:")
lname=input("Enter any name:")
username=fname+lname
print("User name is :",username)
email=username+"@gmail.com"
print( "E-mail is:",email)


spwd="Balu@14321"
upwd=input("Enter your password : ")
print(spwd==upwd)

#simple interest
p=int(input("Enter amount:"))
t=float(input("Enter time:"))
r=float(input("Enter rate :"))
interest=p*t*r/100
print("Your interest is :",interest)




f=[1,2,3,4,5,6,7,8,9]
print(10 not in f)


import calendar
y=int(input("Enter year :"))
m=int(input("Enter month :"))
result=calendar.month(y,m)
print(result)


#sum of n nutural numbers


n=int(input("Enter any number:"))
sum=0
i=1
while i<=n:
    sum+=i
    i=i+1
print(sum)


n=int(input("Enter any number:"))
while n%5==0:
        print("Diviible by 5")
else:
   print("Not Divisible by 5")
   n+=1
"""
#dictionary
"""p=dict(
    b=1,
    n=2,
    m=3
    )

print(p.keys())


i=2
n=int(input("Enter any number :"))
if n%2==0:
    print("Even")
else:
    print("Odd")

s=set()
print(type(s))

n1=input("Enter any number;")
print(n1.split())


# Multiplication
n=int(input("Enter any number :"))
for i in range(1,11):
    print(n, "*",i,"=",n*i )


seta ={1,2,3,4,5}
seta.remove(1)
print(seta)


cart=[]
n=int(input("Enter u want to add items:"))
for i in range(n):
      item=input("Enter item into the cart")
      cart.append(item)
print(cart)


#inhritance
class product:
   def __init__(self,name,price):
                 self.name=name
                 self.price=price
   def get_data(self):
      self.name=input("Enter name of the product:")
      self.price=int(input("Enter the price of the product:"))
   def put_data(self):
      print(self.name)
      print(self.price)
class digitalproduct(product):
      def __init__(self,link):
              self.link=link
      def get_link(self):
              self.link=input("Enter product link:")
      def put_ink(self):
              print(self.link)
ebook=digitalproduct("")
ebook.get_data()
ebook.get_link()


#Lamda function
r=(lambda x:x**2)(2)
print(r)


#Map Function

n=[1,2,3,4,5]
def square(x):
      return x*x
r=list(map(square,n))
print(r)


l=["1","2","3","4","5"]
print(l)
l1=list(map(int,l))
print(l1)

"""


"""n=input("Enter any values:")
for i in range(1,n):
    r=reversed(i)
print(i,end=" ")
n=int(input("Enter any value:"))
for i in range(1,n):
        print(i,end=" ")
        n+=1
print(reversed(n))

class product:
        
        def __init__(self,name,price):
                self.name=name
                self.price=price
        def summer_discount(self):
                self.price=self.price-self.price*5/100
p1=product("Tshirt","300")
print(p1.name)
print(p1.price)
p1.summer_discount()
print(p1.price)


#Method Overriding


class Food:
        def kali(self):
                print("food")
class Fruit(Food):
        def kali(self):
                print("fruit")
apple=Fruit()
print(apple.kali())

#instance Method
class stud:
        def __init__(self,name):
                self.name=name
        def balu(self):
                print(f"my name is {self.name}")
stud1=stud("Balu")
stud1.balu()


#Static

class stud:
        def add(a,b):
                print(a+b)
stud.add(2,3)


#2 Static method inside a class
class Circle:
        @staticmethod
        def area(r):
                return 3.14*r*r
        @staticmethod
        def circumference(r):
                return 2*3.14*r
        
a=Circle.area(10)
print(a)
c=Circle.circumference(10)
print(c)


#Prime numbers
numbers=[2,3,4,5,6,7,8,9,10,11]
def is_prime(n):
        if n<2:
                return False
        for i in range(2,n):
                if n%2==0:
                        return False
        return True
prime_number=list(filter(is_prime,numbers))
print(prime_number)



#fibonacci series
def fibonacci(n):
        if n<=0:
                return []
        elif n==1:
                return [0]
        elif n==2:
                return [0,1]
        else:
                fib_seq=[0,1]
                fib_seq.extend(map(lambda i:fib_seq[i-1]+fib_seq[i-2],range(2,n)))
        return fib_seq
fib_sequence=fibonacci(10)
print(fib_sequence)




class Product:
        def __init__(self,name,price):
                self.name=name
                self.price=price
        def get_data(self):
                self.name=input("Enter name:")
                self.price=input("Enter a price:")
        def put_data(self):
                print(self.name)
                print(self.price)
p1=Product()
p1.get_data()
p1.put_data()

"""
#constructer inheritance
"""

class Parent:
        def __init__(self):
                self.balance=30000
        def display_balance(self):
                   print(f"Parent balance is: {self.balance}")
        
class Child(Parent):
        pass
mike=Child()
mike.display_balance()

   
#pass in python
def myfun():
        pass
print("Balu")
       
myfun()

for i in range(1,11):
        if i==6:
                break
        print(i)
        if i==8:
                continue
        


number=4
print("Even" if number%2==0 else "Odd")


#join function in python

f=("apple","banana","ornage","sapota")
j=",-".join(f)
print(j)


s=input("Enter any string:")
#print(" ".join(reversed(s)))
print(reversed(s))


#polindrom or not

s=input("Enter any string:")
t=s[::-1]
print(s.count("a"))
print(s.upper())
print(s.title())
print(s.tell())
#print("reverse string is :",t)
if s==t:
    print("polindrome")
else:
    print("Is not polindrome")


#Object creation in python
class Dog():
    def bark(self):
        print("Woof")
        my_dog==Dog()
        my_dog.bark()

#inheritance
class P():
    def __init__(self,name):
        self.name=name
    def sound(self):
        return "Some sound"
class Childclass(P):
    def _init_(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
             return "Bark"


#2
class P:
    def m1(self):
        print("Parent class")
class C(P):
    def m2(self):
        print("Child class")
class D(C):
    def m3(self):
        print("subchild class")
        c=c()
        c.m1()
        c.m2()
        c.m3()

class A:
    def m1(self):
        print(a)
    def m1(self,a,b):
        print(a+b)
    def m1(self,name,age,a):
        print("Name is :",name)
        print("Age is:",age)
        print(a)
        a=A()
        a.m1("Balu",23,10)

#swaping vlues
a=int(input("Enter a vlaue:"))
b=int(input("Enter b vlaue:"))
#temp=b
#b=a
#a=temp
b=a+b
a=b-a
b=b-a
print("Before swapping a value is :",a)
print("After swapping b value is :",b)

#Calculator
n1=int(input("Enter n1 number:"))
n2=int(input("Enter n2 number:"))
operator=input("Enter u want operator:")
if operator=="+":
    print(n1+n2)
elif operator=="-":
    print(n1-n2)
elif operator=="*":
    print(n1*n2)
elif operator=="/":
    print(n1/n2)
else:
    print("Invalid operator")
    
#String cancadination
s1="Bala"
s2="Chandra"
print(s1+s2)
print(len(s2))
print(s2.count("a"))

#count the no of ovels in a string
s=input("Enter any string :")
a=s.count("a")
e=s.count("e")
i=s.count("i")
o=s.count("o")
u=s.count("u")
print(f'No of vowels in given string:{a+e+i+o+u}')

s=input("Enter any string:")
reverse=s[::-1]
if reverse==s:
    print("The given string is polindrom")
else:
    print("The given string isn't palindrom")

"""
def pal_srting(s):
    s=input("Enter a string:")
    r=reversed(s)
if s==r:
    print("plindrome")
else:
    print("Is not polindrome")
    






























































































































