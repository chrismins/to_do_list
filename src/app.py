from server import app
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello_world():
#     return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)