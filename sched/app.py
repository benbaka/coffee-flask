from flask import Flask, render_template
from flask import request
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

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
    return render_template('user.html',name= name)

@app.route('/index')
def index():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your browser is %s</p>" % user_agent

if __name__ == "__main__":
    app.run()