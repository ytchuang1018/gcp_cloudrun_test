from flask import Flask,make_response, send_from_directory
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return "Hello"

@app.route('/user', methods=["GET"])
def user():
    response = make_response(send_from_directory(os.path.dirname(__file__), 'test.json', as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format('user.json')
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))