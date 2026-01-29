def dna_to_rna(dna):
    """
    Converts DNA sequence to RNA sequence.
    """
    return dna.replace("T", "U")


def translate_dna(dna):
    """
    Translates DNA sequence into a protein sequence.
    """
    codon_table = {
        "ATG": "M",
        "GAA": "E",
        "TTT": "F",
        "TAA": "STOP"
    }

    protein = ""

    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]

        if codon not in codon_table:
            break

        if codon_table[codon] == "STOP":
            break

        protein += codon_table[codon]

    return protein
