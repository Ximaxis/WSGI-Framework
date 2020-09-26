# WSGI
For start:

gunicorn fwsgi:application

or

uwsgi --http-socket :8000 --file-serve-mode fwsgi.py

