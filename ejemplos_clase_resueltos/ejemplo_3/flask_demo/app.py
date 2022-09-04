from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>¡Hola mundo!</h1>"

if __name__ == "__main__":
    app.run("0.0.0.0", 5030)