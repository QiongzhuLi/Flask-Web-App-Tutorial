from flask import Blueprint , render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Note
from . import db
import json



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])   ##It is a decorator, which means whenever you go to this route, the following function will run
@login_required   ## login required, see __init__.py
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')            
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])    ## refers to static/index.js
def delete_note():
    note = json.loads(request.data)   
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})