# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request,redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="studentdb"
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        name = request.form['name']
        age = request.form['age']
        course = request.form['course']

        query = "INSERT INTO students(name, age, course) VALUES(%s, %s, %s)"

        values = (name, age, course)

        cursor.execute(query, values)

        db.commit()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    return render_template('index.html',students=students)
####DELETE STUDENT RECORDS
@app.route('/delete/<int:id>')
def delete_student(id):

    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (id,))

    db.commit()

    return redirect('/')

#UPDATE
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):

    if request.method == 'POST':

        name = request.form['name']
        age = request.form['age']
        course = request.form['course']

        query = "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"

        values = (name, age, course, id)

        cursor.execute(query, values)

        db.commit()

        return redirect('/')

    query = "SELECT * FROM students WHERE id=%s"

    cursor.execute(query, (id,))

    student = cursor.fetchone()

    return render_template('update.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)

