import data.db_session
import data.jobs
import data.users
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    data.db_session.global_init('db/blogs.db')

    db_sess = data.db_session.create_session()
    users = db_sess.query(data.users.User)
    jobs = db_sess.query(data.jobs.Jobs)

    return render_template('index.html', jobs=jobs, users=users)


if __name__ == '__main__':
    app.run(port=8071, host='127.0.0.1')
