from itertools import zip_longest


def transpose(lines):
    rows = lines.split("\n")
    lines = list(line.ljust(max(len(l) for l in rows[i+1:]), " ")
                 for i, line in enumerate(rows[:-1])) + [rows[-1]]
    return "\n".join("".join(row) for row in
                     zip_longest(*lines, fillvalue=" "))
