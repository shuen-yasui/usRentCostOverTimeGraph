import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

df=pd.read_csv('censusData\\2010.csv', header=1, usecols=lambda x:"Percent!!GROSS RENT!!" in x and "$" in x and "Occupied" not in x)
df2=df.transpose()
df2=df2.reset_index()
df2.columns=["Name","Percent"]
print(df2)
for row in df2.iterrows():
    print(row)
sc=ColumnDataSource(df2)
p=figure()
p.vbar(x='index', top='Percent', source=sc, width=0.70)
show(p)
