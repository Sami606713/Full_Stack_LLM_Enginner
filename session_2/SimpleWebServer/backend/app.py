from fastapi import FastAPI,UploadFile, File
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware
import requests

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_text_from_audio(audio_data):
    try:
        API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
        headers = {"Authorization": "Bearer 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"}

        response = requests.post(API_URL, headers=headers, data=audio_data)
        return response.json()['text']
    except Exception as e:
        return str(e)

# make the route

@app.get("/")
def home():
    return {"Text": "Welcome to speech to text service"}

@app.post("/upload/" )
async def response(file: UploadFile = File(...)):

    audio_data = BytesIO(await file.read())

    audio_text = get_text_from_audio(audio_data=audio_data)
    return {"Text": audio_text}
    # return {"Text": "Success"}