import numpy as np
import math


def generate_recurrence_formula(r1, r2):
    return lambda n, result: {
        "a": r1 ** n,
        "b": r2 ** n,
        "result": result,
    }


def solve_recurrence(r1, r2, initial_value_0, initial_value_1):
    equation_0 = generate_recurrence_formula(r1, r2)(0, initial_value_0)
    equation_1 = generate_recurrence_formula(r1, r2)(1, initial_value_1)

    a, b = solve_linear_system(equation_0, equation_1)

    return {
        "a": a,
        "b": b,
        "r1": r1,
        "r2": r2,
    }


def solve_linear_system(eq1, eq2):
    A = np.array([
        [eq1["a"], eq1["b"]],
        [eq2["a"], eq2["b"]],
    ])
    B = np.array([eq1["result"], eq2["result"]])

    return np.linalg.solve(A, B)


def solve_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
        raise ValueError("Negative discriminant: the equation has complex roots.")
    
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    
    return x1, x2


def main():
    a = int(input("Enter the coefficient a: "))
    b = int(input("Enter the coefficient b: "))
    c = int(input("Enter the constant c: "))

    s0 = int(input("Enter the initial value s0: "))
    s1 = int(input("Enter the second value s1: "))

    r1, r2 = solve_quadratic(a, b, c)

    solution = solve_recurrence(r1, r2, s0, s1)

    print(f"The roots are: {r1:.1f}, {r2:.1f}")
    a = solution['a']
    b = solution['b']
    r1 = solution['r1']
    r2 = solution['r2']

    print(f"Recurrence relation: {a:.2f} * ({r1:.1f}) ** n + {b:.2f} * ({r2:.1f}) ** n")


if __name__ == "__main__":
    main()
