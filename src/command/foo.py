from flask import Blueprint
import click

# 场景command蓝图
cmdbp = Blueprint('foo', __name__)


@cmdbp.cli.command('test')
def test():
    click.echo('foo.test')
