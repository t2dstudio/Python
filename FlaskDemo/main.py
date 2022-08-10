from flask import Flask

app = Flask(__name__)
#......PYTHON DECORATOR
#.....To add functionality to an existing function
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
#...python function can be passed arround as arguements = Frist-Class Objects
#Decoratator function is just a functions that wrdaps up another function so as to add another functionality to that function
if __name__ == "__main__":
    app.run()
