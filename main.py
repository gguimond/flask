#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, make_response, url_for, render_template, flash, request, session, redirect

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "key1717"

@app.context_processor
def title():
    return dict(title="first flask !")

@app.template_filter('myfilter')
def myfilter(dist):
    return "myfilter"

@app.route('/')
def index():
    return "Hello !"

@app.route('/test', methods=['GET'])
@app.route('/test/<int:num>', methods=['GET'])
def test(num=0):
    return "Test : " + str(num)

@app.route('/makeurl', methods=['GET'])
def url():
    return url_for('test', num="12")

@app.route('/setpseudo', methods=['GET'])
def setpseudo():
    session['pseudo'] = 'MJ'
    return redirect(url_for('template', param="toto"))

@app.route('/template/<param>', methods=['GET'])
def template(param):
    flash(u'hello man')
    pseudo = "anonymous"
    if 'pseudo' in session:
        pseudo = session['pseudo']
    if 'msg' in request.args:
        return render_template('main.html', params=[param, request.args['msg']], pseudo=pseudo)
    else:
        return render_template('main.html', params=[param], pseudo=pseudo)

@app.errorhandler(404)
def not_found(error):
    response = make_response("page not found", 404)
    return response


if __name__ == '__main__':
    app.run(debug=True)