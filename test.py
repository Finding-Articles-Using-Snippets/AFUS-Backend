from firebase_admin import credentials, firestore, initialize_app
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer 
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

cred = credentials.Certificate('secret_key.json')
default_app = initialize_app(cred)
db = firestore.client()
user_ref = db.collection('users')
pdfs_ref = db.collection('pdfs')
user_pdf_ref = db.collection('usersPDF')


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

    user_pdf_ref.update({u'pid': firestore.ArrayUnion([file])})

    file_details = pdfs_ref.document(file).get().to_dict()
    url = file_details['pdfUrl']
    urllib.request.urlretrieve(url, "download.pdf")
    infile = open('download.pdf', 'rb')

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    for page in PDFPage.get_pages(infile):
        interpreter.process_page(page)
    converter.close()
    text = output.getvalue()
    output.close

    
    file_vec = vectorizer.transform([text])
    file_vec_dic = dict(file_vec.todok().items())
    file_vec_dic = {k[1],v for k,v in file_vec_dic}
    
    pdfs_ref.update({u'vector': file_vec_dic})

    return True