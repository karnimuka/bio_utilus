# Bio Utilus

Python project for working with biological sequence files.

This project was developed as part of the Python course at the Institute of Bioinformatics.

## Author

Created by Nina Karamushka. 

## Features

The project contains three functions:

- **`filter_fastq()`** filters FASTQ reads by GC content, sequence length and average Phred33 quality.
- **`convert_multiline_fasta_to_oneline()`** converts multiline FASTA sequences into oneline format.
- **`parse_blast_output()`** extracts the best BLAST match description for each sample and saves the results in order.

## Installation

Clone the repository:

```bash
git clone git@github.com:karnimuka/bio_utilus.git
cd bio_utilus
```


## Usage

Import the functions from `main.py`:

```python
from main import filter_fastq, convert_multiline_fasta_to_oneline, parse_blast_output
```

### 1. FASTQ filtering

```python
filter_fastq("example_data/example_fastq.fastq", "filtered_reads.fastq")
```

The filtered reads are saved to the `filtered/` directory.

Default parameters:

- `gc_bounds=(0, 100)`
- `length_bounds=(0, 2**32)`
- `quality_threshold=0`


### 2. FASTA conversion

```python
convert_multiline_fasta_to_oneline("example_data/example_multiline_fasta.fasta")
```


### 3. BLAST results parsing

```python
parse_blast_output("example_data/example_blast_results.txt", "blast_proteins.txt")
```


## Project structure

```text
bio_utilus/
├── main.py
├── README.md
└── helpers/
    ├── fastq.py
    └── bio_files.py
```

- `main.py` main functions
- `helpers/fastq.py` reading and filtering helpers functions
- `helpers/bio_files.py` FASTA and BLAST helper functions

