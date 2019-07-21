class Garden(object):
    def __init__(self, diagram, students=None):
        self.students = students
        if students is None:
            self.students = ('Alice Bob Charlie David Eve'
                             'Fred Ginny Harriet Ileana'
                             'Joseph Kincaid Larry').split()
        [row1, row2] = diagram.splitlines()
        self.garden = [row1[i:i+2] + row2[i:i+2]
                       for i in range(0, len(row1), 2)]
        # self.garden = [a + b for a, b in zip(
        #                    *[row[::2] for row in diagram.splitlines()]
        #                )]

g = "VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV"
print(Garden(g).garden)
