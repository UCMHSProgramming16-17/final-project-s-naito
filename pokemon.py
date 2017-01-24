import pandas as pd             #imports pandas which allows data to be put into organized tables
import bokeh                    #imports bokeh which allows data to be interpreted indivisually
from bokeh.charts import Scatter, output_file, save         #creates a plot or a place for the data
df = pd.read_csv('Pokemon.csv')                             #accesses the data and converts it into a data frame


p = Scatter(df[1:101],                          #creates the visual
                                                #only access data from 1-100 of csv file
                x='Attack',                     #attack stats will be the x coordinate
                y='Defense',                    #defense stats will be the y coordinate
                marker='Type 1',                #the 1st type of pokemon will have different dots        
                color='Type 2',                 #the 2nd type of pokemon will have different colors
                title='Attack vs Defense',      #title of graph
                legend='top_left',              #placement of legend
                xlabel='Attack stats',          #label for x axis
                ylabel='Defense stats',         #label for y axis
                plot_width=1000,                #the width size of the graph/image itself
                plot_height=1000)               #the height size of the graph/image itself

output_file('pokemonstats.html')                #names the file and turns it into an image

save(p)             #creates/saves the graph