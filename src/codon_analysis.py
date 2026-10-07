from collections import Counter


def get_codon_counts(sequence):
    sequence = sequence.upper()

    codons = [
        sequence[i:i + 3]
        for i in range(0, len(sequence) - 2, 3)
    ]

    valid_codons = [
        codon
        for codon in codons
        if all(base in "ATGC" for base in codon)
    ]

    return Counter(valid_codons)


def get_codon_usage(sequence):
    counts = get_codon_counts(sequence)

    total_codons = sum(counts.values())

    if total_codons == 0:
        return {}

    return {
        codon: count / total_codons * 100
        for codon, count in counts.items()
    }