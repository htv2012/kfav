#!/usr/bin/env python
"""
A simple script to add a song to the database
"""
import bisect

import common
import database


def main():
    common.set_native_locale()
    db = database.read()
    title = input("Title: ")
    author = input("Author: ")
    new_row = database.Row(title, author)
    print(new_row)
    bisect.insort(db, new_row)
    database.save(db)


if __name__ == "__main__":
    main()

