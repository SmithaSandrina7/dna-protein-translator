from translator import dna_to_rna, translate_dna

dna_sequences = [
    "ATGGAATTTTAA",
    "ATGGAAATGTTT"
]

for i, dna in enumerate(dna_sequences):
    print(f"\nSequence {i+1}")
    print("DNA:", dna)
    print("RNA:", dna_to_rna(dna))
    print("Protein:", translate_dna(dna))
