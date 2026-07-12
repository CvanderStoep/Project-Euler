from typing import Iterable, List, Tuple
import sympy as sp
from sympy import Rational, Matrix
pro

def fit_polynomial(points: Iterable[Tuple[float, float]], order: int, regularization: float = 1e-8) -> List[sp.Expr]:
    """Fit a polynomial of given order to the provided points using SymPy.

    If there are fewer points than order + 1, the fit is regularized so that
    a stable solution can still be obtained.

    Returns coefficients [a0, a1, ..., a_order] for
    p(x) = a0 + a1*x + ... + a_order*x^order.
    """
    pts = list(points)
    if order < 0:
        raise ValueError("order must be non-negative")
    if not pts:
        raise ValueError("at least one point is required")

    m = order + 1
    x_vals = [Rational(x) for x, _ in pts]
    y_vals = [Rational(y) for _, y in pts]

    # Build the Vandermonde matrix using exact rational arithmetic
    matrix_list = [[x_vals[i] ** j for j in range(m)] for i in range(len(pts))]
    b_list = y_vals

    # Convert to SymPy matrices
    A = Matrix(matrix_list)
    b = Matrix(b_list)

    ATA = A.T * A
    ATb = A.T * b
    if len(pts) < m:
        ATA += sp.eye(m) * Rational(regularization)
    coeffs = ATA.LUsolve(ATb)

    return [coeff for coeff in coeffs]


def evaluate_polynomial(coefficients: List[sp.Expr], x: float) -> sp.Expr:
    result = Rational(0)
    power = Rational(1)
    x_val = Rational(x)
    for coeff in coefficients:
        result += coeff * power
        power *= x_val
    return result

def function_to_fit(x):
    # Example function to fit: f(x) = x^3
    return 1 - x + x**2 - x**3 + x**4 -x**5 + x**6 - x**7 + x**8 - x**9 + x**10

    # return x ** 3   

if __name__ == "__main__":
    total_FIT = 0
    for k in range(1, 15):
    # k = 3
        sample_points = [(i, function_to_fit(i)) for i in range(1, k+1)]
        # print("Sample points:", sample_points)
        coefs = fit_polynomial(sample_points, order=k-1)
        print("coefficients:", coefs)

        x = 1
        while x <= k + 1:
            fitted_value = evaluate_polynomial(coefs, x)
            # print(f"fitted value at {x}:", fitted_value)
            if fitted_value != function_to_fit(x):
                print(f"k={k}: Discrepancy found at x={x}: fitted value {fitted_value} != actual value {function_to_fit(x)}") 
                total_FIT += fitted_value           
                break
            x += 1
    print("Total FIT:", total_FIT)

    

"""Alternatively, you can use numpy for polynomial fitting and evaluation, which is more efficient for numerical computations. Here's how you can do it using numpy:"""
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