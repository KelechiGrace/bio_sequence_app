

def translate(mrna):
    codon_table = {
        # Phenylalanine
        "UUU": "Phenylalanine", "UUC": "Phenylalanine",

        # Leucine
        "UUA": "Leucine", "UUG": "Leucine",
        "CUU": "Leucine", "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine",

        # Serine
        "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
        "AGU": "Serine", "AGC": "Serine",

        # Tyrosine
        "UAU": "Tyrosine", "UAC": "Tyrosine",

        # Stop codons
        "UAA": "Stop", "UAG": "Stop", "UGA": "Stop",

        # Cysteine
        "UGU": "Cysteine", "UGC": "Cysteine",

        # Tryptophan
        "UGG": "Tryptophan",

        # Proline
        "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",

        # Histidine
        "CAU": "Histidine", "CAC": "Histidine",

        # Glutamine
        "CAA": "Glutamine", "CAG": "Glutamine",

        # Arginine
        "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine",
        "AGA": "Arginine", "AGG": "Arginine",

        # Isoleucine
        "AUU": "Isoleucine", "AUC": "Isoleucine", "AUA": "Isoleucine",

        # Methionine (Start)
        "AUG": "Methionine (Start)",

        # Threonine
        "ACU": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",

        # Asparagine
        "AAU": "Asparagine", "AAC": "Asparagine",

        # Lysine
        "AAA": "Lysine", "AAG": "Lysine",

        # Valine
        "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine",

        # Alanine
        "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",

        # Aspartic Acid
        "GAU": "Aspartic Acid", "GAC": "Aspartic Acid",

        # Glutamic Acid
        "GAA": "Glutamic Acid", "GAG": "Glutamic Acid",

        # Glycine
        "GGU": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine"
    }

    codons = []
    amino_acids = []

    for i in range(0, len(mrna), 3):
        codon = mrna[i:i+3]
        if len(codon) == 3:
            codons.append(codon)
            amino_acids.append(codon_table.get(codon, "Unknown"))

    return codons, amino_acids