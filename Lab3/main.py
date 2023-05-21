from model import *

@app.route('/', methods=['GET'])
def hallo():
    return render_template('index.html')

@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html')

@app.route('/teacher', methods=['GET'])
def teacher():
    return render_template('teacher.html', teachers=Teacher.query.all(), tasks=Task.query.all())

@app.route('/teacher')
def task(teacher_id):
    return render_template('teacher.html', tasks=Task.query.all())

@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    name = request.form['name']
    tname = request.form['tname']
    lname = request.form['lname']

    db.session.add(Teacher(name=name, tname=tname, lname=lname))
    db.session.commit()

    return redirect(url_for('teacher'))

@app.route('/add_task', methods=['POST'])
def add_task():
    # teacher = get_teacher(request.form['id_teacher'])
    print(request.form['id_teacher'])
    name = request.form['name']
    description = request.form['description']
    teacher = Teacher.query.get(request.form['id_teacher'])

    db.session.add(Task(name=name, description=description, teacher_id=teacher.id))
    db.session.commit()

    return redirect(url_for('teacher'))

@app.route('/go_teacher', methods=['GET'])
def go_teacher():
    return redirect(url_for('teacher'))

@app.route('/get_teacher', methods=['POST'])
def get_teacher(Teacher):
    select = Teacher
    print(select)
    return select



if __name__ == '__main__':
    app.run(debug=True)

