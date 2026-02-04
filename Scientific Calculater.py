import math
import cmath
from fractions import Fraction
import re

# ================= GLOBAL STATES =================
SHIFT = False
ANGLE_MODE = "DEG"
PRECISION_MODE = "NORM"
FIX_DECIMALS = 4
MEMORY = 0
ANS = 0
history = []
USE_FRACTION = False  # New: Fraction mode

# ================= ANGLE =================
def to_rad(x):
    return math.radians(x) if ANGLE_MODE == "DEG" else x

def from_rad(x):
    return math.degrees(x) if ANGLE_MODE == "DEG" else x

# ================= SHIFT FUNCTIONS =================
def sin_func(x):
    return math.asin(x) if SHIFT else math.sin(to_rad(x))

def cos_func(x):
    return math.acos(x) if SHIFT else math.cos(to_rad(x))

def tan_func(x):
    return math.atan(x) if SHIFT else math.tan(to_rad(x))

def log_func(x):
    return 10**x if SHIFT else math.log10(x)

def ln_func(x):
    return math.e**x if SHIFT else math.log(x)

def root(x,n):
    return x**(1/n)

# ================= FACTORIAL =================
def factorial(n):
    if n < 0:
        raise ValueError("Factorial only for positive integers")
    return math.factorial(int(n))

# ================= COMBINATORICS =================
def nCr(n,r):
    return math.comb(int(n),int(r))

def nPr(n,r):
    return math.perm(int(n),int(r))

# ================= COMPLEX ↔ POLAR =================
def rect_to_polar(z):
    r = abs(z)
    t = from_rad(cmath.phase(z))
    return r,t

def polar_to_rect(r,t):
    return cmath.rect(r,to_rad(t))

# ================= MEMORY =================
def mem_add(x):
    global MEMORY
    MEMORY += x

def mem_sub(x):
    global MEMORY
    MEMORY -= x

def mem_clear():
    global MEMORY
    MEMORY = 0

# ================= FORMAT OUTPUT =================
def format_out(x):
    if isinstance(x, complex):
        return str(x)
    if USE_FRACTION and isinstance(x,float):
        try:
            return str(Fraction(x).limit_denominator())
        except:
            return str(x)
    if PRECISION_MODE=="FIX":
        return f"{x:.{FIX_DECIMALS}f}"
    if PRECISION_MODE=="SCI":
        return f"{x:.6e}"
    return str(x)

# ================= SAFE ENV =================
SAFE = {
    "sin": sin_func,
    "cos": cos_func,
    "tan": tan_func,
    "log": log_func,
    "ln": ln_func,
    "sqrt": math.sqrt,
    "root": root,
    "pi": math.pi,
    "e": math.e,
    "j": 1j,
    "fact": factorial,
    "nCr": nCr,
    "nPr": nPr,
    "ANS": lambda: ANS,
    "abs": abs,
    "Fraction": Fraction
}

# ================= FACTORIAL PARSER =================
def replace_factorial(expr):
    return re.sub(r'(\d+)!', r'fact(\1)', expr)

# ================= CASIO % KEY =================
def casio_percent(expr):
    m = re.search(r'(\d+\.?\d*)([\+\-\*/])(\d+\.?\d*)%', expr)
    if not m:
        return expr
    a = float(m.group(1))
    op = m.group(2)
    b = float(m.group(3))
    if op == "+":
        result = a + (a*b/100)
    elif op == "-":
        result = a - (a*b/100)
    elif op == "*":
        result = a * (b/100)
    elif op == "/":
        result = a / (b/100)
    return str(result)

# ================= EVALUATE =================
def evaluate(expr):
    global ANS
    expr = expr.replace("^","**")
    expr = expr.replace("ANS", str(ANS))
    expr = replace_factorial(expr)
    expr = casio_percent(expr)
    try:
        # fraction mode auto conversion
        if USE_FRACTION and "/" in expr and not any(f in expr for f in ["sin","cos","tan","log","ln","fact","nCr","nPr"]):
            try:
                return float(Fraction(expr))
            except:
                pass
        result = eval(expr, {"__builtins__":None}, SAFE)
        ANS = result
        return result
    except Exception as e:
        return f"Error: {e}"

# ================= EQUATION SOLVER =================
def solve_linear(a,b):
    return -b/a

def solve_quadratic(a,b,c):
    d = b*b - 4*a*c
    if d >= 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
    else:
        x1 = complex(-b, math.sqrt(-d))/(2*a)
        x2 = complex(-b, -math.sqrt(-d))/(2*a)
    return x1,x2

# ================= MENU =================
def show_menu():
    print("\n==== FULL ADVANCED CALC ====")
    print("SHIFT:",SHIFT," ANGLE:",ANGLE_MODE," PREC:",PRECISION_MODE," FRACTION:",USE_FRACTION)
    print("MEM:",MEMORY," ANS:",ANS)
    print("""
1 Toggle SHIFT
2 Angle DEG/RAD
3 Precision Mode
4 Toggle Fraction Mode
5 Calculate Expression
6 Equation Solver
7 Rect -> Polar
8 Polar -> Rect
9 Memory M+
10 Memory M-
11 MR
12 MC
13 Multi-line History
0 Exit
""")

# ================= MAIN LOOP =================
while True:
    show_menu()
    choice = input("Select: ")

    if choice=="1":
        SHIFT = not SHIFT

    elif choice=="2":
        ANGLE_MODE = "RAD" if ANGLE_MODE=="DEG" else "DEG"

    elif choice=="3":
        m = input("NORM / FIX / SCI: ").upper()
        if m in ["NORM","FIX","SCI"]:
            PRECISION_MODE = m
            if m=="FIX":
                FIX_DECIMALS = int(input("Decimal places: "))

    elif choice=="4":
        USE_FRACTION = not USE_FRACTION
        print("Fraction Mode:",USE_FRACTION)

    elif choice=="5":
        print("Examples: 3+4, 3/4, sin(30), 5!, nCr(5,2), root(27,3), 200+10%")
        expr = input("Enter Expression: ")
        res = evaluate(expr)
        if not isinstance(res,str):
            history.append((expr,res))
            print("Result:",format_out(res))
        else:
            print(res)

    elif choice=="6":
        print("1 Linear ax+b=0")
        print("2 Quadratic ax²+bx+c=0")
        t = input("Type: ")
        if t=="1":
            a=float(input("a: "))
            b=float(input("b: "))
            print("x =", solve_linear(a,b))
        elif t=="2":
            a=float(input("a: "))
            b=float(input("b: "))
            c=float(input("c: "))
            x1,x2 = solve_quadratic(a,b,c)
            print("x1 =", x1)
            print("x2 =", x2)

    elif choice=="7":
        z = complex(input("Enter complex (ex 3+4j): "))
        r,t = rect_to_polar(z)
        print("Polar:",r,"∠",t)

    elif choice=="8":
        r = float(input("r: "))
        t = float(input("theta: "))
        print("Rect:",polar_to_rect(r,t))

    elif choice=="9":
        if history:
            MEMORY += history[-1][1]

    elif choice=="10":
        if history:
            MEMORY -= history[-1][1]

    elif choice=="11":
        print("MR:",MEMORY)

    elif choice=="12":
        mem_clear()

    elif choice=="13":
        print("\n=== HISTORY ===")
        for i,(e,r) in enumerate(history,1):
            print(f"{i}) {e} = {format_out(r)}")

    elif choice=="0":
        break
