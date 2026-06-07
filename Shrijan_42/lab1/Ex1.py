import sympy as sp

x = sp.symbols("x")
expr = sp.sympify(input("Enter polynomial: "))
f = sp.lambdify(x, expr, modules=["numpy"])

fa = float(input("Enter initial value: "))
fb = float(input("Enter final value: "))
tolerence = float(input("Enter tolerence: "))
max_iterations = int(input("Enter maximum iterations: "))

def bisect(f, fa, fb, tolerence, max_iterations):
    if f(fa) * f(fb) > 0:
        return None
    for i in range(max_iterations):
        c = (fa + fb) / 2
        if f(fa) * f(c) < 0:
            fb=c
        else:
            fa=c
        if (fb-fa)/2<tolerence:
            break
        print("Approx root: ", (fa+fb)/2)
    return (fa+fb)/2    

print("Root: ", bisect(f, fa, fb, tolerence, max_iterations))
