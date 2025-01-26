from flask import Flask, render_template, request, redirect
from models import TodoItem 
from database import db
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)


@app.route('/', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        task_name = request.form['task']
        task_description = request.form['description']
        task_duedate = datetime.strptime(request.form['due_date'], '%Y-%m-%dT%H:%M') if request.form['due_date'] else None
        task_is_executed = request.form.get('is_executed') is not None
        # Create new task
        new_task = TodoItem(name=task_name, description=task_description,
                            duedate=task_duedate, is_executed=task_is_executed)
        try:
            db.session.add(new_task)
            db.session.commit()

            return redirect('/')
        except Exception as e:
            db.session.rollback()  
            return f"There was an issue updating the task: {str(e)}"

        
    else:
        tasks=TodoItem.query.order_by(TodoItem.date_created).all()
        return render_template('index.html',tasks=tasks)



@app.route('/update/<int:id>')
def update(id):
    return "update"

@app.route('/delete/<int:id>')
def delete(id):
    return "delete"

@app.route('/toggle_execution/<int:id>', methods=['POST'])
def toggle_execution(id):
    task = TodoItem.query.get_or_404(id)
    task.is_executed = not task.is_executed
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they do not exist
    app.run(debug=True)