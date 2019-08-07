def triplets_with_sum(number):
    return {triple for triple in triplets_in_range(1, number // 2)
            if sum(triple) == number}


def triplets_in_range(start, end):
    for a in range(start, end):
        for b in range(a, end):
            for c in range(b, end):
                triple = (a, b, c)
                if is_triplet(triple):
                    yield triple


def is_triplet(triplet):
    a, b, c = triplet
    return (all(type(n) is int for n in triplet) and
            a ** 2 + b ** 2 == c ** 2)
