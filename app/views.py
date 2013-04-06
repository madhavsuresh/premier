from flask import render_template,redirect
from app import app
from forms import FeedbackForm
from app.database import db_session
from app.models import Feedback

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

def form_to_dict(form):
    ret = {}
    for f in form:
        ret[f.name] = f.data
    return ret

def handle_form_data(arg_d):
    f = Feedback(arg_dict=arg_d)
    db_session.add(f)
    db_session.commit()

        

@app.route('/',methods = ['GET','POST'])
def enter():
#hacky hack
    form = FeedbackForm(csrf_enabled = False)
    if form.validate_on_submit():
        print 'woot!'
        ad = form_to_dict(form)
        handle_form_data(ad)
        return redirect('/')
    return render_template('form.html',form = form)

@app.route('/presenters/<pres>')
def show_stats(pres):
    pres = Feedback.query.filter_by(pres_num=pres).all()
    print pres
    if len(pres) > 0:
        return 'I\'ll get it to you'
    else:
        return 'wat'

@app.route('/viewall')
def viewall():
    pres = Feedback.query.all()
    print pres
    return 'heh'

