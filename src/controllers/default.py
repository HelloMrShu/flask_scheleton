from flask import render_template, request


def index():
    return 'default page'


def test():
    name = request.args.get('name', 'bug')
    context = {
        'username': name
    }
    return render_template('test.html', **context)
