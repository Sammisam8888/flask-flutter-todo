from flask_marshmallow import Marshmallow as ma
from main import ma


class TodoSchema(ma.Schema):
    class Meta:
        fields=('id','name','iscompleted')


todo_schema=TodoSchema()
todos_schema=TodoSchema(many=True)

