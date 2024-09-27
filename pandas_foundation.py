# PANDAS FOUNDATION
"""
single column = series
NaN = not a number
dataframe.values = numpy
"""
# BUILDING DATA FRAMES FROM SCRATCH
"""
csv'den veri çerçeveleri oluşturabiliriz.
sözlüklerden veri çerçevesi oluşturabiliriz
    zip() yöntemi: Bu fonksiyon, her bir argüman dizisinin veya yineleyicinin
    i'inci öğesini içeren i'inci dizilerden oluşan bir liste döndürür. (tuple)
Yeni sütun ekleme Yayınlama: Yeni sütun oluştur ve tüm sütuna bir değer ata
"""

country = ["spain","France"]
population = ["11","12"]
list_label = ["country","population"]
list_col = [country,population]
zipped = list(zip(list_label,list_col))
data_dict = dict(zipped)
import pandas as pd
df = pd.DataFrame(data_dict)
df

# Add new columns
df["capital"] = ["madrid","paris"]
df

# Broadcasting
df["income"] = 0 #entire column
df

# VISUAL EXPLORATORY DATA ANALYSIS
"""
Plot
Subplot
Histogram: 
    bins: bin sayısı
    range(tuble): binlerin min ve max değerleri
    normed(boolean): normalleştir veya normalleştirme
    cumulative(boolean): kümülatif dağılımı hesapla
"""
data = pd.read_csv('/Users/ndergin/Desktop/Data-Science-Tutorial/pokemon.csv')

# plottin all data
data1 = data.loc[:,['Attack','Defense',"Speed"]]
data1.plot()

# subplot
import matplotlib.pyplot as plt
data1.plot(subplots = True)
plt.show()

# scatter plot  
data1.plot(kind = "scatter",x="Attack",y = "Defense")
plt.show()

# hist plot  
# data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True)
# normed = True ESKİ, density=True normalize etme False deneyebilirsin
 
data1.plot(kind="hist", y="Defense", bins=50, range=(0, 250), density = True)
plt.show()

# histogram  subplot with non cumulative and cumulative
fig, axes = plt.subplots(nrows = 2, ncols = 1)
data1.plot(kind = "hist", y = "Defense", bins = 50, range = (0,250), density = True, ax = axes[0])
data1.plot(kind = "hist", y = "Defense", bins = 50, range = (0,250), density = True, ax = axes[1], cumulative = True)
plt.savefig('graph.png')
plt

# INDEXING PANDAS TIME SERIES
"""
datetime = object
parse_dates(boolean): Transform date to ISO 8601 (yyyy-mm-dd hh:mm:ss ) format
"""

time_list = ["1992-03-08","1992-04-12"]
print(type(time_list[1]))
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object))


# data sette time olmadığı içim ilk beşi seçip ekledim
data2 = data.head()
date_list = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2["date"] = datetime_object
data2 = data2.set_index("date")
data2

print(data2.loc["1993-03-16"])
print(data2.loc["1992-03-10":"1993-03-16"])

# ************** RESAMPLING PANDAS TIME SERIES ***********
"""
    * Yeniden örnekleme (Resampling): Farklı zaman aralıklarında istatistiksel bir yöntemdir.
Frekansı belirtmek için bir string değeri gereklidir, örneğin "M" = ay, "A" = yıl.
    * Aşağı örnekleme (Downsampling): Zaman serisi verilerindeki satırları daha düşük
bir frekansa indirmek, örneğin günlükten haftalığa.
    * Yukarı örnekleme (Upsampling): Zaman serisi verilerindeki satırları daha yüksek
bir frekansa çıkarmak, örneğin günlükten saatliğe.
    *Enterpolasyon (Interpolate): ‘linear’ (doğrusal), ‘time’ (zaman) veya ‘index’ (indeks) gibi
farklı yöntemlere göre değerleri tahmin etmek (enterpole etmek).
"""

data2.resample("A").mean() 

data2.resample("M").mean()

# zaman serisi verilerindeki eksik değerlerin, mevcut verilere dayanarak doldurulmasını sağlar.
# Bu sayede veriler daha anlamlı hale gelir ve analiz için daha iyi bir temel sunar.
data2.resample("M").first().interpolate("linear")

# yada mean ile innterpolate yapabilirsin
data2.resample("M").mean().interpolate("linear")