from matplotlib import pyplot;
from pylab import genfromtxt;
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("f", help="file name for importing data")
parser.add_argument("--title", help="title of plot", type = str)
parser.add_argument("--xlab", help="x label", type = str)
parser.add_argument("--ylab", help="y label", type=str)
parser.add_argument("--type", help="type of plot", type=str)

args = parser.parse_args()

if args.title is None:
    args.title = " "
if args.ylab is None:
    args.ylab = " "
if args.xlab is None:
    args.xlab = " "
if args.type is None:
    args.type = "line"

dat = genfromtxt(args.f)

if args.type == "line":
    pyplot.plot(dat[:,0], dat[:,1], label = args.title);
if args.type == "scatter":
    pyplot.scatter(dat[:,0], dat[:,1], label = args.title);
else:
    pyplot.plot(dat[:,0], dat[:,1], label = args.title);

pyplot.ylabel(args.ylab)
pyplot.xlabel(args.xlab)
pyplot.legend();
pyplot.show();
