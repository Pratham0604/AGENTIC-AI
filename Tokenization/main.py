import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "the name is pratham"

decode = enc.encode(text)

print(decode)

# import tiktoken
# print("tiktoken is installed!")

#import sys
#print(sys.executable)

#  D:/AGENTIC-AI/.venv/Scripts/Activate.ps1  to activate my virtual environment

