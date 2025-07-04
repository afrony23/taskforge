from flask import Flask, render_template, request, jsonify
from datetime import datetime
import time

app = Flask(__name__)

tasks = [
    {"id": 1, "name": "Call land agents", "done": False},
    {"id": 2, "name": "Practice Krita", "done": False},
    {"id": 3, "name": "Apply to remote jobs", "done": False}
]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks, current_time=datetime.now().strftime("%H:%M"))

@app.route("/set_reminder", methods=["POST"])
def set_reminder():
    task_id = int(request.form.get("task_id"))
    minutes = int(request.form.get("minutes"))
    time.sleep(minutes * 60)  # Simulate delay
    return jsonify({"message": f"⏰ Time for: {tasks[task_id-1]['name']}!"})

if __name__ == "__main__":
    app.run(debug=True)