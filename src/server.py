from flask import Flask
from handler import main as main_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)

