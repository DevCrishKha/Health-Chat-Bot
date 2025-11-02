from flask import Flask, render_template, session, request, url_for, redirect
from myGemini import Gemini

app = Flask(__name__)
app.secret_key = "Devin_DevCrish"

Messages = list({"role":"user", "parts":[{"text":"Hey Gemini, can you help my friend with something"}]})

@app.route('/', methods=['POST', 'GET'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        Messages.append({"role":"user", "parts":[{"text":user_input}]})
        Bot_response = Gemini(Messages)
        Messages.append({"role":"model", "parts":[{"text":Bot_response}]})
        print(Messages)
        print("\n")
        return render_template("index.html", messages=Messages)
    return render_template("index.html", messages=Messages) 

app.run(debug=True)