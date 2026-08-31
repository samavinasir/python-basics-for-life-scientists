import json
import os
import re

# Source directory containing markdown chapters and target output directory
CHAPTERS_DIR = "chapters"
NOTEBOOKS_DIR = "notebooks"
os.makedirs(NOTEBOOKS_DIR, exist_ok=True)

# GitHub details for Google Colab badges
GITHUB_USER = "samavinasir"  # Replace with your GitHub username
REPO_NAME = "python-for-life-scientists"
BRANCH = "main"

def md_to_ipynb(md_path, ipynb_path, filename):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    cells = []
    
    # Add Google Colab interactive badge cell at the very top of each notebook
    colab_url = f"https://colab.research.google.com/github/{GITHUB_USER}/{REPO_NAME}/blob/{BRANCH}/{NOTEBOOKS_DIR}/{filename.replace('.md', '.ipynb')}"
    badge_md = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
    
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [badge_md + "\n"]
    })

    # Split markdown by Python code blocks
    parts = re.split(r'(```python[\s\S]*?```|```bash[\s\S]*?```)', content)

    for part in parts:
        if not part.strip():
            continue
        
        # Code cells (Python or Bash)
        if part.startswith("```python") or part.startswith("```bash"):
            lines = part.split("\n")[1:-1]
            # Convert bash commands into Jupyter magic commands for Colab compatibility
            processed_lines = []
            for line in lines:
                if part.startswith("```bash") and not line.startswith("!"):
                    processed_lines.append(f"!{line}\n")
                else:
                    processed_lines.append(line + "\n")
            
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": processed_lines
            })
        # Standard Markdown text cells
        else:
            lines = [line + "\n" for line in part.split("\n")]
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": lines
            })

    # Assemble Jupyter Notebook JSON structure
    notebook_json = {
        "cells": cells,
        "metadata": {
            "language_info": {"name": "python"},
            "orig_nbformat": 4
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

    with open(ipynb_path, "w", encoding="utf-8") as f:
        json.dump(notebook_json, f, indent=2)

# Run conversion across all chapters
for file in sorted(os.listdir(CHAPTERS_DIR)):
    if file.endswith(".md"):
        md_file_path = os.path.join(CHAPTERS_DIR, file)
        ipynb_file_path = os.path.join(NOTEBOOKS_DIR, file.replace(".md", ".ipynb"))
        md_to_ipynb(md_file_path, ipynb_file_path, file)
        print(f"Converted {file} -> {file.replace('.md', '.ipynb')}")