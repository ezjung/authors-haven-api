import os
import pathlib
import dotenv

from django.core.wsgi import get_wsgi_application


CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DIR / ".env"

USE_DOTENV = os.environ.get("USE_DOTENV_PKG")

print('USE_DOTENV from wsgi', USE_DOTENV)

if str(USE_DOTENV) == "1":
    # base_path is the same folder where manage.py is
    # base_path = pathlib.Path(__file__).resolve().parent
    # Read the file and add into our environment
    # dotenv.read_dotenv()
    print('POSTGRES_HOST', os.environ.get('POSTGRES_HOST'))

    dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authors_api.settings.local')

application = get_wsgi_application()
