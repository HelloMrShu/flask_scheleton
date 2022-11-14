from flask import render_template, request
from src import myApp


def index():
    myApp.logger.info("default index action")
    return 'default page'


def test():
    name = request.args.get('name', 'bug')
    context = {
        'username': name
    }
    return render_template('test.html', **context)
