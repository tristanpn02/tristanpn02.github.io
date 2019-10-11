from app import app
from flask import render_template
import os


@app.errorhandler(404)
def page_not_found(e):
    return render_template('essential/404.html'), 404


@app.route('/')
def index():
    project_list = []
    for project in os.listdir('./app/projects'):
        project_list.append(project)
    return render_template('index.html', projects=project_list)


@app.route('/about')
def about():
    return render_template('information/about.html')


@app.route('/todo')
def todo():
    return render_template('information/todo.html')


@app.route('/contact')
def contact():
    return render_template('information/contact.html')

from .projects.kennitala import kennitala
app.register_blueprint(kennitala.bp)

from .projects.store import store
app.register_blueprint(store.bp)

from .projects.news import news
app.register_blueprint(news.bp)