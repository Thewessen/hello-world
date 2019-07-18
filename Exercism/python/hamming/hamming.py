def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError(
            f'Strands {strand_a} and {strand_b} not equal in size'
        )
    return sum(a != b for (a, b) in zip(strand_a, strand_b))
