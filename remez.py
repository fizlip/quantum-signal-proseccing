import numpy 
import math


def bisection_search(f, low, high):
    
    #flip high and low if out of order
    if f(high) < f(low):
        low, high = high, low
    
    #find mid point
    mid = .5*(low + high)
    
    while True:
        #bracket up
        if f(mid) < 0:
            low = mid
        #braket down
        else:
            high = mid
        
        #update mid point
        mid = .5*(high + low)
        #break if condition met
        if abs(high - low) < 10**-15:
            break
    
    return mid


def concave_max(f, low, high):
    #create an approximate derivative expression
    scale = abs(high - low)
    h = 10**(-5)*scale
    df = lambda x: (f(x + h) - f(x-h)) / (2.0*h)

    return bisection_search(df, low, high)

def Remez(func, n_degree):
    
    #initialize the node points
    
    x_points = numpy.polynomial.chebyshev.chebpts2(n_degree+2)
    print(x_points)
    max_iter = 100
    
    A = numpy.zeros((n_degree+2, n_degree+2))
    b = numpy.zeros(n_degree+2)
    coeffs = numpy.zeros(n_degree+2)
    
    #place in the E column
    
    E_array = numpy.array([(-1)**(i+1) for i in range(n_degree+2)])
    A[:, n_degree+1] = E_array
    
    for i in range(max_iter):
        
        #build the system
        
        for i in range(n_degree+1):
            A[:,i] = x_points**i
            b[i] = func(x_points[i])
        
        b[-1] = func(x_points[-1])
        
        #solve the system for polynomial coefficents
        params = numpy.linalg.solve(A, b)
        coeffs = numpy.flip(params[:-1])
        
        #build the residual expression
        r_i = lambda x: func(x) - numpy.polyval(coeffs, x)
        
        #create the intervals to bracket
        interval_list = [[x_points[i], x_points[i+1]] for i in range(len(x_points)-1)]
        
        intervals = [3.5]
        intervals.extend([bisection_search(r_i, *i) for i in interval_list])
        intervals.append(-3.5)
        
        #now that we have the brakets for the extermem
        extermum_interval = [[intervals[i], intervals[i+1]] for i in range(len(intervals)-1)]
        
        # solve for the extermum
        extremums = [concave_max(r_i, *i) for i in extermum_interval]
        
        # HEAVY ASSUMPTION
        extremums[0] = 3.5
        extremums[-1] = -3.5
        
        #update our set K
        x_points = numpy.array(extremums)
        
        # Termination criteria
        errors = numpy.array([abs(r_i(i)) for i in extremums])
        mean_errors = numpy.mean(errors)

        if numpy.max(numpy.abs(errors - mean_errors)) < 10**(-4)*numpy.max(errors):
            break
        
        
    # for i in range(len(coeffs)):
    #    coeffs[i] = -2*numpy.arccos(-coeffs[i]) 
    return coeffs 

def func1(x):
    return x
def func2(x):
    return 2*x**2 - 1
def func3(x):
    return 4*x**3 - 3*x
def func4(x):
    return math.exp(x)

