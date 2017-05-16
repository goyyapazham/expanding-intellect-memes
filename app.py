from flask import Flask, render_template, url_for, request, redirect, session
import json
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.rebug = True
    app.run()
