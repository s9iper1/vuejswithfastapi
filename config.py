import os
import sys
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl

from dotenv import load_dotenv
from os.path import join

BASEDIR = os.getcwd()
LOGDIR = "logs"
LOGFILE = "vuejswithfast"
BIND = "0.0.0.0"

print(os.path.dirname(__file__))
dotenv_path = join(os.path.dirname(__file__), ".env")

load_dotenv(dotenv_path)

PORT = os.environ.get("PORT")
WORKERS = os.environ.get("WORKERS")
RELOAD = os.environ.get("RELOAD")
ORIGINS = os.environ.get("ORIGINS")
NB_ENV = os.environ.get("EN_ENV")

BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

