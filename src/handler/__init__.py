from flask import Blueprint

main = Blueprint('main', __name__)

from handler import hello, verify_code, register
