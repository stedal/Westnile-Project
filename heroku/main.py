# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
from bokeh.io import curdoc,show
from bokeh.layouts import row,column, widgetbox
from bokeh.plotting import figure
from bokeh.io import output_notebook, show
from bokeh.models import ColumnDataSource, HoverTool, Plot
from bokeh.embed import components, file_html
from bokeh.transform import factor_cmap
from bokeh.models.widgets import Panel, Tabs
from bokeh.resources import CDN
from bokeh.palettes import Spectral6



train = pd.read_csv('heroku/data/combined_train.csv')
test = pd.read_csv('heroku/data/combined_test.csv')
#spray = pd.read_csv('assets/input/spray.csv')

train['Year'] = train['Date'].apply(lambda x: x[:4])
train['Month'] = train['Date'].apply(lambda x: x[5:7])
train['Day'] = train['Date'].apply(lambda x: x[8:])

test['Year'] = test['Date'].apply(lambda x: x[:4])
test['Month'] = test['Date'].apply(lambda x: x[5:7])
test['Day'] = test['Date'].apply(lambda x: x[8:])

def datetime(x):
    return np.array(x, dtype=np.datetime64)

x2007 = datetime(list(train[train['Year'] == '2007']['Date']))
y2007 = list(train[train['Year'] == '2007']['Tavg'])
x2009 = datetime(list(train[train['Year'] == '2009']['Date']))
y2009 = list(train[train['Year'] == '2009']['Tavg'])
x2011 = datetime(list(train[train['Year'] == '2011']['Date']))
y2011 = list(train[train['Year'] == '2011']['Tavg'])
x2013 = datetime(list(train[train['Year'] == '2013']['Date']))
y2013 = list(train[train['Year'] == '2013']['Tavg'])
x2015 = datetime(list(train[train['Year'] == '2015']['Date']))
y2015 = list(train[train['Year'] == '2015']['Tavg'])

data3 = {'temperature2007': y2007,
        'date2007': x2007,
         'range2007': list(range(len(x2007)))
       }
data4 = {
        'temperature2009': y2009,
        'date2009': x2009
}
data5 = {
        'temperature2011': y2011,
        'date2011': x2011
}
data6 = {
        'temperature2013': y2013,
        'date2013': x2013
}
source3 = ColumnDataSource(data = data3)
source4 = ColumnDataSource(data = data4)
source5 = ColumnDataSource(data = data5)
source6 = ColumnDataSource(data = data6)

p3 = figure(title = 'Average Temperature (2007)', x_axis_type="datetime", plot_height = 600, plot_width = 800)
p3.circle('date2007' ,'temperature2007', source = source3)
p3.title.align = 'center'
p3.title.text_font_size = '16pt'
p3.add_tools(HoverTool(
    tooltips=[
        ("Date", "@date2007"),
     ("Temp", "@temperature2007")
    ]))

p4 = figure(title = 'Average Temperature (2009)', x_axis_type="datetime", plot_height = 600, plot_width = 800)
p4.circle('date2009' ,'temperature2009', source = source4)
p4.title.align = 'center'
p4.title.text_font_size = '16pt'
p4.add_tools(HoverTool(
    tooltips=[
        ("Date", "@date2009"),
     ("Temp", "@temperature2009")
    ]))

p5 = figure(title = 'Average Temperature (2011)', x_axis_type="datetime", plot_height = 600, plot_width = 800)
p5.circle('date2011' ,'temperature2011', source = source5)
p5.title.align = 'center'
p5.title.text_font_size = '16pt'
p5.add_tools(HoverTool(
    tooltips=[
        ("Date", "@date2011"),
     ("Temp", "@temperature2011")
    ]))

p6 = figure(title = 'Average Temperature (2013)', x_axis_type="datetime", plot_height = 600, plot_width = 800)
p6.circle('date2013' ,'temperature2013', source = source6)
p6.title.align = 'center'
p6.title.text_font_size = '16pt'
p6.add_tools(HoverTool(
    tooltips=[
        ("Date", "@date2013"),
     ("Temp", "@temperature2013")
    ]))

tab1 = Panel(child = p3, title = 'Ave Temp vs Time (2007)')
tab2 = Panel(child = p4, title = 'Ave Temp vs Time (2009)')
tab3 = Panel(child = p5, title = 'Ave Temp vs Time (2011)')
tab4 = Panel(child = p6, title = 'Ave Temp vs Time (2013)')
layout = Tabs(tabs=[tab1, tab2, tab3, tab4])
#show(layout)

curdoc().add_root(layout)
