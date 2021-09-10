#!/usr/bin/env python3
"""
Converts an md file to csv
"""
import collections
import csv
import fileinput
import itertools
import locale
import pathlib


def by_title(record):
    title, author = record
    sort_key = locale.strxfrm(title)
    return sort_key


def main():
    """ Entry """
    try:
        locale.setlocale(locale.LC_COLLATE, 'vi_VN')
    except locale.Error:
        print("WARNING: Failed to set Vietnamese collation")

    data_path = pathlib.Path(__file__).parent / ".." / "favorites.csv"

    group = collections.defaultdict(list)
    with open(data_path, "r") as stream:
        reader = csv.reader(stream)
        for line_number, row in zip(itertools.count(1), reader):
            title = row[0]
            group[title].append((line_number, row))

    for title, tup in group.items():
        if len(tup) < 2:
            continue
        for line_number, row in tup:
            print(f"{line_number:>4}: ", end="")
            print(",".join(row))


if __name__ == '__main__':
    main()

