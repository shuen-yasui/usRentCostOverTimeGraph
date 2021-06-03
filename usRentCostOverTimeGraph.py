import math
import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# Prepare data format using pandas
# Open csv, and filter data
years=[]
cYear=2010
while cYear<2020:
    if cYear==2018:
        temp_df=pd.read_csv('censusData\\'+str(cYear)+".csv", header=1, usecols=lambda x:"Percent Estimate!!GROSS RENT!!" in x and "$" in x)
    else:
        temp_df=pd.read_csv('censusData\\'+str(cYear)+".csv", header=1, usecols=lambda x:"Percent!!GROSS RENT!!" in x and "$" in x)
    temp_df=temp_df.transpose()
    temp_df=temp_df.reset_index()
    print('censusData\\'+str(cYear)+".csv")
    temp_df.columns=["Name","Percent"]
    # sanitize string in name
    temp_df['Name']=temp_df['Name'].str.replace("Percent!!GROSS RENT!!","")
    temp_df['Name']=temp_df['Name'].str.replace("Occupied units paying rent!!","")
    temp_df['Name']=temp_df['Name'].str.replace("Percent Estimate!!GROSS RENT!!","")
    print(temp_df)
    cYear+=1
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
#show(p)
