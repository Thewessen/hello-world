#!/usr/bin/env python3

import os, subprocess
from bs4 import BeautifulSoup
from markdownify import markdownify
from dotenv import load_dotenv
from argparse import ArgumentParser
from datetime import date
from api import intro, get_input


def create_cli():
    """Make an easy to use cli for fetching adventofcode puzzles"""
    parser = ArgumentParser(description="Fetch puzzle readme and input from adventofcode.com")
    parser.add_argument('day', metavar='D', type=int, nargs='?', help="The day of the puzzle", default=date.today().day)
    parser.add_argument('-f', '--force', action='store_true', help="Force recreation of readme and input files", default=False)
    return parser.parse_args()


def html_to_md(text: str, root = 'article') -> str:
    soup = BeautifulSoup(text, features="html.parser")
    articles = ''.join(str(art) for art in soup.find_all(root))
    md = markdownify(articles)
    return  md.replace('\n\n\n', '\n\n').strip()


def main():
    load_dotenv()
    args = create_cli()

    if args.day < 1:
        print("Only positive intergers are allowed")
        exit(1)

    root = os.environ.get('ROOT', './')
    year = os.environ.get('YEAR', date.today().year)
    path = os.path.join(root, str(year), f'day{args.day:02}')
    if not os.path.isdir(path):
        os.mkdir(path)

    docpath = os.path.join(path, 'README.md')
    if not os.path.isfile(docpath) or args.force:
        print(f'Getting puzzle description for day {args.day}...')
        r = intro(args.day)
        if r.status_code != 200:
            print(r)
            exit(1)
        desc = html_to_md(r.text)
        with open(docpath, 'w') as doc:
            doc.write(desc)
    else:
        print('Puzzle description file already exists')

    inputpath = os.path.join(path, 'input')
    if not os.path.isfile(inputpath) or args.force:
        print(f'Getting puzzle input for day {args.day}...')
        r = get_input(args.day)
        if r.status_code != 200:
            print(r)
            exit(1)
        puzzle = r.text.strip()
        with open(inputpath, 'w') as i:
            i.write(puzzle)
    else:
        print('Puzzle input file already exists')

    subprocess.call('/usr/bin/bat --style=plain,rule --terminal-width=80 '
                    + docpath, shell=True)


if __name__ == '__main__':
    main()
