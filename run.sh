#!/bin/bash

python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 transmission_util/main.py
