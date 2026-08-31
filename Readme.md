# 🧬 Python Programming Fundamentals for Life Scientists

> A beginner-friendly, open-source guide designed to teach Python programming through real-world biological datasets, lab calculations, and bioinformatics concepts.

---

## 📌 Overview

Traditional programming courses often rely on abstract examples like managing shopping carts or calculating circle areas. This repository takes a practical approach: **core Python concepts are introduced using biological data**, including DNA/RNA sequences, enzyme kinetics, cell populations, and patient clinical variables.

Whether you are a wet-lab biologist transitioning to computational research, a student learning data analysis, or a researcher aiming to automate daily workflows, this guide provides a structured foundation.

---

## 🎯 Target Audience

* **Perfect for:**
  * Life science students needing Python for coursework, data analysis, or thesis projects.
  * Lab researchers aiming to automate routine calculations, sequence processing, and plotting.
  * Biologists transitioning from Excel to reproducible, script-based workflows.
  * Absolute beginners with zero prior programming experience.

* **Not intended for:**
  * Experienced bioinformaticians looking for advanced NGS pipeline engineering or structural modeling architectures.

---

## 📚 What You Will Learn

* **Python Fundamentals:** Variables, dynamic typing, input processing, dynamic casting, and core syntax rules.
* **Control Flow & Logic:** Decision structures (`if-elif-else`), Walrus operator (`:=`), and repetitive task automation using loops.
* **Data Structures:** Lists, tuples, dictionaries (e.g., codon translation maps), sets (e.g., unique sequence extraction), and string manipulation.
* **Bioinformatics & Data Handling:** Reading/parsing FASTA records via Biopython, modeling exponential cell growth, and creating publication-ready line plots.

---

## 🗂️ Module Outline

| Chapter | Source File | Core Topics Covered | Practical Life Science Applications |
| :--- | :--- | :--- | :--- |
| **01** | [`01_introduction.md`](./chapters/01_introduction.md) | Python history, Py2 vs Py3, execution lifecycle (PVM/AST), ecosystem overview | Setting up Python environment, introduction to PySam, Biopython & DeepChem |
| **02** | [`02_python_basics.md`](./chapters/02_python_basics.md) | Comments, structural indentation rules, variables, dynamic typing, user input | Calculating exponential DNA amplification from PCR inputs |
| **03** | [`03_operations.md`](./chapters/03_operations.md) | Arithmetic, assignment, relational, logical operators, and the Walrus operator (`:=`) | Evaluating patient BMI, glucose ranges, clinical trial screening, & enzyme thresholds |
| **04** | [`04_control_flow.md`](./chapters/04_control_flow.md) | Decision logic (`if-elif-else`), `for` loops, and `while` loops | Cholesterol classification, patient BMI triage, & tracking simulated cell growth |
| **05** | [`05_functions.md`](./chapters/05_functions.md) | Function definitions (`def`), argument passing, built-in functions, and `lambda` expressions | Modularizing calculations (BMI, concentration adjustments) & sequence length checks |
| **06** | [`06_data_structures.md`](./chapters/06_data_structures.md) | Lists, tuples, dictionaries, sets, mutation mechanics, and mathematical set logic | Codon-to-amino acid translation maps, expression arrays, and unique DNA base extraction |
| **07** | [`07_bioinformatics.md`](./chapters/07_bioinformatics.md) | Math modeling, string manipulation, package management (`pip`), virtual environments, Biopython, Matplotlib | FASTA parsing (`SeqIO`), DNA-to-RNA transcription, GC-content calculations, & bacterial growth plotting |

---

## ⚡ Quickstart Code Example

Here is a preview showing how basic Python string manipulation and math translate into sequence analysis:

```python
# DNA Sequence Analysis & Transcription Shorthand
dna_seq = "ATGCTTGCCA"

# Transcribe DNA to RNA
rna_seq = dna_seq.replace("T", "U")

# Calculate GC Content Percentage
gc_count = dna_seq.count('G') + dna_seq.count('C')
gc_content = (gc_count / len(dna_seq)) * 100

print(f"RNA Sequence: {rna_seq}")
print(f"GC Content: {gc_content:.2f}%")

```
---

## 💻 Setup & Environment Installation

1. **Clone this repository:**
```bash
git clone [https://github.com/your-username/python-basics-for-life-scientists.git](https://github.com/your-username/python-basics-for-life-scientists.git)
cd python-for-life-scientists

```

2. **Create and activate a virtual environment:**
```bash
# Create environment named 'env'
python -m venv env

# Activate on macOS/Linux:
source env/bin/activate

# Activate on Windows:
env\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```

---

## 📄 License

Distributed under the MIT License. Feel free to use, adapt, and distribute for educational or research purposes.
