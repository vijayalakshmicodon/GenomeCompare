from src.codon_analysis import get_codon_counts, get_codon_usage

from pathlib import Path

from src.genome_analysis import (
    read_genome,
    genome_length,
    gc_content,
    nucleotide_counts
)

from src.visualization import (
    create_gc_comparison,
    create_nucleotide_comparison,
    create_genome_length_comparison
)


def compare_genomes(genome1_file, genome2_file):
    genome1 = read_genome(genome1_file)
    genome2 = read_genome(genome2_file)

    comparison = {
        genome1["id"]: {
            "length": genome_length(genome1["sequence"]),
            "gc_content": gc_content(genome1["sequence"]),
            "nucleotide_counts": nucleotide_counts(genome1["sequence"])
        },
        genome2["id"]: {
            "length": genome_length(genome2["sequence"]),
            "gc_content": gc_content(genome2["sequence"]),
            "nucleotide_counts": nucleotide_counts(genome2["sequence"])
        }
    }

    return comparison


def calculate_differences(results):
    lengths = [
        data["length"]
        for data in results.values()
    ]

    gc_values = [
        data["gc_content"]
        for data in results.values()
    ]

    return {
        "length_difference": max(lengths) - min(lengths),
        "gc_difference": max(gc_values) - min(gc_values)
    }
    genome_ids = list(results.keys())

    genome1 = results[genome_ids[0]]
    genome2 = results[genome_ids[1]]

    length_difference = abs(
        genome1["length"] - genome2["length"]
    )

    gc_difference = abs(
        genome1["gc_content"] - genome2["gc_content"]
    )

    return {
        "length_difference": length_difference,
        "gc_difference": gc_difference
    }


def create_summary_report(results, differences, output_file):

    genome_ids = list(results.keys())

    with open(output_file, "w") as file:

        file.write("GenomeCompare Analysis Report\n")
        file.write("=" * 35 + "\n\n")

        for genome_id, data in results.items():

            file.write(f"Genome: {genome_id}\n")
            file.write(
                f"Genome Length: {data['length']:,} bp\n"
            )
            file.write(
                f"GC Content: {data['gc_content']:.2f}%\n"
            )

            file.write("Nucleotide Counts:\n")

            for base, count in data["nucleotide_counts"].items():
                file.write(
                    f"  {base}: {count:,}\n"
                )

            file.write("\n")

        file.write("Comparison Summary\n")
        file.write("-" * 25 + "\n")

        file.write(
            f"Genome length range: "
            f"{differences['length_difference']:,} bp\n"
        )

        file.write(
            f"GC content range: "
            f"{differences['gc_difference']:.2f} "
            f"percentage points\n"
        )

if __name__ == "__main__":

    genome_files = [
        r"data/e_coli.fasta",
        r"data/b_subtilis.fasta",
        r"data/p_aeruginosa.fasta"
    ]

    results_folder = Path("results")
    results_folder.mkdir(exist_ok=True)

    results = {}

    for genome_file in genome_files:
        genome = read_genome(genome_file)

    results[genome["id"]] = {
        "length": genome_length(genome["sequence"]),
        "gc_content": gc_content(genome["sequence"]),
        "nucleotide_counts": nucleotide_counts(genome["sequence"]),
        "codon_counts": get_codon_counts(genome["sequence"]),
        "codon_usage": get_codon_usage(genome["sequence"])
    }

    differences = calculate_differences(results)

    print("\n================================")
    print("       GenomeCompare")
    print("================================")

    for genome_id, data in results.items():

        print(f"\nGenome: {genome_id}")
        print(f"Length: {data['length']:,} bp")
        print(f"GC Content: {data['gc_content']:.2f}%")

        print("Nucleotide Counts:")

        for base, count in data["nucleotide_counts"].items():
            print(f"  {base}: {count:,}")

    print("\n--------------------------------")
    print("Comparison Summary")
    print("--------------------------------")

    print(
        f"Genome length range: "
        f"{differences['length_difference']:,} bp"
    )

    print(
        f"GC content range: "
        f"{differences['gc_difference']:.2f} "
        f"percentage points"
    )

    gc_values = {
        genome_id: data["gc_content"]
        for genome_id, data in results.items()
    }

    length_values = {
        genome_id: data["length"]
        for genome_id, data in results.items()
    }

    create_gc_comparison(
        gc_values,
        results_folder / "gc_comparison.png"
    )

    create_nucleotide_comparison(
        results,
        results_folder / "nucleotide_comparison.png"
    )

    create_genome_length_comparison(
        length_values,
        results_folder / "genome_length_comparison.png"
    )

    create_summary_report(
        results,
        differences,
        results_folder / "comparison_report.txt"
    )

    print("\nCharts created successfully!")
    print("Comparison report created successfully!")
    print("Results saved in the results folder.")