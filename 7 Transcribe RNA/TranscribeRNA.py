### MADE by Exercism and its contributors
### https://github.com/exercism/python
transcribe = str.maketrans('GCTA', "CGAU")
def to_rna(RNA):
    # RNA Transcription
    # Given a DNA strand, return its RNA complement (per RNA transcription).

    # Both DNA and RNA strands are a sequence of nucleotides.

    # The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).

    # The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).

    # Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

    # G -> C
    # C -> G
    # T -> A
    # A -> U
    try:
        return (RNA.translate(transcribe))
    except NameError:
        return ""