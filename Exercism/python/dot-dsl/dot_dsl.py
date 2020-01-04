NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        data = data or list()
        self.nodes = list()
        self.edges = list()
        self.attrs = dict()
        if any(len(g) < 2 for g in data) or type(data) != list:
            raise TypeError("Invalid data")
        for (t, *args) in data:
            if t == NODE:
                if len(args) != 2:
                    raise ValueError("Invalid data")
                self.nodes += [Node(*args)]
            elif t == EDGE:
                if len(args) != 3:
                    raise ValueError("Invalid data")
                self.edges += [Edge(*args)]
            elif t == ATTR:
                if len(args) != 2:
                    raise ValueError("Invalid data")
                self.attrs[args[0]] = args[1]
            else:
                raise ValueError("Invalid data")
