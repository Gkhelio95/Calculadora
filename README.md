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

# Java Calculator

This project is a simple calculator written in Java that supports basic operations: addition, subtraction, multiplication, and division. It also includes a set of unit tests using JUnit 5.

## How It Works

The `Calculadora` class has four methods: `sumar` (add), `restar` (subtract), `multiplicar` (multiply), and `dividir` (divide). The `dividir` method throws an exception if division by zero is attempted.

## Tests

The tests are written in the `CalculadoraTest.java` class using JUnit 5. Each operation is tested to ensure it returns the expected result, and division by zero is checked to correctly throw an exception.

# JavaScript Calculator

This project implements a basic calculator in JavaScript that supports simple mathematical operations: addition, subtraction, multiplication, and division. It also includes automated unit tests using Jest.

## Features

The Calculator class provides the following methods:

- `add(a, b)`: returns the sum of a and b
- `subtract(a, b)`: returns the result of a minus b
- `multiply(a, b)`: returns the product of a and b
- `divide(a, b)`: returns the result of a divided by b. Throws an error if b is 0

## Requirements

- Node.js
- npm

## Installation

1. Clone the repository or copy the files into a directory
2. Open a terminal in the project folder
3. Run:

```bash
npm install


Run with:

```bash
