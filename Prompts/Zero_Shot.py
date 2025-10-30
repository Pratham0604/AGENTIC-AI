# zero shot prompting means giving direct instructions to model

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()   # reads the env file and load it to the environment

client = OpenAI(
    api_key = "your_api_key",
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = "you are physics expert and can only answer questions related to physics"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[                # system prompt
        {"role":"system","content": SYSTEM_PROMPT},
        {"role":"user","content" : "tell me about chemistry"}
    ]
)

print(response.choices[0].message.content)