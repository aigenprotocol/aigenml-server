import datetime

from sqlalchemy_serializer import SerializerMixin

from .globals import globals as g


class AIProject(g.db.Model, SerializerMixin):
    __tablename__ = 'ai_project'
    id = g.db.Column(g.db.Integer, primary_key=True)
    name = g.db.Column(g.db.String, nullable=False)
    model_dir = g.db.Column(g.db.String)
    no_of_ainfts = g.db.Column(g.db.Integer)
    status = g.db.Column(g.db.String)
    progress = g.db.Column(g.db.Integer)
    job_id = g.db.Column(g.db.Integer)
    created_date = g.db.Column(g.db.DateTime, default=datetime.datetime.utcnow)
