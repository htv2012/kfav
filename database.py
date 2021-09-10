#!/usr/bin/env python
"""
database-related functions
"""
import csv
import collections
import logging
import pathlib
import unicodedata


AUTHOR = "Author"
TITLE = "Title"
HEADER=[]
SEARCHABLE_AUTHOR = "searchableAuthor"
SEARCHABLE_TITLE = "searchableTitle"
LAST_MODIFIED = 0
LOGGER = logging.getLogger("kfav")

DATA_PATH = pathlib.Path(__file__).with_name("favorites.csv")


Row = collections.namedtuple("Row", [TITLE, AUTHOR])


def strip_accents(text):
    """
    Strips the accents, replace the dd, and lower case
    """
    text = text.replace("đ", "d").replace("Đ", "d")
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore")
    text = text.decode("utf-8")
    text = text.lower()
    return text


def need_reload():
    """
    Returns True if data need reloading
    """
    global LAST_MODIFIED

    path = pathlib.Path(DATA_PATH)
    modified_time = path.stat().st_mtime
    if modified_time != LAST_MODIFIED:
        LOGGER.info("Database modified, reload")
        LAST_MODIFIED = modified_time
        return True
    return False


def read_db():
    """
    Read the database, returns a list of rows
    """
    global HEADER
    with open(DATA_PATH) as stream:
        reader = csv.DictReader(stream)
        HEADER = reader.fieldnames
        rows = list(reader)
        for row in rows:
            row[SEARCHABLE_TITLE] = strip_accents(row[TITLE])
            row[SEARCHABLE_AUTHOR] = strip_accents(row[AUTHOR])
        return rows


def read():
    rows = [Row(row[TITLE], row[AUTHOR]) for row in read_db()]
    return rows


def save(rows):
    with open(DATA_PATH, "w") as stream:
        writer = csv.writer(stream)
        writer.writerow([TITLE, AUTHOR])
        writer.writerows(rows)

