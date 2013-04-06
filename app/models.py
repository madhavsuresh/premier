from app.database import Base
from sqlalchemy import Column,Integer,Text,Float


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    pres_num = Column(Integer())
    jud_num = Column(Integer())
    knowl_top = Column(Float())
    meth_cont = Column(Float())
    clarity = Column(Float())
    access = Column(Float())
    research = Column(Float())
    overall = Column(Float())
    comments = Column(Text())

    def __init__(self,pres_num=None,jud_num=None,
                knowl_top=None, meth_cont=None,clarity=None,
                access=None,research=None, overall=None,
                comments=None,arg_dict=None):

        if arg_dict:
            self.pres_num = arg_dict['pres_num']
            self.jud_num = arg_dict['jud_num']
            self.knowl_top = arg_dict['knowl_top']
            self.meth_cont = arg_dict['meth_cont']
            self.clarity = arg_dict['clarity']
            self.access = arg_dict['access']
            self.research = arg_dict['research']
            self.overall = arg_dict['overall']
            self.comments = arg_dict['comments']
        else:
            self.pres_num = pres_num
            self.jud_num = jud_num
            self.knowl_top = knowl_top
            self.meth_cont = meth_cont
            self.clarity = clarity
            self.access = access
            self.research = research
            self.overall = overall
            self.comments = comments


