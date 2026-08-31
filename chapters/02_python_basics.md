# Chapter 2: Python Basics & Syntax

## Comments in Python
Comments are portions of code completely ignored by the Python interpreter. They are used to explain logic, provide reminders, or temporarily disable lines during troubleshooting.

### Single-line Comments
Any text following a hash symbol (`#`) on a line is ignored:
```python
# Extract raw DNA sequence from sample pipeline
print("Processing FASTA record: GenBank_AC1234")  # Process header line
```

### Multi-line Comments
Python does not feature a dedicated multi-line comment symbol. You can create them in two ways:
1. Placing a `#` at the start of every line consecutively.
2. Using unassigned triple-quoted (`'''` or `"""`) multi-line string literals. 

```python
"""
Multi-line docstring:
Calculates transcript count and filters low-quality read pairs
before executing downstream variant calling.
"""
print("Quality filtering applied.")
```

> 💡 **Good Commenting Practice:** Write clear, concise comments. Avoid over-explaining obvious lines of code.

---

## Understanding Indentation
In Python, indentation refers to the whitespace characters at the very beginning of a code line. While other languages use curly braces `{}` to isolate functional blocks, Python uses indentation to group structural blocks together.

```python
if sequence_length > 100:
    # This indented block belongs inside the 'if' statement
    filter_passed_reads()
# This line is not indented, meaning it sits outside the block
log_pipeline_status()
```
Every line within the exact same structural block must share the exact same number of leading spaces. Inconsistent indentation triggers an `IndentationError`.

---

## Understanding Variables
Variables function as labeled containers used to store data values inside your computer's memory.

```text
Bookshelf Analogy:
[ Genomic Data ] ➔ Holds FASTA/FASTQ Files
[ Proteomics Data ] ➔ Holds PDB Coordinate Files
```

### Variable Assignment
To store a value inside a variable, use the assignment operator (`=`).
```python
read_depth = 150  # Assigns the integer 150 to a container named 'read_depth'
```

> 💡 **Dynamic Typing:** Python does not require you to explicitly declare what data type a variable holds. It calculates it automatically based on the value you provide.

### Storing Different Data Types
```python
read_depth = 150  # Integer (sequencing depth)
organism = "Staphylococcus aureus"  # String (bacterial species)
ph_levels = [6.8, 7.2, 7.4]  # List (experimental buffer pH measurements)
```

### Advanced Assignment Patterns
You can assign multiple variables simultaneously on a single line:
```python
pcr_temp, denaturation_time, extension_time = 95.0, 30, 60
# pcr_temp is 95.0, denaturation_time is 30, extension_time is 60
```

You can assign a matching value to multiple separate variables at once:
```python
buffer_concentration = stock_concentration = final_concentration = 50.0
```

### Boolean Data Type
Boolean variables store exactly one of two values: `True` or `False`. 
```python
has_signal_peptide = True
is_antimicrobial = False
print(type(has_signal_peptide))  # Output: <class 'bool'>
```
> ⚠️ **Syntax Note:** The keywords `True` and `False` must always begin with capital letters. Using lowercase text will trigger a runtime error.

---

## Processing User Input
To fetch real-time information from a user, evaluate the built-in `input()` function. Whatever a user submits is processed by Python strictly as a **string** data type.

```python
sample_id = input("Enter the sample ID: ")
```

### Converting Data Types
If your script requires numeric inputs for math calculations, cast the text string explicitly using `int()` or `float()` wrapper tools:

```python
dna_concentration_input = "55.4"  # Mock text input
dna_concentration = float(dna_concentration_input)  # Converted to a decimal number
```

### Complete Input Processing Script
Copy and run this sample tracking script to practice working with dynamic inputs:

```python
# 1. Prompt user for string inputs
dna_concentration_str = input("Enter the DNA concentration in ng/µL: ")
pcr_cycles_str = input("Enter the number of PCR cycles: ")

# 2. Convert text strings into matching numeric data types
dna_concentration = float(dna_concentration_str)
pcr_cycles = int(pcr_cycles_str)

# 3. Perform analysis: calculate exponential sample amplification
# Suppose each cycle doubles the total DNA amount
total_dna = dna_concentration * (2 ** pcr_cycles)

# 4. Display results using f-strings
print(f"Initial DNA concentration: {dna_concentration} ng/µL")
print(f"PCR cycles: {pcr_cycles}")
print(f"Predicted total DNA after PCR: {total_dna} ng/µL")
```
