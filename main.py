import numpy as np
import math

def get_equation(r1, r2) -> callable:
    return lambda n, result: {"a": r1**n, "b": r2**n, "c": result}

def solve_reccurance(r1, r2, result_0, result_1) -> dict:
    eq_0 = get_equation(r1, r2)(0, result_0)
    eq_1 = get_equation(r1, r2)(1, result_1)

    a, b = solve_linear(eq_0, eq_1)

    return dict(a=a, b=b, r1=r1, r2=r2)

def solve_linear(eq1 : dict, eq2 : dict) -> np.ndarray[np.float64]:
    A = np.array([[eq1["a"], eq1["b"]], [eq2["a"], eq2["b"]]])
    B = np.array([eq1["c"], eq2["c"]])

    return np.linalg.solve(A, B)

def solve_quadratic(a, b, c):
    D = b**2 - 4*a*c
    
    if D < 0:
        raise ValueError("Bro is trying to solve for x1, x2 while D is negative :skull")
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return (x1, x2)

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

s0 = int(input("s0:  "))
s1 = int(input("s1:  "))

r1, r2 = solve_quadratic(a, b, c)
solution = solve_reccurance(r1, r2, s0, s1)

print(r1, r2)
a = solution['a']
b = solution['b']
r1 = solution['r1']
r2 = solution['r2']

print(f"{a} * ({r1:.1f}) ** n + {b:.2f} * ({r2:.1f}) ** n")