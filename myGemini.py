import google.generativeai as genai

def Gemini(prompt):
    genai.configure()
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text

print(Gemini("Hi Gemini"))