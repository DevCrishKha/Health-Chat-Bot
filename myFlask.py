from flask import Flask, render_template, session, request, url_for, redirect
from myGemini import Gemini
import markdown

app = Flask(__name__)
app.secret_key = "Devin_DevCrish"



@app.route('/', methods=['POST', 'GET'])
def chat():
    if "Messages" not in session:
        # Define the system instruction to set the bot's fixed role
        system_instruction = (
            "You are a friendly, non-medical, and helpful health assistant. "
            "Your sole purpose is to provide general, educational health information and lifestyle tips. "
            "You **must** start every response, regardless of the user's input, by reminding the user that you are not a doctor "
            "and that they should consult a professional for medical advice. "
            "Do not engage in conversations outside of health, wellness, or general information."
        )

        session["Messages"] = [
            # The system instruction is the first message (hidden from user)
            {"role": "user", "parts": [{"text": system_instruction}]},
            
            # The model's first visible message
            {"role": "model", "parts": [{"text": "Hi there! I'm ready to help you with general health and wellness information. What's on your mind today?"}]}
        ]
        
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