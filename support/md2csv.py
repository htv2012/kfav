#!/usr/bin/env python3
"""
Converts an md file to csv
"""
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

    outfilename = pathlib.Path(__file__).parent / ".." / "favorites.csv"

    records = []
    with fileinput.input() as instream:
        for line in instream:
            line = line.strip()
            if line.startswith("-"):
                line = line.replace("- ", "")
                title, _, author = line.partition("(")
                title = title.strip()
                author = author.strip(")")
                records.append((title, author))

    records.sort(key=by_title)

    with open(outfilename, "w") as outstream:
        writer = csv.writer(outstream)
        writer.writerow(["Title", "Author"])
        writer.writerows(records)

if __name__ == '__main__':
    main()

