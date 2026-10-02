from google import genai
from config import API_KEY, MODEL

if not API_KEY or not MODEL:
    raise SystemExit("Set GEMINI_API_KEY and GEMINI_MODEL in .env")

client = genai.Client(api_key=API_KEY)
response = client.models.generate_content(
    model=MODEL,
    contents="In one sentence, what is an AI agent?",
)
print(response.text)
print("Tokens used:", response.usage_metadata.total_token_count)
