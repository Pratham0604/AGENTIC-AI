from google import genai

client = genai.Client(
    api_key = "your_api_key"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",contents="explain about artificial intelligence"
)

print(response.text)

#  Hello_world\gemini_hello.py    to run the code