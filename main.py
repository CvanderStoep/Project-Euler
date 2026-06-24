import numpy as np


def u(n):
    return sum([(-1)**k * n**k for k in range(11)])


accu = [u(n) for n in range(1, 13)]


def OP(k, n):
    x_vals = list(range(1, k + 1))        
    y_vals = accu[:k]                     
    
    
    coeffs = np.polyfit(x_vals, y_vals, k - 1)
    poly = np.poly1d(coeffs)
    
    
    return round(poly(n))  


bad_list = []

for k in range(1, 11 + 1):  
    pred = OP(k, k + 1)
    actual = accu[k]        
    if pred != actual:
        bad_list.append(pred)


print("bad_list:", bad_list)
print("Sum of bad elements:", sum(bad_list))