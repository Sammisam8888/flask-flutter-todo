from database import get_db

db=get_db()

class TodoItem(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    iscomplete=db.Column(db.Boolean,nullable=False)

    def __init__(self,title,iscomplete):
        self.title=title
        self.iscomplete=iscomplete

