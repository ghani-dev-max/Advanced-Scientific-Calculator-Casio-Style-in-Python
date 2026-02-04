# Advanced Scientific Calculator (Casio Style) - Python

## Overview

This project is a full advanced scientific calculator built using Python.  
It is designed to simulate many features of real Casio scientific calculators while also providing extra programmable flexibility.

The calculator runs in terminal / command line and supports real numbers, fractions, complex numbers, trigonometry, combinatorics, equation solving, memory operations, and precision control.

---

## Key Features

### Basic Math
- Addition, Subtraction, Multiplication, Division
- Power and Roots
- Casio style percentage calculations
- ANS (previous answer recall)

---

### Trigonometry
- sin, cos, tan
- SHIFT mode for inverse functions (asin, acos, atan)
- DEG / RAD angle mode switching

---

### Logarithmic Functions
- log (base 10)
- ln (natural logarithm)
- SHIFT mode:
  - Antilog (10^x)
  - e^x

---

### Fraction Mode
- Toggle fraction output
- Auto fraction conversion
- Simplified fraction results

---

### Factorial and Combinatorics
- Factorial (!)
- nCr (Combination)
- nPr (Permutation)

---

### Complex Numbers
- Full complex arithmetic support
- Rectangular → Polar conversion
- Polar → Rectangular conversion
- Uses Python complex `j` notation

---

### Equation Solver
Supports:

**Linear Equations**
```
ax + b = 0
```

**Quadratic Equations**
```
ax² + bx + c = 0
```
Handles real and complex roots automatically.

---

### Memory Functions
- M+ → Add to memory
- M- → Subtract from memory
- MR → Recall memory
- MC → Clear memory

---

### Output Precision Modes
- NORM → Normal display
- FIX → Fixed decimal places
- SCI → Scientific notation

---

### History System
- Stores previous calculations
- Multi-line history viewer

---

## Example Expressions

```
3 + 4
3 / 4
sin(30)
5!
nCr(5,2)
root(27,3)
200 + 10%
3 + 4j
```

---

## Requirements

- Python 3.8 or higher

Libraries used:
- math
- cmath
- fractions
- re

(All are built-in Python libraries)

---

## How To Run

### Step 1: Download / Clone Project

```
git clone https://github.com/yourusername/advanced-scientific-calculator.git
```

### Step 2: Navigate to Folder

```
cd advanced-scientific-calculator
```

### Step 3: Run Program

```
python calculator.py
```

---

## Project Structure

```
project/
│
├ calculator.py
├ README.md
```

---

## Learning Objectives

This project helps in learning:

- Scientific calculator logic design
- Safe expression evaluation
- Python math and numerical libraries
- Complex number operations
- Fraction mathematics
- CLI program design

---

## Possible Future Improvements

- GUI Version (Tkinter / PyQt)
- Graph plotting calculator
- Matrix calculator
- Unit converter
- Custom math expression parser (Shunting Yard Algorithm)
- Save history to file
- Persistent memory storage

---

## Contribution

You can fork, modify, and extend this project for learning or development.

---

## License

Open source for educational and personal use.
