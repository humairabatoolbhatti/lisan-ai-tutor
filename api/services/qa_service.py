import os
import google.generativeai as genai

def answer_question(question: str) -> str:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    try:
        response = model.generate_content(f"Answer this question precisely and concisely: {question}")
        return response.text.strip()
    except Exception as e:
        print(f"Gemini error: {e}")
        return "Error generating answer."
