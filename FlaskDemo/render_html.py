from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>"\
           "<p>This is a paragraph</p>"\
           "<img src='https://media.giphy.com/media/4Zo41lhzKt6iZ8xff9/giphy.gif' width=200/>"


@app.route("/bye")
def bye():
    return "Bye"

#Creating ariable paths and conerting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return(f"Hello {name}, you are {number} years old")


if __name__ == "__main__":
    #Running the app in debug mode to auto-reload
    app.run(debug=True)
