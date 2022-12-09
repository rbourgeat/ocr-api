# api dependencies
from fastapi import FastAPI
import uvicorn
# ocr dependencies
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'image.jpeg'

app = FastAPI()
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH)
result

@app.get("/")
async def hello_world():
    return {"api": "work !"}

@app.get("/get/{id}")
async def get_id(id: int):
    return {"id": id}

@app.get("/get/")
async def get_multiple_param(id: int, text: str):
    return {"id": id, "text": text}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)

# or command: uvicorn app:app --reload
