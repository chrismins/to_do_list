from . import main
from flask import request


@main.route("/register", methods=["POST"])
def register():
    user_name = request.args.get("user_name")
    password = request.args.get("password")
