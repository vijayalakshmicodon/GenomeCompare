from src.codon_analysis import get_codon_counts, get_codon_usage

import unittest

from src.genome_analysis import (
    genome_length,
    gc_content,
    nucleotide_counts
)

from src.compare_genomes import compare_genomes, calculate_differences


class TestGenomeAnalysis(unittest.TestCase):

    def test_genome_length(self):
        sequence = "ATGCATGC"
        self.assertEqual(genome_length(sequence), 8)

    def test_gc_content(self):
        sequence = "ATGCATGC"
        self.assertAlmostEqual(gc_content(sequence), 50.0)

    def test_nucleotide_counts(self):
        sequence = "AATTGGCC"

        expected = {
            "A": 2,
            "T": 2,
            "G": 2,
            "C": 2
        }

        self.assertEqual(
            nucleotide_counts(sequence),
            expected
        )

    def test_compare_genomes(self):
        results = compare_genomes(
            r"data/e_coli.fasta",
            r"data/b_subtilis.fasta"
        )

        self.assertEqual(len(results), 2)

        for genome_id, data in results.items():
            self.assertGreater(data["length"], 0)
            self.assertGreater(data["gc_content"], 0)
            self.assertLess(data["gc_content"], 100)

    def test_calculate_differences(self):
        results = {
            "Genome_A": {
                "length": 1000,
                "gc_content": 50.0,
                "nucleotide_counts": {
                    "A": 250,
                    "T": 250,
                    "G": 250,
                    "C": 250
                }
            },
            "Genome_B": {
                "length": 1200,
                "gc_content": 40.0,
                "nucleotide_counts": {
                    "A": 300,
                    "T": 300,
                    "G": 300,
                    "C": 300
                }
            }
        }

        differences = calculate_differences(results)

        self.assertEqual(
            differences["length_difference"],
            200
        )

        self.assertEqual(
            differences["gc_difference"],
            10.0
        )


    def test_codon_counts(self):
        sequence = "ATGGCCATGGCC"

        counts = get_codon_counts(sequence)

        self.assertEqual(counts["ATG"], 2)
        self.assertEqual(counts["GCC"], 2)

    def test_codon_usage(self):
        sequence = "ATGGCCATGGCC"

        usage = get_codon_usage(sequence)

        self.assertAlmostEqual(usage["ATG"], 50.0)
        self.assertAlmostEqual(usage["GCC"], 50.0)

if __name__ == "__main__":
    unittest.main()