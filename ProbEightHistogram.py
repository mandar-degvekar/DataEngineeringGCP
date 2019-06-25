import matplotlib.pyplot as pt
import pandas as pd
import numpy as np

# x = np.random.random_integers(1,200,5)
def splitandlist(input):
    l=[]
    for i in input:
        try:

            l.append(int(i))

        except:
            print(i + " is not a number")


    return l



xinputval=input("Please enter integer values to plot histogram X axis")

x=xinputval.split(',')
y=[10,20,30,40,50,60,70]
pt.hist(splitandlist(x),y,histtype="bar",rwidth=0.8)
pt.title("Test Histogram")
pt.xlabel('x-axis')
pt.ylabel('no')
pt.savefig("filname.pdf")