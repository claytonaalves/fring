import os
import sys

sys.path.append(os.path.dirname(__file__))

from config import ApiConfig
from api.app import create_app

application = create_app(ApiConfig)

