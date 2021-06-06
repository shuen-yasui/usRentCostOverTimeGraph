import math
import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# Prepare data format using pandas
cYear=2010
allDF=[]
# Cycle through all .csv data between 2010-2019
while cYear<2020:
    # Open csv, and extract data
    if cYear==2018: # specific filters due to csv format
        c_df=pd.read_csv('censusData\\'+str(cYear)+".csv", header=1, usecols=lambda x:"Percent Estimate!!GROSS RENT!!" in x and "$" in x)
    else:
        c_df=pd.read_csv('censusData\\'+str(cYear)+".csv", header=1, usecols=lambda x:"Percent!!GROSS RENT!!" in x and "$" in x)
    c_df=c_df.transpose()
    c_df=c_df.reset_index()
    c_df.columns=["Name","Percent"]
    # sanitize string in name
    c_df['Name']=c_df['Name'].str.replace("Percent!!GROSS RENT!!","")
    c_df['Name']=c_df['Name'].str.replace("Occupied units paying rent!!","")
    c_df['Name']=c_df['Name'].str.replace("Percent Estimate!!GROSS RENT!!","")
    c_df['Name']=str(cYear)+" "+c_df['Name'] # Add year prefix to name
    # append df to allDF array
    allDF.append(c_df)
    cYear+=1
contDF=pd.concat(allDF)
# Create plot using bokeh
sc=ColumnDataSource(contDF)
# Define figure with x range as Name
p=figure(x_range=contDF['Name'], plot_width=1500)
# Define graph annotations
p.title.text="Rent cost catagory by year"
p.xaxis.axis_label="Year and rent cost bracket"
p.xaxis.major_label_orientation = math.pi/4
p.yaxis.axis_label="Percent"
# Create bar graph
p.vbar(x='Name', top='Percent', source=sc, width=0.7)
show(p)
