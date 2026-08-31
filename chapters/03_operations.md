# Chapter 3: Python Operations & Operators

## Arithmetic Operators
These operators handle core quantitative math calculations using numeric operands:

* **Addition (`+`):** Sums two numerical values.
* **Subtraction (`-`):** Calculates the difference between numbers.
* **Multiplication (`*`):** Multiplies two numbers.
* **Division (`/`):** Divides values and **always** returns a floating-point decimal.
* **Floor Division (`//`):** Divides numbers and drops the fraction, returning only the integer quotient.
* **Modulus (`%`):** Evaluates division and returns the remaining remainder value.
* **Exponentiation (`**`):** Raises a base number to the power of a specified exponent.

### Example: Calculating Patient Body Mass Index (BMI)
```python
weight_kg = float(input("Enter weight of person (kg): "))
height_m = float(input("Enter height of person (meters): "))

# BMI Formula: weight divided by the square of height
bmi = weight_kg / (height_m ** 2)

print(f"BMI is {bmi:.2f}")
```

---

## Assignment Operators
Assignment operators are evaluated to update variable storage values. They are regularly combined with arithmetic operators as shorthand shortcuts:

* **Basic Assignment:** `=`
* **Arithmetic Updates:** `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

### Example: Updating Quantified DNA Volume
```python
dna_concentration = 50  # Initial concentration in ng/µL
dna_concentration += 10  # Concentration drops in 10 units after extraction step
print(dna_concentration)  # Output: 60
```

---

## Comparison Operators
Comparison (or relational) operators inspect two operands, check their logic, and return a strict boolean outcome (`True` or `False`):

* **Equal To:** `==`
* **Not Equal To:** `!=`
* **Greater Than / Less Than:** `>` / `<`
* **Greater Than or Equal / Less Than or Equal:** `>=` / `<=`

```python
binding_affinity_kd1 = 10.5  # Dissociation constant in nM
binding_affinity_kd2 = 12.1
print(binding_affinity_kd1 < binding_affinity_kd2)  # Check if binder 1 has higher affinity (Output: True)
```

### Example: Verifying Glucose Thresholds
```python
glucose_level = float(input("Enter glucose level of person: "))

if 70 <= glucose_level <= 100:
    print("Glucose level is normal.")
else:
    print("Glucose level is out of range.")
```

---

## Logical Operators
Logical operators are used to chain multiple distinct conditions together:

* **`and`:** Evaluates to `True` if **both** isolated conditions are met.
* **`or`:** Evaluates to `True` if **at least one** condition is met.
* **`not`:** Reverses and negates the boolean logic state.

### Example: Clinical Trial Screening Eligibility
```python
age = float(input("Enter age of person: "))
biomarker_level = float(input("Enter biomarker level of person: "))

# Condition: Age must be 18+ AND biomarker level must be above 5
if age >= 18 and biomarker_level > 5:
    print("Eligible for clinical trial")
else:
    print("Not eligible")
```

---

## The Walrus Operator (`:=`)
Introduced in Python 3.8, the **Walrus Operator** is known formally as **Assignment Expressions**. It allows you to assign a data value to a variable as part of a larger expression using the `name := expression` syntax. This saves you from writing separate assignment and conditional statements, making your code much more concise.

### Example: Streamlining Enzyme Activity Measurements
Compare how the Walrus operator shortens code by combining assignment and testing into a single step:

#### Standard Approach (Without Walrus)
```python
activity = float(input("Enter enzyme activity in units/mL: "))
if activity > 50:
    print("High enzyme activity detected.")
else:
    print("Enzyme activity is within normal range.")
```

#### Compact Approach (With Walrus)
```python
if (activity := float(input("Enter enzyme activity in units/mL: "))) > 50:
    print("High enzyme activity detected.")
else:
    print("Enzyme activity is within normal range.")
```
