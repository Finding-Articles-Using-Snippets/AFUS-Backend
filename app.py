# Processes
import spacy
import subprocess

# Server
import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

tags_metadata = [
    {
        "name": "Extraction",
        "description": "Operations with extraction of keywords.",
    },
    {
        "name": "Search",
        "description": "Files Search Engine.",
    },
    {
        "name": "Welcome",
        "description": "Just a welcome here."
    },
]

app = FastAPI(
    title="AFUS API",
    description="AFUS API",
    version="0.0.1",
)

# Services
from test import get_results, store_vector

# getting model
from models.user import User
from models.search import Search

@app.post('/api/files', tags=['Extraction'])
def get_keywords(user: User):
    status = store_vector(user.user_id, user.file_id)
    if status:
        return jsonable_encoder({
            "status": True
            })
    return jsonable_encoder({
        "status": False
        })


@app.post('/api/search', tags=['Search'])
def get_fuzzy_matches(user: Search):
    pdfs = get_results(user.user_id,user.search)
    if pdfs:
        return jsonable_encoder({
            'pdfs' : pdfs,
            'status': True
        })
    return jsonable_encoder({
            'status': False
        })

@app.get("/status", tags = ['Welcome'])
def home():
    return {
        "status": "True",
        "message": "OK!"
        }

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=5002)