def translate(mrna):
    codons = []
    amino_acids = []

    codon_table = {
        "AUG": "Methionine (Start)",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UAA": "Stop",
        "UAG": "Stop",
        "UGA": "Stop"
    }

    for i in range(0, len(mrna), 3):
        codon = mrna[i:i+3]
        if len(codon) == 3:
            codons.append(codon)
            amino_acids.append(codon_table.get(codon, "Unknown"))

    return codons, amino_acids