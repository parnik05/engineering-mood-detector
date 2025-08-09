from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mood data for each semester
moods = {
    "1": {"emoji": "😃", "text": "Excited for the new journey!", "hint": "സ്വാഗതം! Engineering is just fun... for now ", "gif": "/static/gifs/s1.gif"},
    "2": {"emoji": "🙂", "text": "Sleep during class = default mode.", "hint": "Still figuring out where the classes are", "gif": "/static/gifs/s2.gif"},
    "3": {"emoji": "😅", "text": " Labs = Fear!!Viva = Trauma", "hint": "Midway stress kicking in.", "gif": "/static/gifs/s3.gif"},
    "4": {"emoji": "🤯", "text": " Mid BTech crisis!", "hint": "Assignments everywhere!", "gif": "/static/gifs/s4.gif"},
    "5": {"emoji": "😴", "text": "Energy running low.", "hint": "Power naps can save you!", "gif": "/static/gifs/s5.gif"},
    "6": {"emoji": "🥲", "text": "Where is the break button??", "hint": " Syllabus and exams says nope.", "gif": "/static/gifs/s6.gif"},
    "7": {"emoji": "🥴", "text": "💼 Placement season = anxiety season.", "hint": "📈 Stress level = Final year max..", "gif": "/static/gifs/s7.gif"},
    "6": {"emoji": "🥲", "text": "Where is the break button??", "hint": " Syllabus and exams says nope.", "gif": "/static/gifs/s6.gif"},
    "6": {"emoji": "🥲", "text": "Where is the break button??", "hint": " Syllabus and exams says nope.", "gif": "/static/gifs/s6.gif"},
    "6": {"emoji": "🥲", "text": "Where is the break button??", "hint": " Syllabus and exams says nope.", "gif": "/static/gifs/s6.gif"},
    "8": {"emoji": "😐 ", "text": "Last days of college!!", "hint": "Remember when we were excited in s1", "gif": "/static/gifs/s8.gif"},
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_mood", methods=["POST"])
def get_mood():
    data = request.get_json()
    semester = data.get("semester")
    mood = moods.get(semester, {"emoji": "❓", "text": "Unknown", "hint": "No data", "gif": ""})
    return jsonify(mood)

if __name__ == "__main__":
    app.run(debug=True)
