import os, requests
from urllib.parse import urljoin

def get_url(day: int, ext = '') -> str:
    """The default formatted url for adventofcode. Partially stored in env."""
    url = os.environ.get('BASE_URL')
    year = os.environ.get('YEAR')
    if url is None:
        raise ImportError('No base url in env file')
    if year is None:
        raise ImportError('No YEAR in env file')
    if len(ext) > 0:
        path = os.path.join(year, 'day', str(day), ext.strip('/'))
    else:
        path = os.path.join(year, 'day', str(day))
    return urljoin(url, path)


def get_session():
    """So the servers knows who I am..."""
    s = requests.session()
    s.cookies.set('session', os.environ.get('SESSION'))
    return s


def submit(day: int, part2: bool, result):
    s = get_session()
    data = { "answer": result, "level": int(part2) + 1 }
    url = get_url(day, '/answer')
    return s.post(url, data)


def intro(day: int):
    s = get_session()
    url = get_url(day)
    return s.get(url)


def get_input(day: int):
    s = get_session()
    url = get_url(day, 'input')
    return s.get(url)
