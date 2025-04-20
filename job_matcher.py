from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_texts, job_description):
    texts = resume_texts + [job_description]
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(texts)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    return similarity_scores.flatten()
