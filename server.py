from flask import Flask, render_template, request, flash, redirect, session
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def base():
    
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)