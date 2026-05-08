def analyze_protein(amino_acids):
    protein_chain = [a for a in amino_acids if "Stop" not in a]

    return {
        "chain": protein_chain,
        "length": len(protein_chain),
        "note": "Protein analysis simulated (can extend with UniProt API later)"
    }