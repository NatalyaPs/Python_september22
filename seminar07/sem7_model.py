import sympy

def evaluate_expr(expr):
    x = str(sympy.Symbol('x'))  # вводим переменную
    return sympy.solve(expr, x)