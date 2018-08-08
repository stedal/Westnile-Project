# -*- coding: utf-8 -*-

##Interactive bokeh for cross location selection

## Updated with regression line on 29 Apr 18
import numpy as np
import pandas as pd
from bokeh.io import curdoc,show
from bokeh.layouts import row,column, widgetbox
from bokeh.models import ColumnDataSource,LabelSet,Div,Paragraph,PointDrawTool,PolyDrawTool,PolyEditTool,PolySelectTool,CustomJS
from bokeh.models.widgets import Slider, TextInput,Button,CheckboxGroup,CheckboxButtonGroup,RadioGroup,Select,DataTable, TableColumn
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models import HoverTool

train = pd.read_csv('heroku/combined_train.csv')
test = pd.read_csv('heroku/combined_test.csv')
#spray = pd.read_csv('assets/input/spray.csv')

x_var = ['Negative', 'Positive'] #train['WnvPresent'].value_counts(normalize = False).index
counts = train['WnvPresent'].value_counts(normalize = False)
source = ColumnDataSource(data = dict(labels = x_var, counts = counts))



p1 = figure(x_range = x_var, title = 'West Nile Class Balance',
            plot_height = 400, plot_width = 400, tools = 'save')

p1.vbar(source = source,
        x = 'labels',
        top = 'counts',
        bottom = 0,
        width = .9,
        #fill_color ="green",
        line_color ="white",
        line_width = 2,
        fill_color=factor_cmap('labels', palette = Spectral6, factors = x_var)
       )

p1.title.align = 'center'
p1.add_tools(HoverTool(
    tooltips=[
        ("index", "$index"),
     ("(x,y)", "($labels, $counts)")
    ])
           )

# hover.tooltips = [
#     ("index", "$index"),
#     ("(x,y)", "($x, $y)")]

show(p1)

curdoc().add_root(p1)
