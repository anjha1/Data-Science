from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def anjha():
    return "<h1>Hello I am anjha</h1>"


@app.route("/user/quary_data")
def user_quary():
    data=request.args.get('q')
    return f"This is input data from url {data}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
