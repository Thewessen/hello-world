class Garden(object):
    """Determines which plants each child in the kindergarten class is
    responsible for."""

    def __init__(self, diagram: str, students: list = None):
        children = ['Alice', 'Bob', 'Charlie', 'David', 'Eve',
                    'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph',
                    'Kincaid', 'Larry']
        seeds = {
            'C': 'Clover',
            'G': 'Grass',
            'R': 'Radishes',
            'V': 'Violets'
        }
        [row1, row2] = diagram.splitlines()
        self.garden = {
            child: [seeds[p] for p in plants]
            for child, plants in zip(
                sorted(students or children),
                zip(*[iter(row1)]*2 + [iter(row2)]*2)
            )
        }

    def plants(self, name: str) -> list:
        """Lists all plants for a specific child."""
        return self.garden[name]
