# Advanced Scientific Calculator (Python)

This project is a powerful, menu-driven scientific calculator built in Python.
It replicates many features found in advanced Casio calculators and extends them
with programmable flexibility.

The calculator runs in the terminal and supports real numbers, fractions,
complex numbers, trigonometry, combinatorics, equation solving, and more.

---

## Features

### Core Calculation
- Basic arithmetic (+, -, ×, ÷, powers)
- Scientific notation and fixed precision modes
- ANS support (previous answer)
- History tracking (multi-line)

### Trigonometry
- sin, cos, tan
- SHIFT mode for inverse functions
- DEG / RAD angle modes

### Logarithmic Functions
- log (base 10)
- ln (natural log)
- SHIFT mode for antilog and exp

### Fractions
- Toggle Fraction Mode
- Automatic fraction simplification
- Mixed float and fraction handling

### Factorial & Combinatorics
- Factorial (!)
- nCr (combinations)
- nPr (permutations)

### Percentage (Casio-style)
- 200 + 10%
- 200 - 10%
- 200 × 10%
- 200 ÷ 10%

### Complex Numbers
- Complex arithmetic
- Rectangular ↔ Polar conversion
- Support for `j` notation

### Roots & Powers
- Square root
- nth root (root(x, n))

### Equation Solver
- Linear equations (ax + b = 0)
- Quadratic equations (ax² + bx + c = 0)
- Real and complex roots

### Memory Functions
- M+
- M-
- MR
- MC

---

## Example Inputs

3 + 4
3/4
sin(30)
SHIFT + sin → asin(0.5)
5!
nCr(5,2)
root(27,3)
200 + 10%
3 + 4j
---

## How to Run

1. Make sure Python 3.8+ is installed
2. Save the file as `calculator.py`
3. Run:

This project is ideal for:
Learning expression parsing and evaluation
Understanding scientific calculator logic
Exploring safe eval() usage
Practicing Python math, cmath, and fractions
Extending into GUI (Tkinter / PyQt)
Embedding into hardware or microcontroller projects

Future Enhancements
GUI interface
Graph plotting
Matrix operations
Unit conversions
Custom expression parser (Shunting Yard)
Persistent memory storage
