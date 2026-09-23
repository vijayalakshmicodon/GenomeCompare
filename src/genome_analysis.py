from Bio import SeqIO


def read_genome(filename):
    record = SeqIO.read(filename, "fasta")

    return {
        "id": record.id,
        "description": record.description,
        "sequence": str(record.seq).upper()
    }


def genome_length(sequence):
    return len(sequence)


def gc_content(sequence):
    gc = sequence.count("G") + sequence.count("C")

    return (gc / len(sequence)) * 100


def nucleotide_counts(sequence):
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }