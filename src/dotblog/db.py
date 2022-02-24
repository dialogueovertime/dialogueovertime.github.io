import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def savePassword(password):
    db = get_db()

    db.execute(
        "INSERT INTO passwords VALUES (?)",
        (generate_password_hash(password),),
    )
    db.commit()

def seedDB():
    db = get_db()

    with current_app.open_resource('seed.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
@click.password_option()
def init_db_command(password):
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
    savePassword(password)
    click.echo('Password saved.')
    seedDB()
    click.echo('Database Seeded.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)