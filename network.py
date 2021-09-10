#!/usr/bin/env python
import urllib.request
import urllib.error


def public_ip():
    try:
        response = urllib.request.urlopen('https://ipinfo.io/ip')
    except urllib.error.HTTPError:
        return None

    bytes_output = response.fp.read()
    ip = bytes_output.decode('utf-8')
    ip = ip.strip()
    return ip
