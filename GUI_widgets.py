import ipywidgets as widgets
from IPython.display import display

a = widgets.FloatText()
b = widgets.FloatSlider()

display (a,b)
mylink = widgets.jslink((a,'value'),(b,'value'))