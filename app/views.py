from flask import render_template
from app import app
from forms import FeedbackForm

@app.route('/')
@app.route('/index')
def index():
#hacky hack
    form = FeedbackForm(csrf_enabled = False)
    return render_template('form.html',form = form)
