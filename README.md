\# GenomeCompare



GenomeCompare is a Python-based bioinformatics project for comparing bacterial genomes using Biopython and Matplotlib.



The project analyzes real bacterial reference genome sequences and compares:



\- Genome length

\- GC content

\- Nucleotide composition

\- Genome-wide statistics



It also generates visual comparison charts and a summary analysis report.



\## Bacterial Genomes



The project currently analyzes three bacterial genomes:



| Organism | Accession |

|---|---|

| Escherichia coli | NC\_000913.3 |

| Bacillus subtilis | NC\_000964.3 |

| Pseudomonas aeruginosa | NC\_002516.2 |



The genome sequences were obtained from the NCBI RefSeq database.



\## Features



\- FASTA genome parsing using Biopython

\- Genome length calculation

\- GC content calculation

\- A, T, G and C nucleotide counting

\- Comparison of multiple bacterial genomes

\- Automated comparison charts

\- Text-based analysis report

\- Unit tests for core analysis functions



\## Project Structure



```text

GenomeCompare/

│

├── data/

│   ├── e\_coli.fasta

│   ├── b\_subtilis.fasta

│   └── p\_aeruginosa.fasta

│

├── results/

│   ├── comparison\_report.txt

│   ├── gc\_comparison.png

│   ├── genome\_length\_comparison.png

│   └── nucleotide\_comparison.png

│

├── src/

│   ├── genome\_analysis.py

│   ├── compare\_genomes.py

│   └── visualization.py

│

├── tests/

│   └── test\_genome\_analysis.py

│

├── requirements.txt

├── .gitignore

└── README.md

