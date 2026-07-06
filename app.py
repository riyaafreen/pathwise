from flask import Flask, render_template, request

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        student = {
            "name": request.form["name"],
            "email": request.form["email"],
            "career": request.form["career"]
        }

        students.append(student)

        return f"""
        <h2>Registration Successful!</h2>
        <p>Name: {student['name']}</p>
        <p>Email: {student['email']}</p>
        <p>Career Goal: {student['career']}</p>
        <a href='/'>Back Home</a>
        """

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)