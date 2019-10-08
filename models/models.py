from sqlalchemy.dialects import postgresql
from initialize import db

class Currency(db.Model):
    __tablename__ = 'currency'
    id = db.Column(db.INT,primary_key=True,autoincrement=True)
    name = db.Column(db.VARCHAR(50), nullable=False)
    code = db.Column(db.VARCHAR(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    status =db.Column(db.VARCHAR(50),nullable=False)
    from_date = db.Column(db.DATE,nullable=False)
    to_date = db.Column(db.DATE,nullable=False)
    changes = db.Column(db.Float,nullable=False)



    def __init__(self,value,code,name,from_date,to_date,changes,status):
        self.name = name
        self.code = code
        self.value = value
        self.from_date = from_date
        self.to_date = to_date
        self.changes = changes
        self.status = status

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def filter(cls,**query):
        return cls.query.filter_by(**query)

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __str__(self):
        return f'{self.code}'