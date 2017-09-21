# Bisection method of solving an equation 

It is a quite simple method of solving an equation numerically in cases where the exact solution is difficuilt to find. In this method we repetedly bisect an interval into halves until we reach the desired accuracy. It is a consequence of well known **mean value theorem** of calculus.

I have used the equation  `x - cos(x) = 0  ` as a demonstration. This problem is also on the book "Quantum Mechanics" of Schaum Outlines page 256. They have done that in FORTRAN though while my code is on Python (2.7.13). My C version of the same problem can be found [here.](https://github.com/physicistbkb/bisection-method-in-C/)

The code was written under Debian GNU/Linux in `Python IDLE` under `Python`.
``` sh
$ python --version
Python 2.7.13
```

Here's the code running. The value obtained after 16 iterations can be verified with the book or other sources as well. Also note that we obtained exactly the same value using C as well.
![N](https://imgoat.com/uploads/c8349cc726/44898.png)


# USAGE
If your maximum iterations is say 20 then you can use,


`python bisection.py 20`


Alternatively you can also `chmod +x bisection.py` and then  


`./bisection.py 20`

# LICENSE
![GNU_GPL_v3.0](https://www.gnu.org/graphics/gplv3-127x51.png)


Totally [RMS](https://stallman.org/) approved!
While you're at it, please check out [GNU](https://www.gnu.org) and [Free Software Foundation](https://www.fsf.org) as well!
