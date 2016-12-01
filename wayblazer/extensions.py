from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import CsrfProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_restful import Api
from flask_marshmallow import Marshmallow


debug_toolbar = DebugToolbarExtension()
csrf = CsrfProtect()
db = SQLAlchemy()
login_manager = LoginManager()
api = Api()
ma = Marshmallow()
