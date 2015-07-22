from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def go_to_form():

    projects = hackbright.get_all_project()
    students = hackbright.get_all_students()
    return render_template('index.html')


@app.route("/student_info")
def get_student():
    """Show information about a student."""

    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template('student_info.html',
                            first=first,
                            last=last,
                            github=github)
    return html


@app.route("/student_form")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html") 

@app.route("/add_student")
def student_add():
    """Add a student."""
    return render_template("student_add.html")

# adding new route
@app.route("/new_student", methods=["POST"])
def show_new_student():
    """Add a student."""
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')
    hackbright.make_new_student(first_name, last_name, github)


    html = render_template('new_student.html',
                            first=first_name,
                            last=last_name,
                            github=github)
    return html  

   

if __name__ == "__main__":
    app.run(debug=True)