import numpy as np
from matplotlib import pyplot  as plt


# Generalize math functions
def linearfunc2(x, **kwargs):
    a= kwargs["a"]
    b = kwargs["b"]
    y = a * x + b
    return y


def parabole2(x, **kwargs):
    a= kwargs["a"]
    y = x ** 2 + a
    return y

def sin(x, **kwargs):
    a = kwargs["a"]
    b = kwargs["b"]
    c = kwargs["c"]
    y = a*np.sin(x*b)+c
    return y


def generalFunc(func, x, **kwargs):
    return func(x, **kwargs)


# Tangent line and function plots
def calc_plot_derv(p, x, derv_a, derv_b):

    arr = np.arange(x[p]-2, x[p]+2, 0.1)
    new_y = derv_a[p] * arr + derv_b[p]
    plt.plot(arr, new_y)


def plotAll(p, x, derv_a, derv_b, func, **kwargs):
    plt.plot(x, generalFunc(func, x, **kwargs))
    calc_plot_derv(p, x, derv_a, derv_b)
    plt.show()


def myDerv(dx, funcToUse, p, x, **kwargs):


    y_x_dx = generalFunc(funcToUse, (x + dx), **kwargs)  # f(x+dx)
    y_x = generalFunc(funcToUse, (x), **kwargs)  # f(x)

    # Slope: a=(f(x+dx)-f(x))/dx   Intercept: b= y- a*x
    derv_a = (y_x_dx - y_x) / dx  # a of tangent at each point
    derv_b = y_x - derv_a * x  # b of tangent at each point

    # Convert point to index and plot
    itemindex = np.where(np.round(x, 3) == p)
    plotAll(itemindex[0][0], x, derv_a, derv_b, funcToUse, **kwargs)


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

func = d[4]

myDerv(dx, func, p, x, a = a, b = b, c = c)









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