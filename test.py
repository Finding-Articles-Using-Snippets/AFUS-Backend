from firebase_admin import credentials, firestore, initialize_app
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer 

cred = credentials.Certificate('secret_key.json')
default_app = initialize_app(cred)
db = firestore.client()
user_ref = db.collection('users')
pdfs_ref = db.collection('pdfs')
user_pdf_ref = db.collection('usersPDF')

user = user_pdf_ref.document("e8IMLRvCImOhjM1rNyP0Jb5gcTV2").get()
print(user.to_dict())

def get_results(uid,query):

    vectorizer = pickle.load(open("tfidf1.pkl", 'rb'))
    query_vector = vectorizer.transform([query])
    files = user_pdf_ref.document(uid).get().to_dict()['pid']
    file_vectors = []
    for file in files:
        file_details= pdfs_ref.document(file).get().to_dict()
        file_vec_dict = file_details['vector']
        vec_dim = 10000

        file_vec = [0]*vec_dim
        for k,v in file_vec_dict.items():
            file_vec[k] = v
        file_vectors.append(file_vec)

    results = cosine_similarity(query_vector,file_vectors)[0]

    return sorted(list(zip(files,results)),key = lambda x: x[1],reverse = True)


def store_vector(uid,file):

    vectorizer = pickle.load(open("tfidf1.pkl", 'rb'))
    # Append to user
    file_details = pdfs_ref.document(file).get().to_dict()
    file_vec = vectorizer.transform(file)
    