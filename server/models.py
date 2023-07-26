import datetime

from sqlalchemy_serializer import SerializerMixin

from .globals import globals as g


class AIProject(g.db.Model, SerializerMixin):
    __tablename__ = 'aiproject'
    id = g.db.Column(g.db.Integer, primary_key=True)
    name = g.db.Column(g.db.String, nullable=False)
    model_dir = g.db.Column(g.db.String)
    no_of_ainfts = g.db.Column(g.db.Integer)
    status = g.db.Column(g.db.String)
    progress = g.db.Column(g.db.Integer)
    job_id = g.db.Column(g.db.Integer)
    created_date = g.db.Column(g.db.DateTime, default=datetime.datetime.utcnow)


class AINFT(g.db.Model, SerializerMixin):
    __tablename__ = 'ainft'
    id = g.db.Column(g.db.Integer, primary_key=True)
    filename = g.db.Column(g.db.String)
    project_id = g.db.Column(g.db.Integer, g.db.ForeignKey('aiproject.id'),
                             nullable=False)
    job_id = g.db.Column(g.db.Integer)
    created_date = g.db.Column(g.db.DateTime, default=datetime.datetime.utcnow)
