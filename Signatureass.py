import math

def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

# Define f(x) and f'(x)
f = lambda x: math.exp(x) + x**2 - 4
df = lambda x: math.exp(x) + 2*x

# Initial guess
x0 = -2.0

# Compute root
root = newton_method(f, df, x0)
print(f"The negative root is approximately: {root:.6f}")