from main import db
db.create_all()

def get_db():
    yield(db)
    return

exit()