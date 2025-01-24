from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import TodoItem 
from database import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)



@app.route('/', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        task_name = request.form['task']
        task_description = request.form['description']
        task_duedate = request.form['due_date']
        task_is_executed = request.form.get('is_executed') == False
        # Create new task
        new_task = TodoItem(name=task_name, description=task_description,
                            duedate=task_duedate, is_executed=task_is_executed)
        try:
            db.session.add(new_task)
            db.session.commit()

            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks=TodoItem.query.order_by(TodoItem.date_created).all()
        return render_template('index.html',tasks=tasks)

@app.route('/update/<int:id>')
def update(id):
    return "update"

@app.route('/delete/<int:id>')
def delete(id):
    return "delete"




if __name__ == '__main__':
    app.run(debug=True)