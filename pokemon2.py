import pandas as pd             #imports pandas which allows data to be put into organized tables
import bokeh                    #imports bokeh which allows data to be interpreted indivisually
from bokeh.charts import Bar, output_file, save         #creates the setting and place for the data
df = pd.read_csv('Pokemon.csv')                             #accesses the data and converts it into a data frame

p = Bar(df[0:13],                                   #accesses information from pokemon # 1-9
                'Name',                                #x axis is formatted alphabetically by name       
                group='Type 1',                     #same type pokemon are colored the same
                values='HP',                        #y axis is formatted by the HP info
                legend='top_center',                #position of the legend
                title='HP vs Evolutions')           #title of graph
                


output_file('pokemon_evolutions.html')              #puts a name to the file and makes into a visual

save(p)                                         #saves/creates the file
