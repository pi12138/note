from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager, Shell
from flask_wtf import FlaskForm
from flask_migrate import Migrate, MigrateCommand
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
manage = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail(app)

app.config['SECRET_KEY'] = 'xxxxx'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return "<User {}>".format(self.username)

class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


"""
@app.route('/', methods=["GET", "POST"])
def index():
    name = None
    form = NameForm()
    
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=name)
"""
"""
@app.route('/', methods=["GET", "POST"])
def index():
    form = NameForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))
"""
"""
@app.route('/', methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())

@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)






migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)
manage.add_command("shell", Shell(make_context=make_shell_context))
manage.run()


if __name__ == "__main__":
    app.run()
