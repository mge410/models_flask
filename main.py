from data import db_session
from data.jobs import Jobs
from data.users import User
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    db_session.global_init('db/blogs.db')

    db_sess = db_session.create_session()
    users = db_sess.query(User)
    jobs = db_sess.query(Jobs)

    return render_template('index.html', jobs=jobs, users=users)


if __name__ == '__main__':
    app.run(port=8071, host='127.0.0.1')
