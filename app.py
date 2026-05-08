from flask import Flask, render_template, request
from sequence_utils import detect_sequence, validate_sequence
from transcription import transcribe
from translation import translate
from protein_analysis import analyze_protein

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        sequence = request.form["sequence"]

        # validate
        if not validate_sequence(sequence):
            error = "Invalid sequence"
            return render_template("index.html", error=error)

        # detect DNA/RNA
        seq_type = detect_sequence(sequence)

        # transcription
        mrna = transcribe(sequence, seq_type)

        # translation
        codons, amino_acids = translate(mrna)

        # protein analysis
        protein_info = analyze_protein(amino_acids)

        result = {
            "type": seq_type,
            "mrna": mrna,
            "codons": codons,
            "amino_acids": amino_acids,
            "protein": protein_info
        }

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)