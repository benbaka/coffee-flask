from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", my_age=28)

@app.context_processor
def luck_processor():
    from random import randint
    def lucky_number():
        return randint(1, 10)

    return dict(lucky_number=lucky_number)

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, %s!</h1>" % name


if __name__ == "__main__":
    app.run()