# DIAGNOSE DATA for CLEANING

#  Büyük-küçük harf veya kelimeler arasındaki boşluk gibi sütun adı tutarsızlık, eksik veri, farklı dil kirli data örnekleri 

# columns gives column names of features
import pandas as pd

data = pd.read_csv('/Users/ndergin/Desktop/Data-Science-Tutorial/pokemon.csv')
data.columns

# shape gives number of rows and columns in a tuble
data.shape

# info gives data type like dataframe, number of sample or row, number of feature or column, feature types and memory usage
data.info()

# EXPLORATORY DATA ANALYSIS
# value_counts(): Frekans sayıları aykırı değerler: verilerin geri kalanından önemli ölçüde daha yüksek veya daha düşük olan değer
""" * Diyelim ki %75'lik değer Q3'tür ve %25'lik değer Q1'dir.
    * Aykırı değerler Q1 - 1.5(Q3-Q1)'den küçük ve Q3 + 1.5(Q3-Q1)'den
büyüktür. (Q3-Q1) = IQR Specify() metodunu kullanacağız.
Describe metodu şunları içerir:
    * count: number of entries
    * mean: average of entries
    * std: standart deviation
    * min: minimum entry
    * 25%: first quantile
    * 50%: median or second quantile
    * 75%: third quantile
    * max: maximum entry

    What is quantile?
    * Medyan, dizinin ortasındaki sayıdır.
    * The lower quartile, en küçük sayı ile medyan arasındaki medyandır
    * The upper quartile, medyan ile en büyük sayı arasındaki medyanı bulursunuz

"""
import statistics
a = [0, 1, 2, 3, 4, 15]
mean_value = statistics.mean(a)
median_value = statistics.median(a)
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")



# For example lets look frequency of pokemom types
print(data['Type 1'].value_counts(dropna =False))  # if there are nan values that also be counted
# As it can be seen below there are 112 water pokemon or 70 grass pokemon

# For example max HP is 255 or min defense is 5
data.describe() #ignore null entries

# VISUAL EXPLORATORY DATA ANALYSIS

#Box plots: visualize basic statistics like outliers, min/max or quantiles

"""
    # For example: compare attack of pokemons that are legendary  or not
    # Black line at top is max
    # Blue line at top is 75%
    # Green line is median (50%)
    # Blue line at bottom is 25%
    # Black line at bottom is min
    # There are no outliers
"""
data.boxplot(column='Attack',by = 'Legendary')

# TIDY DATA

# Verileri melt() ile düzenliyoruz

# Firstly I create new data from pokemons data to explain melt nore easily.
data_new = data.head()    # I only take 5 rows into new data
data_new

# lets melt
# id_vars = what we do not wish to melt
# value_vars = what we want to melt
melted = pd.melt(frame=data_new,id_vars = 'Name', value_vars= ['Attack','Defense'])
melted
""" pd.melt(...): Bu, pandas kütüphanesinin melt fonksiyonudur.
DataFrame'in geniş formatını uzun formata dönüştürmek için kullanılır.
Özellikle verileri daha kolay analiz etmek veya görselleştirmek için yararlıdır.

frame=data_new: Burada data_new, melt işlemi yapılacak olan DataFrame'dir.
Yani, data_new adındaki DataFrame üzerinde melt işlemi gerçekleştirilecektir.

id_vars='Name': id_vars, melt işleminde eritilmeyecek olan sütunları belirtir.
Yani, bu sütunlar, her bir eritme işleminde korunacak olan sabit (kimlik) sütunlardır.
Bu örnekte, "Name" sütunu eritilmeyecek ve her bir erime işlemine karşılık gelen Pokémon'un adı olarak kalacaktır.

value_vars=['Attack', 'Defense']: value_vars, melt işleminde eritilmesi istenen sütunları belirtir.
Yani, bu sütunlardaki veriler uzun formata dönüştürülecektir. Burada, "Attack" ve "Defense" sütunları eritilmekte
ve bu sütunlardaki değerler bir araya getirilerek daha uzun bir format oluşturulmaktadır.

melted: Sonuç olarak, melt işlemi sonrasında elde edilen yeni DataFrame melted adlı bir değişkene atanır.
Bu yeni DataFrame, "Name" (isim) sütununu koruyarak, "Attack" ve "Defense" sütunlarından elde edilen
değerlerin uzun formatını içerecektir.
"""

# PIVOTING DATA

#Erimenin tersi.

# Index is name
# I want to make that columns are variable
# Finally values in columns are value
melted.pivot(index = 'Name', columns = 'variable',values='value')
melted
# ************************************* CONCATENATING DATA ********************
# We can concatenate two dataframe 

# Firstly lets create 2 data frame
data1 = data.head()
data2 = data.tail()
conc_data_row = pd.concat([data1,data2],axis = 0,ignore_index =True) # axis = 0 : adds dataframes in row
conc_data_row

data1 = data['Attack'].head()
data2 = data['Defense'].head()
conc_data_col = pd.concat([data1,data2],axis =1) # axis = 1 : adds dataframes in column
conc_data_col


# DATA TYPES
"""
5 temel veri türü vardır: nesne(string), boolean, integer, float ve kategorik.
Str'den kategorik veya int'den float'a gibi veri türlerini dönüştürebiliriz
"""

# lets convert object(str) to categorical and int to float.
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')
# As you can see Type 1 is converted from object to categorical
# And Speed ,s converted from int to float
data.dtypes

# ************************** MISSING DATA and TESTING WITH ASSERT ************************


"""
Eksik verilerle karşılaşırsak neler yapabiliriz:
* olduğu gibi bırakın
* dropna() ile bırakın
* fillna() ile eksik değeri doldurun
* mean gibi test istatistikleri ile eksik değerleri dolduru
 Assert statement: programınızın testini bitirdiğinizde açılıp kapanabileceğini kontrol edin

"""

# Lets look at does pokemon data have nan value
# As you can see there are 800 entries. However Type 2 has 414 non-null object so it has 386 null object.
data.info()

# Lets chech Type 2
data["Type 2"].value_counts(dropna =False)
# As you can see, there are 386 NAN value

# Lets drop nan values
data1 = data   # also we will use data to fill missing value so I assign it to data1 variable
data1["Type 2"].dropna(inplace = True)  # inplace = True means we do not assign it to new variable. Changes automatically assigned to data
# So does it work ?

#  Lets check with assert statement
# Assert statement:
assert 1==1 # return nothing because it is true

# In order to run all code, we need to make this line comment
# assert 1==2 # return error because it is fa

assert data['Type 2'].notnull().all() # returns nothing because we drop nan values
data["Type 2"].fillna('empty',inplace = True)

assert  data['Type 2'].notnull().all() # returns nothing because we do not have nan values

# # With assert statement we can check a lot of thing. For example
# assert data.columns[1] == 'Name'
import numpy as np
data['Speed'] = data['Speed'].astype('int')
# assert data.Speed.dtypes == np.int
