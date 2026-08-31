# Chapter 5: Functions in Python

## What is a Function?
A function is a reusable block of isolated code built to carry out a specific task. Defining functions helps you organize your script into manageable parts, minimizes bugs, improves readability, and avoids repeating code.

---

## Writing Custom Functions
To build custom reusable tools, follow these structured syntax rules:
1. Always start your block with the explicit `def` keyword.
2. Provide a descriptive, lowercase function name.
3. Place optional argument parameters inside parentheses `()`.
4. End the structural function header with a trailing colon (`:`).
5. Indent all core body code blocks consistently.
6. End with an optional `return` statement to send results back out of the function.

### Functional Blueprint Syntax
```python
def function_name(parameter1, parameter2):
    """Docstring describing function purpose."""
    # Code block execution logic
    return result
```

### Calling a Function
To trigger a function, call its exact name followed by matching arguments enclosed within parentheses:
```python
result = function_name(arg1, arg2)
```

### Example: Creating a Reusable BMI Calculator Function
```python
def calculate_bmi(weight_kg, height_m):
    # Calculate body mass using metrics
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Call the function with patient measurement parameters
patient_bmi = calculate_bmi(70, 1.75)
print(f"Patient BMI: {patient_bmi:.2f}")
```

---

## Built-In Functions
Python features a variety of pre-installed background functions ready for immediate use:

* **`print()`:** Outputs formatted data directly onto the screen.
* **`input()`:** Halts execution to read incoming text characters typed by a user.
* **`len()`:** Evaluates and returns the structural length count of an object container.
* **`type()`:** Inspects and returns the literal data class type of any variable.

### Example: Processing Genomic Sample IDs
```python
sample_id = input("Enter Sample ID: ")
# Measure the length of the raw input text string
print("Length of sample ID:", len(sample_id))
```

---

## Lambda Functions
Lambda functions are small, unnamed tools defined on a single line using the `lambda` keyword. They are perfect for short operations that don't require writing a full function block.

### Lambda Syntax
```python
lambda parameters: expression
```
> ⚠️ **Limitation:** Lambda functions can only handle a single expression. You cannot insert multiple statements or complex multi-line loops inside a lambda block.

### Example: Doubling Enzyme Concentration Calculations
```python
# Convert DNA length in base pairs to kilobases (kb)
bp_to_kb = lambda bp: bp / 1000

# Execute the lambda tool
result = bp_to_kb(4500)
print(f"{result} kb")  # Output: 4.5 kb
```
