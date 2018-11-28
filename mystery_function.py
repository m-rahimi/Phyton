def reduce(fun, arr, init=None):
    accum = init
    for x in arr:
        accum = fun(accum, x)
    return accum

def mystery_function(x):
    return lambda z: reduce(lambda w,y: y(w), x, z)
    
m = mystery_function([lambda x, i=i: x*i for i in range(1,4)])
m(2)
