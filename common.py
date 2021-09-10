#!/usr/bin/env python
"""
A list of favorite songs for karaoke with search
"""
import locale
import logging
import os


os.environ["LOGLEVEL"] = "DEBUG"
logging.basicConfig(level=os.getenv("LOGLEVEL", "WARN"))
LOGGER = logging.getLogger("kfav")


def set_native_locale():
    """
    Sets the locale to native language: Vietnamese
    """
    try:
        LOGGER.debug("Set locale to vi_VN")
        locale.setlocale(locale.LC_COLLATE, "vi_VN")
    except locale.Error as error:
        LOGGER.debug(f"Set locale failed: {error}")

