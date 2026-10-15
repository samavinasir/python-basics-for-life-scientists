# 🧬 Python Programming Fundamentals for Life Scientists

> A beginner-friendly, open-source guide designed to teach Python programming through real-world biological datasets, lab calculations, and bioinformatics concepts.

---

<a name="overview"></a>
<img src="assets\banners\01-overview.svg" alt="01 / Features" width="100%" />


Traditional programming courses often rely on abstract examples like managing shopping carts or calculating circle areas. This repository takes a practical approach: **core Python concepts are introduced using biological data**, including DNA/RNA sequences, enzyme kinetics, cell populations, and patient clinical variables.

Whether you are a wet-lab biologist transitioning to computational research, a student learning data analysis, or a researcher aiming to automate daily workflows, this guide provides a structured foundation.

<details>
<summary><b>🖼️ Browse all 6 slides</b></summary>
<br />

<div align="center">

<img src="assets\slide-1.png" alt="Slide 1" width="48%" />
<img src="assets\slide-2.png" alt="Slide 2" width="48%" />
<img src="assets\slide-3.png" alt="Slide 3" width="48%" />
<img src="assets\slide-4.png" alt="Slide 4" width="48%" />
<img src="assets\slide-5.png" alt="Slide 5" width="48%" />
<img src="assets\slide-6.png" alt="Slide 6" width="48%" />

</div>

</details>

---

<a name="target-audience"></a>
<img src="assets\banners\02-who-this-content-is-for.svg" alt="02 / Features" width="100%" />


* **Perfect for:**
  * Life science students needing Python for coursework, data analysis, or thesis projects.
  * Lab researchers aiming to automate routine calculations, sequence processing, and plotting.
  * Biologists transitioning from Excel to reproducible, script-based workflows.
  * Absolute beginners with zero prior programming experience.

* **Not intended for:**
  * Experienced bioinformaticians looking for advanced NGS pipeline engineering or structural modeling architectures.

---

<a name="what-you-will-learn"></a>
<img src="assets\banners\03-key-takeaways-and-insights.svg" alt="03 / Features" width="100%" />

* **Python Fundamentals:** Variables, dynamic typing, input processing, dynamic casting, and core syntax rules.
* **Control Flow & Logic:** Decision structures (`if-elif-else`), Walrus operator (`:=`), and repetitive task automation using loops.
* **Data Structures:** Lists, tuples, dictionaries (e.g., codon translation maps), sets (e.g., unique sequence extraction), and string manipulation.
* **Bioinformatics & Data Handling:** Reading/parsing FASTA records via Biopython, modeling exponential cell growth, and creating publication-ready line plots.

---

<a name="module-outline"></a>
<img src="assets\banners\04-structure-and-main-topics.svg" alt="04 / Features" width="100%" />


| Chapter | Markdown Source | Interactive Colab Notebook | Key Life Science Applications |
| :--- | :--- | :--- | :--- |
| **01** | [`01_introduction.md`](./chapters/01_introduction.md) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samavinasir/python-basics-for-life-scientists/blob/main/notebooks/01_introduction.ipynb) | PySam, Biopython, DeepChem setup & execution lifecycle |
| **02** | [`02_python_basics.md`](./chapters/02_python_basics.md) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samavinasir/python-basics-for-life-scientists/blob/main/notebooks/02_python_basics.ipynb) | Calculating exponential DNA amplification from PCR inputs |
| **03** | [`03_operations.md`](./chapters/03_operations.md) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samavinasir/python-basics-for-life-scientists/blob/main/notebooks/03_operations.ipynb) | Evaluating patient BMI, glucose thresholds, & enzyme logic |
| **04** | [`04_control_flow.md`](./chapters/04_control_flow.md) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samavinasir/python-basics-for-life-scientists/blob/main/notebooks/04_control_flow.ipynb) | Cholesterol classification & tracking cell growth loops |
| **05** | [`05_functions.md`](./chapters/05_functions.md) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samavinasir/python-basics-for-life-scientists/blob/main/notebooks/05_functions.ipynb) | Modularizing BMI tools & sequence length evaluation |
| **06** | [`06_data_structures.md`](./chapters/06_data_structures.md) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samavinasir/python-basics-for-life-scientists/blob/main/notebooks/06_data_structures.ipynb) | Codon maps, expression vectors, & unique DNA base extraction |
| **07** | [`07_bioinformatics.md`](./chapters/07_bioinformatics.md) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/samavinasir/python-basics-for-life-scientists/blob/main/notebooks/07_bioinformatics.ipynb) | FASTA parsing, DNA-to-RNA conversion, & bacterial growth plotting |
---

<a name="quickstart-code"></a>
<img src="assets\banners\05-fast-implementation-snippet.svg" alt="05 / Features" width="100%" />


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

<a name="setup-and-installation"></a>
<img src="assets\banners\06-steps-to-configure-workspace.svg" alt="06 / Features" width="100%" />


1. **Clone this repository:**
```bash
git clone https://github.com/samavinasir/python-basics-for-life-scientists.git
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

<a name="Licence"></a>
<img src="assets\banners\07-license.svg" alt="07 / Features" width="100%" />


Distributed under the MIT License. Feel free to use, adapt, and distribute for educational or research purposes.
