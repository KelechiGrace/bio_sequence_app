
def validate_sequence(seq):
    seq = seq.upper()
    return all(base in "ATCGU" for base in seq)


def detect_sequence(seq):
    seq = seq.upper()

    if "U" in seq and "T" not in seq:
        return "RNA"
    elif "T" in seq:
        return "DNA"
    else:
        return "Unknown"