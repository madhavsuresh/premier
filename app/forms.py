from flask.ext.wtf import Form,DecimalField,TextAreaField,IntegerField,validators

comment_string = '''1)Knowledge of topic:
2)Methods and Content:
3)Clarity of Presentation:
4)Accessibility:
5)Research Contributions:
6)Overall Presentation:
'''

class FeedbackForm(Form):
    pres_num = IntegerField(u'Presenter Number',[validators.required(),validators.NumberRange(min=0,max=300)])
    jud_num = IntegerField(u'Judge Number',[validators.required(),validators.NumberRange(min=0,max=300)])
    knowl_top = DecimalField(u'Knowledge of Topic (20%)',[validators.required(),validators.NumberRange(min=1,max=7)])
    meth_cont = DecimalField(u'Methods and content (20%)',[validators.required(),validators.NumberRange(min=1,max=7)])
    clarity = DecimalField(u'Clarity of Presentation (20%)',[validators.required(),validators.NumberRange(min=1,max=7)])
    access = DecimalField(u'Accessibility (20%)',[validators.required(),validators.NumberRange(min=1,max=7)])
    research = DecimalField(u'Research Contributions (10%)',[validators.required(),validators.NumberRange(min=1,max=7)])
    overall = DecimalField(u'Overall Presentation (20%)',[validators.required(),validators.NumberRange(min=1,max=7)])
    comments = TextAreaField(u'Comments',default=comment_string)
