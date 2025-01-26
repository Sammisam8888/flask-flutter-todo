from database import db
from datetime import datetime


class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)

    description = db.Column(db.String(100))
    is_executed = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    duedate=db.Column(db.DateTime)
    
    class Config():
        from_attribute=True

    def __repr__(self):
        return '<Task %r>' % self.id
        #everytime we create a new task it will print the id

    def __init__(self, name,description, duedate, is_executed):
        self.name = name
        self.is_executed = is_executed
        self.description = description
        self.duedate = duedate


