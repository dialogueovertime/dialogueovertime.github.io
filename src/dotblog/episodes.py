from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from dotblog.db import get_db

bp = Blueprint('episodes', __name__)

@bp.route("/")
def episodeList():
    return render_template("episodelist.html")

@bp.route("/addepisode", methods=('GET', 'POST'))
def addEpisode():
    if request.method == 'POST':
        # password = request.form['password']
        db = get_db()
        error = None

        for f in request.form:
            if not f:
                error = 'Fill in all fields'
                break

        if error is None:
            try:
                db.execute(
                    "INSERT INTO episodes VALUES (?, ?, ?, ?, ?, ?)",
                    (request.form['episodeNumber'],
                    request.form['title'],
                    request.form['releaseDate'],
                    request.form['runTimeMinutes'],
                    request.form['segment'],
                    request.form['oneLastThing']
                    )
                )
                db.commit()
            except db.IntegrityError:
                error = f"Episode number {request.form['episodeNumber']} is already saved."
            else:
                return redirect(url_for('episodes.episodeList'))

        flash(error)

    return render_template('addepisode.html')
