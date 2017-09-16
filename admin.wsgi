import os
import sys

sys.path.append(os.path.dirname(__file__))

from config import AdminConfig
from admin.app import create_app

application = create_app(AdminConfig)

