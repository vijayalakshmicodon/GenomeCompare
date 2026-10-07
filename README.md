# GenomeCompare

GenomeCompare is a Python-based bioinformatics project for analyzing and comparing bacterial genome sequences using Biopython and Matplotlib.

The project works with real bacterial reference genome sequences and calculates important genomic features such as genome length, GC content, nucleotide composition, and codon usage.

## Genomes Analyzed

The project currently includes:

| Organism | Accession |
|---|---|
| Escherichia coli | NC_000913.3 |
| Bacillus subtilis | NC_000964.3 |

The genome sequences were obtained from the NCBI RefSeq database.

## Features

- FASTA sequence parsing using Biopython
- Genome length calculation
- GC content calculation
- A, T, G and C nucleotide counting
- Comparative analysis of bacterial genomes
- Codon usage analysis
- Generation of genome comparison charts
- Text-based comparison report
- Unit tests for core analysis functions

## Analysis Performed

### Genome Statistics

The project calculates basic genome statistics including:

- Total genome length
- GC percentage
- Nucleotide composition
- Relative nucleotide frequencies

### Codon Usage Analysis

The project also analyzes coding sequences to determine codon usage patterns.

This includes:

- Codon frequency calculation
- Comparison of codon usage
- Identification of commonly used codons
- Codon usage statistics for genome analysis

## Results

The analysis generates visualizations and a summary report for comparing the genomes.

Example outputs include:

- GC content comparison
- Genome length comparison
- Nucleotide composition comparison
- Codon usage analysis
- Genome comparison report

## Technologies Used

- Python
- Biopython
- Matplotlib
- Unittest
- Git & GitHub

## Project Structure

```text
GenomeCompare/
│
├── data/
│   ├── e_coli.fasta
│   ├── e_coli.fasta.gz
│   ├── b_subtilis.fasta
│   └── b_subtilis.fasta.gz
│
├── results/
│   ├── comparison_report.txt
│   ├── gc_comparison.png
│   ├── genome_length_comparison.png
│   ├── nucleotide_comparison.png
│
├── src/
│   ├── genome_analysis.py
│   ├── compare_genomes.py
│   ├── visualization.py
│   └── codon_analysis.py
│
├── tests/
│   └── test_genome_analysis.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Data Source

Genome sequences were obtained from the NCBI RefSeq database using publicly available bacterial reference genome records.

The accession numbers used in this project are:

- E. coli — NC_000913.3
- B. subtilis — NC_000964.3

## Purpose

The main purpose of GenomeCompare is to apply Python programming to real biological sequence data and demonstrate basic computational biology and bioinformatics workflows.

The project provides practical experience in:

- Biological sequence handling
- Genome analysis
- Comparative genomics
- Codon usage analysis
- Data visualization
- Automated testing

## Future Improvements

Possible future improvements include:

- Adding more bacterial genomes
- Adding protein sequence analysis
- Detecting genomic regions with unusual GC content
- Adding gene-level comparisons
- Creating an interactive genome comparison dashboard
- Adding more advanced codon usage metrics

## Author

S. Vijaya Lakshmi

B.Tech Biotechnology
