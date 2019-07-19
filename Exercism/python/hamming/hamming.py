def distance(strand_a: str, strand_b: str) -> int:
    """Calculates the Hamming Distance between two DNA strands.
    For example:
        GAGCCTACTAACGGGAT
        CATCGTAATGACGGCCT
        ^ ^ ^  ^ ^    ^^
    They have 7 differences, and therefore the Hamming Distance is 7."""
    if (len(strand_a) != len(strand_b)):
        raise ValueError(
            f'Strands {strand_a} and {strand_b} not equal in size'
        )
    return sum(a != b for a, b in zip(strand_a, strand_b))
