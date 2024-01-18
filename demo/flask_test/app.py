from flask import Flask, request, session, flash,render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mdeditor import MDEditor, MDEditorField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import mistune
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_pyfile('setting.py')
app.config['MDEDITOR_FILE_UPLOADER'] = os.path.join(basedir, 'uploads') # save your uploaded img
db = SQLAlchemy(app)
mdeditor = MDEditor(app)
from models import Article


class PostForm(FlaskForm):
    content = MDEditorField('Body', validators=[DataRequired()])
    submit = SubmitField()


@app.route('/')
def hello():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        body = form.content.data
        new_article = Article(content=body)
        db.session.add(new_article)
        db.session.commit()
        flash('add-success')
        return redirect(url_for('hello'))


    return render_template('post_form.html', form=form)


@app.route('/save', methods=['GET', 'POST'])
def save():
    if request.method == 'GET':
        return render_template('post.html')
    else:
        values = request.form
        # print(values)
        content = values.get('mdeditor')
        new_article = Article()
        new_article.content = content
        db.session.add(new_article)
        db.session.commit()
        flash('add-success')
        return redirect(url_for('hello'))


@app.route('/get/<int:aritlce_id>')
def get_article(aritlce_id):
    article = Article.query.get_or_404(aritlce_id)
    output = mistune.html(article.content)
    return render_template('detail.html', article=article, content=output)


@app.cli.command()
def initdb():
    """init testdb"""
    import models
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)