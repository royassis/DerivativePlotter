import numpy as np
from matplotlib import pyplot  as plt


# Generalize math functions
def linearfunc2(x, *arg):
    a, b = arg[:2]
    y = a * x + b
    return y


def parabole2(x, *arg):
    a = arg[0]
    y = x ** 2 + a
    return y

def sin(x, *arg):
    a,b,c = arg
    y = a*np.sin(x*b)+c
    return y


def generalFunc(func, x, *arg):
    return func(x, *arg)


# Tangent line and function plots
def calc_plot_derv(p, x, derv_a, derv_b):
    new_y = derv_a[p] * x + derv_b[p]
    plt.plot(x, new_y)


def plotAll(p, x, derv_a, derv_b, func, *arg):
    plt.plot(x, generalFunc(func, x, *arg))
    calc_plot_derv(p, x, derv_a, derv_b)
    plt.show()


def myDerv(dx, funcToUse, p, x, *arg):


    y_x_dx = generalFunc(funcToUse, (x + dx), *arg)  # f(x+dx)
    y_x = generalFunc(funcToUse, (x), *arg)  # f(x)

    # Slope: a=(f(x+dx)-f(x))/dx   Intercept: b= y- a*x
    derv_a = (y_x_dx - y_x) / dx  # a of tangent at each point
    derv_b = y_x - derv_a * x  # b of tangent at each point

    # Convert point to index and plot
    itemindex = np.where(np.round(x, 3) == p)
    plotAll(itemindex[0][0], x, derv_a, derv_b, funcToUse, *arg)


#   Code

#   Plot x data
x = np.arange(-5, 5., 0.1)

# farams
a = 2  # if linear function
b = 5  # if linear and parabolic
c = 3
dx = 0.000000000001  # dx
p = 1

d={1:sin,
   2:parabole2,
   3:linearfunc2,
   4:sin
   }

func = d[2]

myDerv(dx, func, p, x, a, b, c)












"""
#Which function to use
funcToUse= parabole2

y_x_dx  =generalFunc(funcToUse,(x+dx),b) #f(x+dx)
y_x     =generalFunc(funcToUse,(x),b)    #f(x)

# Slope: a=(f(x+dx)-f(x))/dx   Intercept: b= y- a*x
derv_a= ( y_x_dx - y_x) / dx #a of tangent at each point
derv_b = y_x- derv_a*x #b of tangent at each point

# Choose an x point,-5<x<5,to derive
p = 3

#Convert point to index and plot
itemindex = np.where(np.round(x,3)==p)
plotAll(itemindex[0][0],x,derv_a,derv_b,b,funcToUse)



#Define math functions
def linearfunc(x,a,b):
    y= a*x+b
    return y

def parabole(x,b):
    y= x**2+b
    return y


"""