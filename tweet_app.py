from bokeh.plotting import figure
from bokeh.io import output_notebook, show, curdoc
from bokeh.models import ColumnDataSource, Select
from bokeh.models.glyphs import Line
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import row

from bokeh.models import ColumnDataSource, DatetimeTickFormatter, DatePicker

from datetime import datetime

import pandas as pd 


df=pd.read_csv("df_prepared.csv") 
df['date']=pd.to_datetime(df['date'])
df.set_index('date', inplace=True)


def df_freq(has, loc, freq):
    df1 = df[(df["hashtag"]==str(has)) & (df['location']==str(loc))].resample(str(freq)).mean()
    df2 = df[(df["hashtag"]==str(has)) & (df['location']==str(loc))].resample(str(freq)).mean()
    df3 = df[(df["hashtag"]==str(has)) & (df['location']==str(loc))].resample(str(freq)).mean()
    df4 = df[(df["hashtag"]==str(has)) & (df['location']==str(loc))].resample(str(freq)).mean()
    return {0:df1,1:df2,2:df3,3:df4}
        
source1 = ColumnDataSource(df_freq("netflix","europe","D")[0])
source2 = ColumnDataSource(df_freq("netflix","usa","D")[1])
source3 = ColumnDataSource(df_freq("disneyplus","europe","D")[2])
source4 = ColumnDataSource(df_freq("disneyplus","usa","D")[3])
        
p = figure(title= "People's opinion about Netflix/Disney+ in USA and EUROP",x_axis_type="datetime", plot_width=1000, plot_height=600)
        
p.line('date','tweet_polarity', source=source1, alpha=1, color='red', line_width=2, legend="Netflix Europ")
p.line('date','tweet_polarity', source=source2, color='blue', line_width=2, legend="Netflix Usa")
p.line('date','tweet_polarity', source=source3, color='green', line_width=2, legend="Disney+ Europ")
p.line('date','tweet_polarity', source=source4, color='black', line_width=2, legend="Disney+ Usa")
        
p.legend.location = "top_left"
p.legend.click_policy="hide"

#p.xaxis.formatter=DatetimeTickFormatter(days="%m/%d %H:%M",
#months="%m/%d %H:%M",
#hours="%m/%d %H:%M",
#minutes="%m/%d %H:%M")
        
select = Select(title="Options :", value="Days", options=['Days', 'Hours'])
        
def update(attr, old, new) :
    N = select.value
    if N=="Days": a="D"
    elif N=="Hours": a="H"
    source1.data = df_freq("netflix","europe",str(a))[0]
    source2.data = df_freq("netflix","usa",str(a))[1]
    source3.data = df_freq("disneyplus","europe",str(a))[2]
    source4.data = df_freq("disneyplus","usa",str(a))[3]
select.on_change('value', update)
        
layout =  row(select, p)
curdoc().add_root(layout)        