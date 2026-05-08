def transcribe(seq, seq_type):
    seq = seq.upper()

    # DNA coding strand → RNA
    if seq_type == "DNA":
        return seq.replace("T", "U")

    # DNA template strand (simple assumption for project)
    elif seq_type == "RNA":
        return seq

    return seq