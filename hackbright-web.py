from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def go_to_form():
    return """<!doctype html>
        <html>
            <head>
                <title>Home</title>
            </head>
            <body>
                <h1>Home Page</h1>

                <p><a href="/student_form">Go to student form</a></p>
            </body>
        </html>"""


@app.route("/student", methods=["POST"])
def get_student():
    """Show information about a student."""

    github = request.form.get('github','jhacks')
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

if __name__ == "__main__":
    app.run(debug=True)