from ollama import chat
msg = "Hello! my name is justin what is life if full of care we have no time to stand and stare"
response = chat(
    model='nemotron-3-ultra:cloud',
    messages=[{'role': 'user', 'content': msg}],
)
print(response.message.content)