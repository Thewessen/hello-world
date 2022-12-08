#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Optional, Union
from dataclasses import dataclass, field
from itertools import dropwhile
import re


@dataclass
class Directory:
    name: str
    parent: Optional['Directory']
    children: list[Union['Directory', 'File']] = field(default_factory=list)

    def __repr__(self):
        return f"dir {self.name}"

    @property
    def size(self):
        return sum(child.size for child in self.children)

    def set_children(self, lines: Iterator[str]):
        for line in lines:
            if line.startswith('dir'):
                name = line.strip().replace('dir ', '')
                self.children.append(Directory(name=name, parent=self))
            elif re.match(r"^\d+ ", line):
                size, name = line.strip().split(' ')
                self.children.append(File(name=name, size=int(size), parent=self))
            else:
                raise ValueError(f"Unknown child found: {line}")


@dataclass
class File:
    name: str
    size: int
    parent: Directory

    def __repr__(self):
        return f"{self.size} {self.name}"


def parse_input(data: Iterator[str]) -> Directory:
    """Return the directory structure found in puzzle input"""
    cd = re.compile(r"^\$ cd")
    ls = re.compile(r"^\$ ls")
    parent = None
    for line in data:
        if cd.match(line):
            name = line.strip().replace('$ cd ', '')
            if parent is not None and any(child.name == name
                                          for child in parent.children):
                parent = next(child for child in parent.children
                                    if child.name == name) 
            elif name == '..':
                parent = parent.parent
            else:
                parent = Directory(name=name, parent=parent)
            continue
        elif line.startswith('dir'):
            name = line.strip().replace('dir ', '')
            parent.children.append(Directory(name=name, parent=parent))
            continue
        elif re.match(r"^\d+ ", line):
            size, name = line.strip().split(' ')
            parent.children.append(File(name=name, size=int(size), parent=parent))
        elif ls.match(line):
            continue

    while parent.parent is not None:
        # return the root dir
        parent = parent.parent

    return parent


def dir_sizes(directory: Directory) -> Iterator[int]:
    """Iterates through all directories, returning their size"""
    yield directory.size
    for child in directory.children:
        if isinstance(child, Directory):
            yield from dir_sizes(child)


def sum_dir_sizes_lt(data: Iterator[str]) -> int:
    """Sum all directories with a size less than 100_000 (part 1)"""
    directory = parse_input(data)
    return sum(s for s in dir_sizes(directory) if s < 1e5)


def smallest_deleted_dir(data: Iterator[str]) -> int:
    """Find the smallest dir which can be deleted to free up enough disk space (part 2)"""
    directory = parse_input(data)
    used = directory.size
    free = 7e7 - used
    needed = 3e7 - free
    valid_sizes = dropwhile(lambda s: s < needed,
                            sorted(dir_sizes(directory)))
    return next(valid_sizes)


def tree(directory: Directory, level = 0): 
    """Print a nice tree like output (debugging)"""
    print(level * '   ' + repr(directory))
    for file in directory.children:
        if isinstance(file, Directory): 
            tree(file, level + 1)
        elif isinstance(file, File):
            print((level + 1) * '   ' + repr(file))
        else:
            raise ValueError(f"file not recognized: {file}")


if __name__ == '__main__':
    create_cli(7, part1=sum_dir_sizes_lt, part2=smallest_deleted_dir)
