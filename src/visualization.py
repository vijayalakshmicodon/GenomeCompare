import matplotlib.pyplot as plt


def create_gc_comparison(gc_values, output_file):
    genomes = list(gc_values.keys())
    values = list(gc_values.values())

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(genomes, values)

    ax.set_title("GC Content Comparison")
    ax.set_xlabel("Genome")
    ax.set_ylabel("GC Content (%)")
    ax.set_ylim(0, 100)

    for genome, value in zip(genomes, values):
        ax.text(
            genome,
            value,
            f"{value:.2f}%",
            ha="center",
            va="bottom"
        )

    fig.tight_layout()
    fig.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close(fig)


def create_nucleotide_comparison(genome_data, output_file):
    genomes = list(genome_data.keys())
    bases = ["A", "T", "G", "C"]

    x = range(len(genomes))
    width = 0.2

    fig, ax = plt.subplots(figsize=(9, 5))

    for i, base in enumerate(bases):
        values = [
            genome_data[genome]["nucleotide_counts"][base]
            for genome in genomes
        ]

        positions = [
            position + (i - 1.5) * width
            for position in x
        ]

        ax.bar(
            positions,
            values,
            width=width,
            label=base
        )

    ax.set_title("Nucleotide Composition Comparison")
    ax.set_xlabel("Genome")
    ax.set_ylabel("Nucleotide Count")

    ax.set_xticks(list(x))
    ax.set_xticklabels(genomes)

    ax.legend()

    fig.tight_layout()
    fig.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close(fig)


def create_genome_length_comparison(length_values, output_file):
    genomes = list(length_values.keys())
    values = list(length_values.values())

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(genomes, values)

    ax.set_title("Genome Length Comparison")
    ax.set_xlabel("Genome")
    ax.set_ylabel("Genome Length (bp)")

    for genome, value in zip(genomes, values):
        ax.text(
            genome,
            value,
            f"{value:,}",
            ha="center",
            va="bottom"
        )

    fig.tight_layout()
    fig.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close(fig)