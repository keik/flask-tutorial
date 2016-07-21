import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

DATABASE = '.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    def connect_db():
        return sqlite3.connect(app.config['DATABASE'])

    @app.before_request
    def before_request():
        g.db = connect_db()

    @app.after_request
    def after_request(response):
        g.db.close()
        return response

    @app.route('/')
    def show_entries():
        return render_template('show_entries.html')

    return app

if __name__ == '__main__':
    create_app().run()
