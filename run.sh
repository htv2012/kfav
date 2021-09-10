#!/usr/bin/env bash
if [[ -z $VIRTUAL_ENV ]]
then
    source ~/.virtualenv/kfav/bin/activate
fi
FLASK_ENV=development python main.py
