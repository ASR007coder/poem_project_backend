import os
import google.generativeai as genai
from dotenv import load_dotenv

def get_poem_from_gemini(name: str, topic: str) -> str:
    """Talks to the Gemini API."""
    try:
        load_dotenv()
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        
        model = genai.GenerativeModel('gemini-2.0-flash')
        prompt = f"Create a short 4-line poem about {topic} for a user named {name}."
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return "An error occurred while writing your poem."