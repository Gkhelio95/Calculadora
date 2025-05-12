# Basic Calculator in Python, Java, and JavaScript

This project implements a basic calculator in three different programming languages: Python, Java, and JavaScript. Each implementation supports the four fundamental operations: addition, subtraction, multiplication, and division. Unit tests are included to ensure correct functionality across different scenarios.

---

## Python Calculator

### File: `calculadora.py`

Implements standalone functions:

- `sumar(n1, n2)`: Returns the sum of two numbers.
- `restar(n1, n2)`: Returns the difference of two numbers.
- `multiplicar(n1, n2)`: Returns the product of two numbers.
- `dividir(n1, n2)`: Returns the quotient or raises an exception if `n2` is zero.

### Tests: `test_calculadora.py`

Uses the `unittest` module and includes:

- Standard cases with integers and decimals.
- Negative number operations.
- Division by zero (expects a raised exception).

Run with:

```bash
python -m unittest test_calculadora.py
