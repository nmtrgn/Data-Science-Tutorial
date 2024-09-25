import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/Users/ndergin/Desktop/Data-Science-Tutorial/pokemon copy.csv')
data.head()
data.info()

#data.corr() fonksiyonunun yalnızca sayısal (numerik) verilerle çalışabilir. select_dtypes metodunu kullanarak yalnızca sayısal sütunları seç
numeric_data = data.select_dtypes(include=[np.number])

#correlation map
f, ax = plt.subplots(figsize=(18, 18))
sns.heatmap(numeric_data.corr(), annot=True, linewidths=.5, fmt='.1f', ax=ax)
plt.show()

data.head(10)

#line plot
# color = color, label = label, linewidth = width of line, alpha = opacity, grid = grid, linestyle = sytle of line
data.Speed.plot(kind = 'line', color = 'g', label ='speed', linewidth = 1, alpha = 0.5, grid = True, linestyle = ':')
data.Defense.plot(color = 'r', label = 'Defense', linewidth = 1, alpha = 0.5, grid = True, linestyle = '-.')
plt.legend(loc = 'upper right')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Line Plot')
plt.show()

#scatter plot
# x = attack, y = defense

data.plot(kind='scatter', x='Attack', y='Defense', alpha=0.5, color='r')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Attack and Defense Scatter Plot')
plt.show()

#Histogram
# binns = number of bar in figure

data.Speed.plot(kind='hist', bins=50, figsize=(15,15))
plt.show()

# clf() = cleanns it up again you can start a fresh
data.Speed.plot(kind='hist', bins=50)
plt.clf()
# we cannot see plot due to clf()

#create dictionary and look its keys and values

dictionary = {'spain':'madrid', 'usa':'vegas'}
print(dictionary.keys())
print(dictionary.values())

#Keys have to be immutable objects like sting, boolen, float, inntegeer or tubles
#List is not immutable
#Keys are unique

dictionary['spain'] = "barcelona"
print(dictionary)
dictionary['france'] = "paris"
print(dictionary)
del dictionary['spain']
print(dictionary)
print('france' in dictionary)
dictionary.clear()
print(dictionary)
#del dictionary 

series = data['Defense']
print(type(series))
data_frame = data[['Defense']]
print(type(data_frame))

# Comparison operator
print(3 > 2)
print(3 != 2)

#Boolen operators
print(True and False)
print(True or False)

# 1) filtering pandas data frame 
x = data['Defense']>200 #There are only 3 pokemon who have higher defense valuee than 200
data[x]

# data['Defense']>200

# 2) Filtering pandas with locical_and
# There are only 2 pokemons who have higher denefse value than 200 annd higher attack value than 100
data[np.logical_and(data['Defense']>200, data['Attack']>100)]

#This is also some with previous code line. Therefore we can also use '&' for filtering
data[(data['Defense']>200) & (data['Attack']>100)]

#stay in loop if condition (i is not equql 5) is true
i = 0
while i != 5:
    print('i is: ',i)
    i +=1
print(i,'is equal to 5')

liste = [1,2,3,4,5]
for i in liste:
    print('i is :', i)
print('')

# Enumerate index and value of liste
# index : value = 0:1, 1:2, 2:3, 3:4, 4:5
for index, value in enumerate(liste):
    print(index,":",value)
print('')

# for dictionaries
# We can use a for loop to access the keys and values of a dictionary. We learned about keys and values in the dictionary section.
dictionary = {'spain':'madrid', 'usa':'vegas'}
for key, value in dictionary.items():
    print(key,":",value)
print('')

# For pandas, we can access the index and values.

for index, value in data[['Attack']][0:1].iterrows():
    print(index,":",value)