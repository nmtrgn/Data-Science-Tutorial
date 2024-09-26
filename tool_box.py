# USER DEFINE FUNCTION

# tuple

def tuple_ex():
    t = (1,2,3)
    return t
a,b,c = tuple_ex()
print(a,b,c)

#SCOPE

x = 2
def f():
    x = 3
    return x
print(x) 
print(f())

x = 5
def f():
    y = 2*x
    return y
print(f())

# How can we learn what is built in scope
import builtins
dir(builtins)

# NESTED FUNCTION

def sqaure():
    def add():
        x = 2
        y = 3
        z = x + y 
        return z
    return add()**2
print(sqaure())

# DEFAULT and FLEXIBLE ARGUMENTS

# default arguments
def f(a, b = 1, c = 2):
    y = a + b + c
    return y
print(f(5)) # 5 + 1 + 2 = 8 default değerler
print(f(5,4,3)) # 5 + 4 + 5 = 14 

# flexible arguments *args

def f(*args):
    for i in args:
        print(i)
f(1)
print("")
f(1,2,3,4)

def f(**kwargs):
    for key, value in kwargs.items():
        print(key, " ", value)
f(country = 'spain', capital = 'madrid', population = 123456)

# LAMBDA FUNCTION

square = lambda x: x**2     # where x is name of argument
print(square(4))
tot = lambda x,y,z: x+y+z   # where x,y,z are names of arguments
print(tot(1,2,3))

# ANONYMOUS FUNCTİON

number_list = [1,2,3]
y = map(lambda x:x**2,number_list)
print(list(y))

# ITERATORS

name = "ronaldo"
it = iter(name)
print(next(it))
print(*it) 

# zip example
list1 = [1,2,3,4]
list2 = [5,6,7,8]
z = zip(list1,list2)
print(z)
z_list = list(z)
print(z_list)

un_zip = zip(*z_list)
un_list1,un_list2 = list(un_zip) # unzip returns tuple
print(un_list1)
print(un_list2)
print(type(un_list2))

# LIST COMPREHENSİON
# **** veri analizi içi sık kullanılır ****
# listeleri tek bir satırda oluşturmak için döngüleri daraltma
# Example of list comprehension

num1 = [1,2,3]
num2 = [i + 1 for i in num1 ] # iterable object
print(num2)

# Conditionals on iterable
num1 = [5,10,15]
num2 = [i**2 if i == 10 else i-5 if i < 7 else i+5 for i in num1]
print(num2)

# pokemon data set ile örnek çalışma
import pandas as pd

data = pd.read_csv('/Users/ndergin/Desktop/Data-Science-Tutorial/pokemon.csv')
threshold = data['Speed'].mean()
print("threshold", threshold)
data["speed_level"] = ["high" if i > threshold else "low" for i in data.Speed]
data.loc[:10,["speed_level","Speed"]]
