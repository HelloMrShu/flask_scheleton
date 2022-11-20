from flask import Blueprint
import click


foobp = Blueprint('foo', __name__)


@foobp.cli.command('test')
def test():
    click.echo('foo.test')
