import math
import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# Prepare data format using pandas
# Open csv, and filter data
df=pd.read_csv('censusData\\2010.csv', header=1, usecols=lambda x:"Percent!!GROSS RENT!!" in x and "$" in x and "Occupied" not in x)
dfTrans=df.transpose()
dfTrans=dfTrans.reset_index()
# define column names
dfTrans.columns=["Name","Percent"]
# sanitize string in name
dfTrans['Name']=dfTrans['Name'].str.replace("Percent!!GROSS RENT!!","")

print(dfTrans)

# Create plot using bokeh
sc=ColumnDataSource(dfTrans)
# Define figure with x range as Name
p=figure(x_range=dfTrans['Name'])
p.vbar(x='Name', top='Percent', source=sc, width=0.70)
# Stylize x axis
p.xaxis.major_label_orientation = math.pi/4
show(p)
