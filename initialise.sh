#! /bin/sh
touch db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py
