# -*- encoding: utf-8 -*-

from flask import render_template, request

from .application import app


@app.route('/')
def index():
    return render_template(
        "pages/index.html",
        key='value1&'
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template(
            "pages/login.html",
            login=request.form.get('login'),
            password=request.form.get('password'),
        )

    return render_template(
        "pages/login.html",
    )

