from flask import Flask, render_template, request, jsonify, redirect, url_for
from analyze import analyze

students =[{"id": 1, "name": "Pidor Pidorovich", "country": "Russia", "skills": ["coding", "communication"]},
           {"id": 2, "name": "Kotak Kotackovich", "country": "Kazakhstan", "skills": ["tomatoes", "cheese"]}]
app = Flask(__name__)

@app.route('/api/v1.0/students', methods=['GET', 'POST'])
def get_students():
    if request.method == 'GET':
        return jsonify(students)
    elif request.method == 'POST':
        data = request.get_json()
        new_id = students[-1]["id"] + 1
        new_student = {"id": new_id, "name": data["name"], "country": data["country"], "skills": data["skills"]}
        students.append(new_student)
        return jsonify(new_student), 201    
@app.route('/students')
def students_template():
    return render_template('students.html', students=students)

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        skills = request.form['skills']
        skills = [skill.strip() for skill in skills.split(",")]
        new_id = students[-1]["id"] + 1
        new_student = {"id": new_id, "name": name, "country": country, "skills": skills}
        students.append(new_student)
        return redirect(url_for('students_template'))
    return render_template('join.html')

        
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        content = request.form['content']
        result = analyze(content)
        return render_template('result.html', result=result)
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)