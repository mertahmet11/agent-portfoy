from google import genai
from config import API_KEY

if not API_KEY:
    raise SystemExit("GEMINI_API_KEY is missing. Check your .env file.")

client = genai.Client(api_key=API_KEY)
for m in client.models.list():
    actions = getattr(m, "supported_actions", None) or []
    if not actions or "generateContent" in actions:
        print(m.name)
