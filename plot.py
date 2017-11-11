from numpy import genfromtxt
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("f", help="file name for importing data")
parser.add_argument("--title", help="title of plot", type = str)
parser.add_argument("--xlab", help="x label", type = str)
parser.add_argument("--ylab", help="y label", type=str)

args = parser.parse_args()

dat = genfromtxt(args.f, delimiter='    ')

plt.plot(dat)

# check the optional arguments
if args.title is None:
    args.title = " "
if args.ylab is None:
    args.ylab = " "
if args.xlab is None:
    args.xlab = " "

plt.title(args.title)
plt.ylabel(args.ylab)
plt.xlabel(args.xlab)
plt.show()
