from handler import main
from flask import request
from models import User
from db import main_db_engine


@main.route("/register", methods=["POST"])
def serve_register():
    args = request
    user_name = request.values.get("user_name")
    if user_name:
        rest = "args has been send"
    else:
        rest = "nothing was send"
    # password = request.args.get("password")
    # results = main_db_engine.session.query(User).filter_by(User.user_name == user_name).all()
    return rest
