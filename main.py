#!/usr/bin/env python
"""
A list of favorite songs for karaoke with search
"""
import locale
import logging
import os
import pathlib
import re

from flask import Flask, render_template, request

import common
import database
import network


os.environ["LOGLEVEL"] = "DEBUG"
logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))
LOGGER = logging.getLogger("kfav")
STATIC_DIR = pathlib.Path(__file__).parent.resolve() / "static"
PORT = 3000
LAST_MODIFIED = 0
app = Flask(__name__)


def match(search_term, text):
    """
    Matches the search term against the text
    """
    search_term = search_term.lower()
    if set(search_term) & set(".*\\"):
        return re.search(search_term, text)

    return search_term in text


@app.route("/")
def index():
    """
    The web entry point
    """
    global ROWS

    if database.need_reload():
        ROWS = database.read_db()

    title = request.args.get("title", "")
    author = request.args.get("author", "")

    rows = [row for row in ROWS if match(title, row[database.SEARCHABLE_TITLE])]
    rows = [row for row in rows if match(author, row[database.SEARCHABLE_AUTHOR])]

    LOGGER.debug("title=%r, author=%r", title, author)
    result = render_template(
        "index.html",
        header=database.HEADER,
        rows=rows,
    )
    return result


def main():
    """
    The back-end entry point
    """
    global ROWS

    pid_path = pathlib.Path("/tmp/kfav.pid")
    pid_path.write_text(str(os.getpid()))
    LOGGER.debug(f"Process ID: {os.getpid()}")

    public_ip = network.public_ip()
    if public_ip is not None:
        url = f"http://{public_ip}:{PORT}/"
    else:
        url = "Ask Hai for the URL"

    LOGGER.debug(f"Serving on {url}")
    common.set_native_locale()

    ROWS = database.read_db()

    app.run(
        host="0.0.0.0",
        port=PORT,
        debug=True,
    )


if __name__ == "__main__":
    main()
