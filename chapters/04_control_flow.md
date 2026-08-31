# Chapter 4: Control Flow (Decision-Making & Loops)

## Decision-Making Structures
Decision statements let your scripts run different blocks of code based on shifting data conditions:

* **`if`:** Runs a block of code only if a specific condition evaluates to true.
* **`if-else`:** Standard binary decision structure that branches to an alternate block if the condition is false.
* **`if-elif-else`:** Multi-conditional ladder that tests step-by-step expressions until it finds a true condition.

### Example: High Blood Sugar Testing (`if`)
```python
glucose_level = float(input("Enter glucose level of patient: "))

if glucose_level > 100:
    print("Warning: High blood sugar level!")
```

### Example: Cholesterol Analysis (`if-else`)
```python
cholesterol = float(input("Enter cholesterol level of patient: "))

if cholesterol <= 200:
    print("Cholesterol level is normal.")
else:
    print("Cholesterol level is high.")
```

### Example: BMI Tier Categorization (`if-elif-else`)
```python
bmi = float(input("Enter BMI of patient: "))

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
```

---

## Loops in Python
Loops automate repetitive workflows by executing a block of code multiple times.

### For Loops
A `for` loop iterates over a **known sequence** or collection of distinct items (like a list, string, or numeric range) and runs once for each item.

#### Example: Processing Lab Protein Concentrations
```python
# List of measured protein values in µg/mL
protein_concentrations = [2.5, 3.0, 4.1, 3.8, 5.2]

# Iterate through every concentration measurement item sequentially
for concentration in protein_concentrations:
    print(f"Protein concentration: {concentration} µg/mL")
```

### While Loops
A `while` loop runs continuously as long as a **defined condition remains true**. Use this when the exact number of iterations is unknown and depends on changing data conditions.

#### Example: Monitoring Simulated Cell Growth
```python
cell_population = 1000  # Initial starting population
target_population = 5000  # Cutoff target count

# Loop until cell population meets or exceeds target
while cell_population < target_population:
    print(f"Current population: {cell_population}")
    
    # Simulate an exponential growth step (multiply population by 1.5 per cycle)
    cell_population *= 1.5
```
