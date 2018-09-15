# program: plotfunc.py
# author: Trevor M. Tomesh
# date: 2018/09/14
# description: This program simply plots a given function using matplotlib
# given a start value, and end value and a step value. 
# -----------------------------------------------------------------------------
from numpy import *
import matplotlib.pyplot as plot

# define start, end and step
pStart = 0
pEnd = 100
pStep = 0.1

# define the title and axies 
ptitle = "Custom Plot"
pxaxis = "x axis"
pyaxis = "y axis"

x = arange(pStart, pEnd, pStep)
y = sin(x)+sin(x/3)+sin(x/5)

plot.plot(x, y)

# render the title
plot.title(ptitle)

# Give x axis label 
plot.xlabel(pxaxis)

# Give y axis label 
plot.ylabel(pyaxis)
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()

# Display the plot
plot.show()
