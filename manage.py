#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# import dotenv


def main():

    # USE_DOTENV = os.environ.get("USE_DOTENV_PKG")

    # print('USE_DOTENV from manage.py', USE_DOTENV)

    # if str(USE_DOTENV) == "1":
    #     # base_path is the same folder where manage.py is
    #     # base_path = pathlib.Path(__file__).resolve().parent
    #     # Read the file and add into our environment
    #     dotenv.read_dotenv()
    #     print('POSTGRES_HOST', os.environ.get('POSTGRES_HOST'))

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authors_api.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
