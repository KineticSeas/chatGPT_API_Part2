from fastapi import FastAPI, HTTPException
from chatgpt import MyOpenAI

app = FastAPI()

#  Notes - End of Step 2 (Setup)
#  Created a new class MyOpenAI with a static method called chat


@app.post("/chat/")
async def chat(prompt: str):
    # Configure the OpenAI library with your API key
    # Create a file on your filesystem with the openai key.
    return MyOpenAI.chat(prompt)

@app.post("/clear/")
async def chat():
    return MyOpenAI.clear()
