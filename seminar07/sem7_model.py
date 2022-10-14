import sympy

def evaluate_expr(expr):
    x = str(sympy.Simbol('x'))  # вводим переменную
    return sympy.solve(expr, x)