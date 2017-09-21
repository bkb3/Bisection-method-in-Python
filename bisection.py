#!/usr/bin/env python
import sys
import math

def func(x):
    return math.cos(x) - x


def main():
    a = 0.0
    b = 1.0
    tolerance = 0.00001
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print 'Usage : bisection.py <maximum iterations>'
        sys.exit(0)

    
    print 'iteration\t a\t\t b\t\t c\t\t f(c)\t'
    print '---------\t --------\t --------\t --------\t --------\t'
    i = 0
    while i <= int(sys.argv[1]):
        c = (a + b)/2.0
        if (func(a) * func(c)) < 0: #sign checking
            b = c
        else: #(func(b) * func(c)) > 0
            a = c
        i = i + 1
        print "%d\t\t %.6f\t %.6f\t %.6f\t %.6f" %(i-1 ,a ,b ,c ,func(c))


#we now get out of loop and print the value of final c
    if abs((a-b)/2.0) < tolerance:
        print 'The root after %dth iteration is %.10f.'%(i-1,c) 
    else:
        print 'We were unable to meet tolerance within given iterations.'
    


if __name__ == '__main__':
    main()
    
