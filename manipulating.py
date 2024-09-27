# MANIPULATING DATA FRAMES WITH PANDAS

"""
INDEXING DATA FRAMES 
    Indexing using square brackets
    Using column attribute and row label
    Using loc accessor
    Selecting only some columns
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# read data
data = pd.read_csv('/Users/ndergin/Desktop/Data-Science-Tutorial/pokemon.csv')
data= data.set_index("#")
data.head()

# indexing using square brackets
data["HP"][1]

# using column attribute and row label
data.HP[1]

# using loc accessor
data.loc[1,["HP"]]

# Selecting only some columns
data[["HP","Attack"]]

"""
SLICING DATA FRAME
    Difference between selecting columns
        Series and data frames
    Slicing and indexing series
    Reverse slicing
    From something to end
"""
# Difference between selecting columns: series and dataframes
print(type(data["HP"]))     # series
print(type(data[["HP"]]))   # data frames

#Slicing and indexin series
data.loc[1:10,"HP":"Defense"]

# Reverse slicing 
data.loc[10:1:-1,"HP":"Defense"] 

# From something to end
data.loc[1:10,"Speed":] 

# ******************** FILTERING DATA FRAMES
#Boolean serileri oluşturma Filtreleri birleştirme Sütun tabanlı filtreleme Diğerleri

# Creating boolean series
boolean = data.HP > 200
data[boolean]

# Combining filters
first_filter = data.HP > 150
second_filter = data.Speed > 35
data[first_filter & second_filter]

# Filtering column based others
data.HP[data.Speed<15]

# ******************** TRANSFORMING DATA
# plain python fonk.
# Lambda fonksiyonu: her elemana keyfi Python fonksiyonunu uygulamak
# Diğer sütunları kullanarak sütunu tanımlama

# Plain python functions
def div(n):
    return n/2
data.HP.apply(div)

# Or we can use lambda function
data.HP.apply(lambda n : n/2)

# Defining column using other columns
data["total_power"] = data.Attack + data.Defense
data.head()



# INDEX OBJECTS AND LABELED DATA

print(data.index.name) # indexin adı
data.index.name ="index_name" # indexin adını değiştir
data.head()

#overwrite index 
#  eğr istersem index 
data.head()
data3 = data.copy()
data3.index = range(100,900,1)
data3.head()

# HIERARCHICAL INDEXING
# lets read data frame one more time to start from beginning
data = pd.read_csv('/Users/ndergin/Desktop/Data-Science-Tutorial/pokemon.csv')
data.head()
# As you can see there is index. However we want to set one or more column to be index

# Setting index : type 1 is outer type 2 is inner index
data1 = data.set_index(["Type 1","Type 2"]) 
data1.head(100)
# data1.loc["Fire","Flying"] # howw to use indexes

# PIVOTING DATA FRAMES

dic = {"treatment":["A","A","B","B"],"gender":["F","M","F","M"],"response":[10,45,5,9],"age":[15,4,72,65]}
df = pd.DataFrame(dic)
df

# pivoting
df.pivot(index="treatment",columns = "gender",values="response")

# STACKING and UNSTACKING DATAFRAME
"""
* deal with multi label indexes
* level: position of unstacked index
* swaplevel: change inner and outer level index position
"""

df1 = df.set_index(["treatment","gender"])
df1
# lets unstack it

# level determines indexes
df1.unstack(level=0)
df1.unstack(level=1)

# change inner and outer level index position
df2 = df1.swaplevel(0,1)
df2

# MELTING DATA FRAMES

# df.pivot(index="treatment",columns = "gender",values="response")
pd.melt(df,id_vars="treatment",value_vars=["age","response"])

#CATEGORICALS AND GROUPBY

# We will use df
df

# according to treatment take means of other features
df.groupby("treatment").mean()   # mean is aggregation / reduction method
# there are other methods like sum, std,max or min

# we can only choose one of the feature
df.groupby("treatment").age.max() 

# Or we can choose multiple features
df.groupby("treatment")[["age","response"]].min() 
df.info()
