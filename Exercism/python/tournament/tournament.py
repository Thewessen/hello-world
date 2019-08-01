class Team(object):
    """Football team"""
    def __init__(self, name: str):
        self.name = name
        self.W = 0
        self.D = 0
        self.L = 0

    @property
    def MP(self) -> int:
        return self.W + self.D + self.L

    @property
    def points(self) -> int:
        return 3 * self.W + self.D


def tally(rows: list) -> list:
    """Tally the results of a small football competition."""
    teams = dict()
    for result in rows:
        name1, name2, res = result.split(';')
        for name in (name1, name2):
            if name not in teams:
                teams[name] = Team(name)
        if res == 'win':
            teams[name1].W += 1
            teams[name2].L += 1
        if res == 'loss':
            teams[name1].L += 1
            teams[name2].W += 1
        if res == 'draw':
            teams[name1].D += 1
            teams[name2].D += 1
    return ([f'{"Team":30} | MP |  W |  D |  L |  P'] +
            [f'{team.name:30} | {team.MP:2d} | {team.W:2d} | '
             f'{team.D:2d} | {team.L:2d} | {team.points:2d}'
            for team in sorted(teams.values(),
                               key=lambda x: (-x.points, x.name))])
