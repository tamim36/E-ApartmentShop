#!/usr/bin/env python
# C:\Users\tamim\PyProjects\E_ApartmentShop\venv\Scripts\activate.bat
# cd PyProjects\E_ApartmentShop\
# 37 start
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eApartmentShop.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
