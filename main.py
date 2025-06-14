from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Question(BaseModel):
    question: str
    image: Optional[str] = None  # base64 image string

@app.post("/api/")
def answer_question(data: Question):
    # This is where your logic will go later (e.g. searching course + discourse content)
    response = {
        "answer": f"This is a placeholder answer for: '{data.question}'",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/sample-post/12345",
                "text": "Sample relevant post"
            }
        ]
    }
    return response
