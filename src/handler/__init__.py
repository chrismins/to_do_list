from flask import Blueprint

main = Blueprint('main', __name__)

from handler import login, hello, verify_code, register
