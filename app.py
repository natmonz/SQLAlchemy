"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_data'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'abcdefgsecretkey'

connect_db(app)

@app.route('/')
def root():
    """Homepage"""
    return redirect('/users')

@app.route('/users')
def users():
    """User Information Page"""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('/users/index.html', users=users)

@app.route('/users/new', methods=['GET'])
def new_user_form():
    """A form where users can create new users"""

    return render_template('/users/new.html')

@app.route('/users/new', methods=['POST'])
def new_users():
    """This will handle form submission when creating a new user"""
    new_user = User (
        first_name = request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None
        )

    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_users(user_id):
    """Shows info of specific user"""
    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_users(user_id):
    """Shows selected user and handles update of specific user"""
    user = User.query.get_or_404(user_id)
    user = request.form['first_name']
    user=request.form['last_name']
    user=request.form['image_url'] 

    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_users(user_id):
    """This handles a submission to delte user info"""
    user = User.query.get_or_404(user_id)
    db.session.add(user)
    db.session.commit()

    return redirect('/users')