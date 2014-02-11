from flask import Flask, render_template, request
from private import keys
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("views/index.html")

@app.route("/foo")
def foo():
    return "dat foo"

@app.route("/boom")
def boom():
    return "dat boom"

@app.route("/input", methods=['GET', 'POST'])
def input_get():
    data = {}
    f = request.form
    if request.method == 'POST':
        
    return render_template("views/input.html")

@app.route("/callback"):
    

@app.route("/input", methods=['POST'])
def input_get():
    
    return render_template("views/input.html", data)


if __name__ == "__main__":
    app.run(port=8000, debug=True)


# def app(environ, start_response):
#     data = "Hello, World!\n"
#     start_response("200 OK", [
#             ("Content-Type", "text/plain"),
#             ("Content-Length", str(len(data)))
#             ])
#     return iter([data])
