#!/usr/bin/env bash
python -m venv venv
source venv/bin/activate
pip install -U -r requirements.txt
cd apps/docs
mkdocs serve
