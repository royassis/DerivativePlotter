import numpy as np
from matplotlib import pyplot  as plt


# My math functions
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


# Generalized math functions
def generalFunc(func, x, **kwargs):
    return func(x, **kwargs)


# Tangent line calc and plot
def calc_plot_derv(p, x, derv_a, derv_b):

    z=2
    c = (z**2/(1+derv_a[p]**2))**0.5
    c = c/2
    print(c)


    arr = np.arange(x[p]-3, x[p]+3, 0.1)
    new_y = derv_a[p] * arr + derv_b[p]
    plt.plot(arr, new_y)


# Tangent line calc and plot + func plot
def plotAll(p, x, derv_a, derv_b, func, **kwargs):
    plt.plot(x, generalFunc(func, x, **kwargs))
    calc_plot_derv(p, x, derv_a, derv_b)
    plt.show()

# Main function
def myDerv(funcToUse, p, x ,dx=0.0001, **kwargs):


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
x = np.arange(-10, 10, 0.1)

# farams
a = 2  # if linear function
b = 5  # if linear and parabolic
c = 3
dx = 0.000000000001  # dx
p = 7

d={1:sin,
   2:parabole2,
   3:linearfunc2,
   4:sin
   }

func = d[2]
someNewFunc = (lambda x, **a: x**3-5*x)

myDerv(someNewFunc, p, x, dx, a = a, b = b, c = c)


