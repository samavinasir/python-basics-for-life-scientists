# Chapter 1: Introduction to Python

## What is Python?
Python is a high-level programming language designed to instruct computers to perform tasks using clear and simple instructions. It is an easy-to-learn, powerful language that closely resembles human language. 

Python is free and open-source, allowing anyone to view, modify, and share its source code. It was created by Guido van Rossum and first released in 1991.

### Object-Oriented Programming (OOP)
Python supports Object-Oriented Programming (OOP). This is a method for organizing data and functions into self-contained objects, making code easier to manage, understand, and debug. 

This encapsulation ensures that different parts of a program can operate independently and can be reused. This allows programmers to build on existing code without rewriting it, speeding up development and reducing redundancy.

---

## Versions of Python
Currently, Python has 2 main versions:
1. **Python 2 (Py2)** — Released in 2000
2. **Python 3 (Py3)** — Released in 2008 as an improved version

> ⚠️ **Recommendation:** Python 3 is the standard version used in modern programming practices.

### Major Differences Between Py2 and Py3
* **Programming Paradigm:** Python 2 relies more on structured programming, whereas Python 3 is highly object-oriented.
* **The Print Feature:** Py2 uses a `print` statement without parentheses (`print "Hello"`). Py3 treats it as a function requiring parentheses (`print("Hello")`).
* **Integer Division:** In Py2, dividing integers returns a floored integer (e.g., `5/2` equals `2`). In Py3, it returns a precise float (`5/2` equals `2.5`).
* **String Storage:** Py3 stores strings as Unicode by default, whereas Py2 defaults to ASCII.
* **Keywords:** Py3 introduced the explicit `as` keyword.

---

## How Python Works
The Python interpreter processes and translates your code using the following lifecycle:

```text
[Source Code (.py)] ➔ [Lexical Analysis] ➔ [Parsing (AST)] ➔ [Bytecode (.pyc)] ➔ [PVM Execution] ➔ [Output]
```

1. **Source Code:** The programmer writes readable code and saves it in a `.py` file.
2. **Lexical Analysis:** The interpreter tokenizes the source code into basic components like keywords, operators, and literals.
3. **Parsing:** Tokens are arranged into an **Abstract Syntax Tree (AST)** to represent logical execution structures.
4. **Bytecode Compilation:** The AST is converted into platform-independent bytecode stored temporarily in `.pyc` files.
5. **Execution:** The **Python Virtual Machine (PVM)** reads the bytecode, handles memory management, executes stack operations, and translates it into machine-specific instructions.
6. **Output:** The final computed results or text displays on the screen.

---

## What are Python Libraries?
Python libraries are collections of pre-written modules that provide ready-to-use functions, classes, and methods. They stop you from having to write code from scratch.

### General Core Libraries
* **Pandas:** Used for manipulating structured data via DataFrames and Series.
* **NumPy:** Provides core support for large multidimensional arrays and mathematical computations.
* **SciPy:** Built on NumPy for advanced scientific computing tasks like optimization.
* **Matplotlib:** Handles static, animated, and interactive data visualizations.
* **Scikit-learn:** A library offering simple machine learning tools for classification and clustering.
* **TensorFlow:** Developed by Google for building deep learning architectures.
* **Requests:** Simplifies making HTTP web requests and interacting with APIs.
* **OpenCV:** Specialized framework for computer vision and processing image data.
* **Flask & Django:** Web frameworks used to build light APIs or production-scale applications.

### Specialized Bioinformatics Libraries
* **Biopython:** The premier toolkit for sequence input/output (parsing FASTA files), sequence alignment, and biological database indexing.
* **Pysam:** Provides a direct interface to read, manipulate, and write raw genomic formats like SAM, BAM, VCF, and BCF.
* **DeepChem:** Applies deep learning models directly to drug discovery pipelines and chemistry datasets.
* **Biotite:** Unifies popular molecular biology tasks, sequence/structure integrations, and structural graphics.
* **MDAnalysis:** A package specifically designed to evaluate complex molecular dynamics simulations and protein-ligand tracking.

---

## Installation & Environment Setup
1. Visit the official [Python Website](https://python.org) and download the latest stable release.
2. **Critical Step:** During installation, check the box that says **"Add Python to PATH"**.
3. Verify your installation by opening a terminal or command prompt and running:
   ```bash
   python --version
   ```

### Where to Write Code
* **IDLE:** Python's built-in basic script editor.
* **IDEs:** Advanced software environments like VS Code, PyCharm, or Spyder.
* **Jupyter Notebook:** An interactive web dashboard that breaks code into single "cells", allowing you to view graphs and data tables inline alongside standard text. Install it using:
   ```bash
   pip install notebook
   ```
* **Google Colab:** A cloud-hosted Jupyter environment managed by Google. It requires zero computer configuration and offers free remote access to high-performance GPU hardware.

---

## Writing Our First Python Program
Let's start the journey by executing the classic "Hello World" routine using the built-in `print()` function:

```python
print("FASTA parsing initialization complete.")
# Output: FASTA parsing initialization complete.
```
