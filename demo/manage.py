import click
from flask.cli import FlaskGroup

from demo.app import create_app


def create_demo(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_demo)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user
    """
    from demo.extensions import db
    from demo.models import User

    click.echo("create user")
    user = User(username="admin", email="edwin@wordspeak.org", password="admin", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
