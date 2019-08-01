def to_rna(dna_strand: str) -> str:
    """Given a DNA strand, return its RNA complement."""
    rna_trans = str.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(rna_trans)
