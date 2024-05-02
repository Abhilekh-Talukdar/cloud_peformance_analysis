import os

command = "/home/g143myspecialone/.local/lib/python3.10/site-packages/gunicorn"
pythonpath = "/home/g143myspecialone/api/"

# Django project settings
wsgi_app = "api.wsgi:application"

# Unix socket path for Unix socket communication
bind = "0.0.0.0:8000"

# Worker configuration
workers = os.cpu_count() * 2 + 1
