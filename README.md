# Derivative plotter

After a time of studying gradient decent I tried to implement it manualyl from scrath.

But I did not know how to derive the loss function in respect to each component. It's not
like your regular hight school mathematics. It had to be don't numericlly. At least that's the only way I knew how to do it
after reading about it online.


### Mathematicly preface
#### Getting the derivative and plotting a tangent

So I used the basic formula to calaculate slope

* formula 1 : dy/dx = ( f(x+dx)-f(dx) ) / dx

and I took dx to be very small. Initially 0.00001

This gave me a slope of a line tangent to a point on a function.

Using the x and f(x) cordinats and the slope I plotted a line tangent to the function at that point

#### Setting the length of the tangent
Later on I wanted to control the length of the plotted line.

I did it in the manner to come :

* formula 2 : z^2 = x^2+ y^2

Where z is the length of the line I wanted, continuing on

* z^2 = x^2+ f(x)^2
* z^2 = x^2+ (ax)^2

Where a is the slope of the tangent line. Now to isolate x:

* (x^2)*(1+a^2) = z^2
* formula 6 : x= ( z^2 / (1+a^2) ) ^ 0.5

Now I knew what is the x range I needed in order to plot a line with z length

Later on I used xrange/2 from both the sides of an x value that I wanted to derive upon


### Actual code
I did two varient of the same code. The second one is better and involves using **kwargs instead of *args.

This is the main function: myDerv

#### * myDerv (funcToUse, p, x ,dx=0.0001, **kwargs)

##### Parameters :

funcToUse - Is a function that recives one number variable and outputs one number .
This function must get **kwargs as input

p - is the point to be derived. a number between -5 and 5 where the function is defined

dx- is dx


##### Output :

Plot of the function and the tangent line to p





