from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash

from dotblog.db import get_db

bp = Blueprint('episodes', __name__)

@bp.route("/")
def episodeList():
    db = get_db()
    episodes = db.execute(
        """select e.*, group_concat(h.firstname) as hosts from episodes e 
            join episodehosts eh on e.episodenumber = eh.episode
            join hosts h on eh.host = h.hostid
            group by e.episodenumber;"""
    ).fetchall()

    return render_template("episodelist.html", episodes=episodes)

@bp.route("/addepisode", methods=('GET', 'POST'))
def addEpisode():
    if request.method == 'POST':
        db = get_db()
        error = None

        passwordStored = db.execute(
            'SELECT * FROM passwords'
        ).fetchone()
        
        if not check_password_hash(passwordStored['passwordHash'], request.form['password']):
            error = 'Incorrect password.'

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
                for h in [1,2,3]:
                    db.execute(
                        "INSERT INTO episodehosts VALUES (?, ?, ?)",
                        (request.form['episodeNumber'],
                        h,
                        0)
                    )
                    db.commit()
                db.commit()
            except db.IntegrityError:
                error = f"Episode number {request.form['episodeNumber']} is already saved."
            else:
                return redirect(url_for('episodes.episodeList'))

        flash(error)

    return render_template('addepisode.html')
