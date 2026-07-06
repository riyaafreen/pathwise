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
@app.route("/skill-gap", methods=["GET", "POST"])
def skill_gap():

    career_skills = {
        "Data Analyst": ["Python", "SQL", "Excel", "Power BI"],
        "AI Engineer": ["Python", "Machine Learning", "TensorFlow"],
        "Digital Marketer": ["SEO", "Content Marketing", "Analytics"]
    }

    if request.method == "POST":

        career = request.form["career"]

        user_skills = [
            skill.strip()
            for skill in request.form["skills"].split(",")
        ]

        required_skills = career_skills[career]

        missing_skills = []

        for skill in required_skills:
            if skill not in user_skills:
                missing_skills.append(skill)

        readiness = round(
            ((len(required_skills) - len(missing_skills))
             / len(required_skills)) * 100,
            2
        )

        return render_template(
            "report.html",
            career=career,
            user_skills=user_skills,
            missing_skills=missing_skills,
            readiness=readiness
        )

    return render_template("skill_gap.html")
if __name__ == "__main__":
    app.run(debug=True)