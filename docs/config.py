
Debug = True
IMAGE_UPLOADS = "static/assets/images"
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])
SECRET_KEY = 'e3992c6689e61d9943cc55a9fbf2c0fc'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI =  'sqlite:///db.sqlite'
# SQLALCHEMY_DATABASE_URI =  'sqlite:///:memory:'
