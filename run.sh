#!/usr/bin/env bash
python3 -m venv venv
source venv/bin/activate
pip install -U -r requirements.txt
python -m pip install --upgrade pip
python manage.py runserver