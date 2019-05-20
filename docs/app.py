from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
# Init app
app = Flask(__name__,static_url_path='/static')
# Datenbank konfig
app.config.from_pyfile('config.py')
# Erstellen von db
db = SQLAlchemy(app)
# Marschmallow initieren
ma = Marshmallow(app)
#password encrypction/decryption
bcrypt = Bcrypt(app)

from views import *
if __name__ == "__main__":
    app.run()
