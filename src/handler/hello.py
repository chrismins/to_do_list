from . import main


# @app.route("/")
# def hello_world():
#     return "my first application!!!"

@main.route("/hello")
def hello_world():
    return 'Hello, World123'
