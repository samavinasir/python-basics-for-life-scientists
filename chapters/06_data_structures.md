# Chapter 6: Data Structures (Lists, Tuples, Dictionaries, Sets)

A data structure is a specialized format used to store, organize, and manage data so that computer programs can access and modify it efficiently.

---

## Lists and Tuples
Both lists and tuples are ordered collections that can hold multiple separate values of any data type (strings, numbers, or other structures) at the same time.

### Key Structural Differences
* **Lists:** Created using square brackets `[]`. They are **mutable**, meaning you can add, change, or delete individual items after creating the list.
* **Tuples:** Created using parentheses `()`. They are **immutable**, meaning their content cannot be changed once created.

```python
# List of gene expression level numbers
expression_levels = [5.2, 7.8, 6.1, 8.0]

# Tuple of sample IDs
sample_ids = ("S001", "S002", "S003")
```

### Indexes and Accessing Data
Lists and tuples are ordered sequentially starting from index `0`. You can extract values using single indexes or range slices (`[start:end]`):

```python
expression_levels = [5.2, 7.8, 6.1, 8.0]
sample_ids = ("S001", "S002", "S003")

# Extracting via direct position
print(expression_levels[0])  # Output: 5.2
print(sample_ids[2])          # Output: S003

# Advanced data slicing
print(expression_levels[1:3]) # Indexes 1 to 2 -> [7.8, 6.1]
print(sample_ids[:2])         # Start to index 1 -> ('S001', 'S002')
print(expression_levels[2:])  # Index 2 to the end -> [6.1, 8.0]
```

### Modifying Lists (Mutations)
```python
expression_levels = [5.2, 7.8, 6.1, 8.0]

# 1. Modify an existing value using its index
expression_levels[2] = 6.5  # Replaces 6.1 with 6.5

# 2. Append a new item to the very end of the list
expression_levels.append(9.1)

# 3. Delete an item using the 'del' statement and its index
del expression_levels[0]  # Removes index 0 (5.2)

# 4. Remove an item by matching its exact value instead of its index
expression_levels.remove(3.0)  # Searches for and drops the value 3.0
```
> ⚠️ **Tuple Safety Check:** If you run `sample_ids[0] = "S010"` on a tuple, Python will stop and throw a `TypeError`. However, you can delete an entire tuple container from memory using `del sample_ids`.

---

## Dictionaries
A dictionary is an **unordered collection** of elements stored as structured **key-value pairs**, much like a real-world dictionary. Dictionaries are mutable, but while values can be any object, keys must be completely unique and immutable (like strings or integers).

### Creating Dictionaries & Mapping Genetic Code
```python
# Map RNA codons to their corresponding single-letter amino acid codes
genetic_code = {
    "UUU": "F",  # Phenylalanine
    "UCU": "S",  # Serine
    "UAU": "Y",  # Tyrosine
    "UGU": "C"   # Cysteine
}
```

### Accessing Values
```python
# Method A: Bracket lookup (throws an error if the key is missing)
print(genetic_code["UUU"])  # Output: F

# Method B: .get() lookup (returns 'None' safely if the key is missing)
print(genetic_code.get("UAA"))  # Output: None
```

### Updating & Modifying Key-Value Pairs
```python
# 1. Add a new key-value entry
genetic_code["UAA"] = "*"  # Adds the stop codon entry

# 2. Update an existing key's value
genetic_code["UGU"] = "Sec"  # Updates Cysteine to Selenocysteine

# 3. Delete a targeted entry using its key
del genetic_code["UCU"]

# 4. Wipe an entire dictionary from memory
del genetic_code
```

### Iterating Over Dictionaries
```python
for codon, amino_acid in genetic_code.items():
    print(f"{codon} codes for {amino_acid}")
```

---

## Sets
A set is an **unordered collection** containing strictly **unique elements**. Sets are mutable, but their contents must be immutable types. They are great for removing duplicates and running mathematical set operations.

### Creating Sets & Finding Unique DNA Bases
```python
# Convert a sequence string into a set using the set() constructor
dna_sequence = "AGCTTAGCGA"
unique_bases = set(dna_sequence)

print(unique_bases)  # Output: {'A', 'G', 'T', 'C'} (Duplicates are automatically removed)
```

### Mathematical Set Operations
```python
# Patient cohort variant SNP sets
cohort_a_variants = {"rs1234", "rs5678", "rs9101"}
cohort_b_variants = {"rs5678", "rs1122", "rs9101"}

# Union: Total unique SNPs across both cohorts
print(cohort_a_variants.union(cohort_b_variants))

# Intersection: Shared SNPs found in both cohorts
print(cohort_a_variants.intersection(cohort_b_variants))  # Output: {'rs5678', 'rs9101'}

# Difference: SNPs unique strictly to Cohort A
print(cohort_a_variants.difference(cohort_b_variants))    # Output: {'rs1234'}
```

### Modifying Sets
```python
unique_bases = {"A", "C", "G", "T"}

unique_bases.add("U")       # Adds Uracil to the set
unique_bases.remove("T")    # Removes Thymine (Throws an error if not found)
unique_bases.discard("X")   # Safely drops "X" without an error if it's missing
```
