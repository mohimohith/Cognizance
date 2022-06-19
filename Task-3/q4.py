import pandas as pd
series = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
newSeries = series.map(lambda x: x[0].upper() + x[1:])
print("\nResulting Series :")
string=""
for i in newSeries:
    string+=i+" "
print(string)