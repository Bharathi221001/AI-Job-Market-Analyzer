from flask import Flask, render_template, request, redirect, url_for
import pdfplumber
import joblib
import sqlite3
app = Flask(__name__)

# Load AI Model
model = joblib.load("model/model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")


# ---------------- Home ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- Dashboard ----------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- Upload ----------------

@app.route("/upload")
def upload():
    return render_template("upload.html")


# ---------------- Jobs ----------------

@app.route("/jobs")
def jobs():
    return render_template("jobs.html")


# ---------------- Job Search ----------------

@app.route("/job_search", methods=["GET", "POST"])
def job_search():

    jobs = [
        {"title":"Python Developer","location":"Hyderabad","experience":"Fresher"},
        {"title":"Frontend Developer","location":"Bengaluru","experience":"Fresher"},
        {"title":"Full Stack Developer","location":"Chennai","experience":"Fresher"},
        {"title":"Backend Developer","location":"Pune","experience":"1 Year"}
    ]

    if request.method == "POST":

        keyword = request.form["keyword"].lower()

        jobs = [
            job for job in jobs
            if keyword in job["title"].lower()
        ]

    return render_template("job_search.html", jobs=jobs)

# ---------------- Skill Prediction ----------------

@app.route("/skill_prediction")
def skill_prediction():
    return render_template("skill_prediction.html")

# ---------------- Register ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(fullname,email,username,password) VALUES(?,?,?,?)",
            (fullname, email, username, password)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")

# ---------------- Login ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            return redirect(url_for("home"))
        else:
            return "Invalid Username or Password"

    return render_template("login.html")

# ---------------- Logout ----------------

@app.route("/logout")
def logout():
    return redirect(url_for("login"))

# ---------------- About ----------------

@app.route("/about")
def about():
    return render_template("about.html")


# ---------------- Contact ----------------

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------------- Predict ----------------

@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["resume"]

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    skills = []

    if "python" in text.lower():
        skills.append("Python")

    if "html" in text.lower():
        skills.append("HTML")

    if "css" in text.lower():
        skills.append("CSS")

    if "javascript" in text.lower():
        skills.append("JavaScript")

    if "flask" in text.lower():
        skills.append("Flask")

    if "sql" in text.lower():
        skills.append("SQL")

    features = [[
        1 if "Python" in skills else 0,
        1 if "HTML" in skills else 0,
        1 if "CSS" in skills else 0,
        1 if "JavaScript" in skills else 0,
        1 if "Flask" in skills else 0,
        1 if "SQL" in skills else 0
    ]]

    prediction = model.predict(features)
    predicted_role = label_encoder.inverse_transform(prediction)[0]

    return render_template(
        "result.html",
        resume_text=text,
        skills=skills,
        predicted_role=predicted_role
    )


# ---------------- Run ----------------

if __name__ == "__main__":
    app.run(debug=True)