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
from services.extract_keywords import extract_keywords
from services.fuzzy import get_fuzzy_similarity
from services.files import getPdf, getDictionary

# downloading the large model 
#subprocess.call("python -m spacy download en_core_web_lg",shell=True)
nlp = spacy.load("en_core_web_lg")
print("Loaded language model")

# getting model
from models.user import User


# Initialize Firestore DB
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate('secret_key.json')
default_app = initialize_app(cred)
db = firestore.client()
user_ref = db.collection('users')
pdfs_ref = db.collection('pdfs')

@app.post('/api/keywords', tags=['Extraction'])
def get_keywords(user: User):
    query_string = getPdf(user.user_id, user.file_id)
    keywords = extract_keywords(nlp,query_string)
    return jsonable_encoder({
        "keywords" : keywords,
        "status": True
        })

@app.post('/api/search', tags=['Extraction'])
def get_fuzzy_matches(user: User):
    search = user.search
    dictionary = getDictionary(user.user_id)
    similar_words = get_fuzzy_similarity(search,dictionary)
    return jsonable_encoder(similar_words = similar_words)

@app.get("/status", tags = ['Welcome'])
def home():
    return {
        "status": "True",
        "message": "OK!"
        }

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=5002)