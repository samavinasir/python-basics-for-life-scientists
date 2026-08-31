# Chapter 7: Bioinformatics Applications & Visualization

This section focuses on core practical scripts that apply Python fundamentals to real-world biological datasets, visualizations, and file formats.

---

## Numerical Analysis: Modeling Exponential Bacterial Growth
Using math tools to predict growth parameters, population changes, and enzyme kinetics summaries.

```python
import math  # Import the built-in math module

initial_population = 1000
growth_rate = 0.3  # Growth rate per hour
hours = 6

# Formula: N(t) = N0 * e^(rt)
population = initial_population * math.exp(growth_rate * hours)

print(f"Population after {hours} hours: {population:.2f}")
```

---

## String Manipulation: Transcribing Sequences & Finding GC Content
Because biological sequences (DNA, RNA, proteins) are naturally represented as strings, you can analyze structural details using Python's built-in string methods.

```python
dna_seq = "ATGCTTGCCA"

# 1. Transcribe DNA to RNA by replacing Thymine with Uracil
rna_seq = dna_seq.replace("T", "U")

# 2. Calculate the sequence's GC content percentage
gc_count = dna_seq.count('G') + dna_seq.count('C')
gc_content = (gc_count / len(dna_seq)) * 100

print(f"RNA Sequence: {rna_seq}")
print(f"GC Content: {gc_content:.2f}%")
```

---

## Working with Libraries & Package Managers (`pip`)
While built-in modules are always available, third-party libraries (like Biopython or Pandas) are developed by the global community and must be installed separately.

### Installing Libraries via the Terminal
```bash
pip install bio
```
*Note: If you are working inside a Google Colab notebook cell, install the library by adding an exclamation mark at the start: `!pip install bio`*

### Managing Isolated Project Environments
Virtual environments allow you to isolate project dependencies so they don't conflict with your global computer settings.
```bash
# 1. Create a virtual environment named 'env'
python -m venv env

# 2. Activate the environment (Mac/Linux)
source env/bin/activate

# 3. Activate the environment (Windows)
env\Scripts\activate
```

---

## Parsing FASTA Genomic Files using Biopython
The script below uses Biopython's `SeqIO` module to open, parse, and analyze records from a standard FASTA sequence file.

```python
from Bio import SeqIO  # Import the sequence utility module

# Parse records from a local sample FASTA file
for record in SeqIO.parse("example.fasta", "fasta"):
    print(f"ID: {record.id}")
    print(f"Sequence Length: {len(record.seq)} bases")
```

---

## Visualizing Lab Data: Plotting Bacterial Growth Curves
Using Matplotlib to plot, format, and visualize experimental data points cleanly.

```python
import matplotlib.pyplot as plt  # Import the visualization module

# Experimental timeline data parameters
hours = [0, 1, 2, 3, 4, 5]
populations = [1000, 1500, 2200, 3300, 5000, 7500]

# Generate a formatted line chart line
plt.plot(hours, populations, marker='o', color='b', linestyle='-')

# Add descriptive label headers and styling
plt.xlabel('Hours')
plt.ylabel('Population')
plt.title('Bacterial Growth Curve')

# Display the finalized plot rendering
plt.show()
```
