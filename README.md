# plot.py

![](plotpy.png)

*"Completely Unnecessary!™"*
------------
This is a collection of little plotting program written in python that probably doesn't even deserve its own repository. It's ridiculously simple and was written up in a couple of minutes using the pyplot library in python. It's here mostly so I don't lose it -- again.

### Dependencies
------------
The following dependencies are required in order to
properly run plot.py!

- python 3.x
- matplotlib
- numpy

Install python 3 (if for some reason you don't already
have it!)
```bash
sudo apt-get install python3
```
Install pip for python 3:
```bash
sudo apt-get install python3-pip
```
Install the matlplotlib library (what all this works on top of!)

```bash
pip3 install matplotlib
```

Install numpy -- because math.
```bash
pip3 install numpy
```

### Installation
Just download it and unzip the folder. Ta-da!

### Usage
plot.py will take a space-delimited table like this:

```
93 46            
94 56            
95 66            
97 76            
100 86     
103 96     
110 106      
```
and turn it into a plot like this:

![Example Plot](https://raw.githubusercontent.com/trevortomesh/plot.py/master/plot.png)


plotfunc.py can be edited internally to plot a 2D function -- just change the line under 
"Type your function here" 
