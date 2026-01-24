from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    with open("messages.txt", "a") as file:
        file.write(f"{name} | {email} | {message}\n")

    return redirect("/")

@app.route("/api/skills")
def api_skills():
    return {
        "languages": ["C++", "Python", "JavaScript"],
        "frameworks": ["Flask"],
        "tools": ["Git", "GitHub", "VS Code"]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

