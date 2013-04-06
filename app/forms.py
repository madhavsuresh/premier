from flask.ext.wtf import Form,DecimalField,validators

class FeedbackForm(Form):
    knowl_top = DecimalField(u'Knowledge of Topic (20%)',[validators.required()])
    meth_cont = DecimalField(u'Methods and content (20%)',[validators.required()])
    clarity = DecimalField(u'Clarity of Presentation (20%)',[validators.required()])
    access = DecimalField(u'Accessibility (20%)',[validators.required()])
    research = DecimalField(u'Research Contributions (10%)',[validators.required()])
    overall = DecimalField(u'Overall Presentation (20%)',[validators.required()])
