import subprocess
from argparse import ArgumentParser
from dotenv import load_dotenv
from api import submit
from get_puzzle import html_to_md


def create_cli(day: int, part1 = None, part2 = None):
    load_dotenv()
    parser = ArgumentParser(description=f"Day {day} solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 " +
                              "(default: part 1 is printed)"))
    parser.add_argument('-p', '--post', action='store_true',
                        help="Post the solution directly to AOC")
                             
    args = parser.parse_args()
    with open(args.path, 'r') as data:
        if args.part2 and part2 is not None:
            r = part2(data)
        elif not args.part2 and part1 is not None:
            r = part1(data)
        else:
            exit(1)
    print(r)

    if args.post:
        resp = submit(day, args.part2, r)
        if resp.status_code != 200:
            print(resp)
            exit(1)
        subprocess.call("echo '" + html_to_md(resp.text).replace("'", "'\\''") +
                        "' | /usr/bin/bat --plain --terminal-width=80",
                        shell=True)
