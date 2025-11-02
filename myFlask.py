from flask import Flask, render_template, session, request, url_for, redirect
from myGemini import Gemini
import markdown

app = Flask(__name__)
app.secret_key = "Devin_DevCrish"



@app.route('/', methods=['POST', 'GET'])
def chat():
    if "Messages" not in session:
        session["Messages"] = []
    if request.method == 'POST':
        user_input = request.form['user_input']
        session["Messages"].append({"role":"user", "parts":[{"text":user_input}]})
        Bot_response = Gemini(session["Messages"])
        # 🟢 CONVERT MARKDOWN TO HTML HERE 🟢
        Bot_response_html = markdown.markdown(Bot_response)
        session["Messages"].append({"role":"model", "parts":[{"text":Bot_response_html}]})
        print(session["Messages"])
        print("\n")
        return render_template("index.html", messages=session["Messages"])
    return render_template("index.html", messages=session["Messages"]) 

app.run(debug=True)