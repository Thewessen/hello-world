#!/usr/bin/env python3.9

import os, subprocess, requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from dotenv import load_dotenv
from argparse import ArgumentParser
from datetime import date


def create_cli():
    """Make an easy to use cli for fetching adventofcode puzzles"""
    parser = ArgumentParser(description="Fetch puzzle readme and input from adventofcode.com")
    parser.add_argument('day', metavar='D', type=int, nargs='?', help="The day of the puzzle", default=date.today().day)
    parser.add_argument('-f', '--force', action='store_true', help="Force recreation of readme and input files", default=False)
    return parser.parse_args()


def get_base_url(day: int) -> str:
    """The default formatted url for adventofcode. Partially stored in env."""
    url = os.environ.get('BASE_URL')
    return f'{url}/day/{day}'


def get_session():
    """So the servers knows who I am..."""
    s = requests.session()
    s.cookies.set('session', os.environ.get('SESSION'))
    return s


def get_puzzle_description(day: int) -> str:
    """Get the description for todays puzzle"""
    s = get_session()
    url = get_base_url(day)
    print(f'Getting puzzle description for day {day} from {url}...')
    r = s.get(url)
    if r.status_code != 200:
        print(r)
        exit(1)
    soup = BeautifulSoup(r.text, features="html.parser")
    articles = ''.join(str(art) for art in soup.find_all('article'))
    md = markdownify(articles)
    return md.replace('\n\n\n', '\n\n').strip()


def get_puzzle_input(day: int) -> str:
    """Get the user input for todays puzzle"""
    s = get_session()
    url = f'{get_base_url(day)}/input'
    print(f'Getting puzzle input for day {day} from {url}...')
    r = s.get(url)
    if r.status_code != 200:
        print(r)
        exit(1)

    return r.text.strip()


def main():
    load_dotenv()
    args = create_cli()

    if args.day < 1:
        print("Only positive intergers are allowed")
        exit(1)

    path = os.path.join(os.environ.get('ROOT', './'), f'day{args.day}')
    if not os.path.isdir(path):
        os.mkdir(path)

    docpath = os.path.join(path, 'README.md')
    if not os.path.isfile(docpath) or args.force:
        desc = get_puzzle_description(args.day)
        with open(docpath, 'w') as doc:
            doc.write(desc)
    else:
        print('Puzzle description file already exists')

    inputpath = os.path.join(path, 'input')
    if not os.path.isfile(inputpath) or args.force:
        puzzle = get_puzzle_input(args.day)
        with open(inputpath, 'w') as i:
            i.write(puzzle)
    else:
        print('Puzzle input file already exists')

    subprocess.call('/usr/bin/bat --style=plain,rule --terminal-width=80 '
                    + docpath, shell=True)

if __name__ == '__main__':
    main()
