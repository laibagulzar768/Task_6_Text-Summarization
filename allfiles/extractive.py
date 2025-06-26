from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import numpy as np
from preprocess import preprocess_text
import spacy
nlp = spacy.load("en_core_web_sm")  # Should not raise an error
print("SpaCy output:", [sent.text for sent in nlp("Test sentence.").sents])



def extractive_summary(text, num_sentences=3):
    """Improved extractive summarization with proper sentence splitting"""
    try:
        # Process text with SpaCy to get sentences
        doc = nlp(text)
        sentences = [sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 10]
        
        if len(sentences) <= num_sentences or len(sentences) == 0:
            return " ".join(sentences)
        
        # Preprocess each sentence (optional)
        preprocessed_sentences = [
            ' '.join([token.text for token in nlp(sent) if not token.is_stop and not token.is_punct])
            for sent in sentences
        ]
        
        # TF-IDF Vectorization
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf = vectorizer.fit_transform(preprocessed_sentences)
        
        # K-Means Clustering
        kmeans = KMeans(n_clusters=num_sentences, random_state=42)
        kmeans.fit(tfidf)
        
        # Get closest sentences to cluster centers
        avg = np.array([tfidf[kmeans.labels_ == i].mean(axis=0) for i in range(num_sentences)])
        closest, _ = pairwise_distances_argmin_min(avg, tfidf)
        
        # Return original sentences (not preprocessed ones)
        return ' '.join([sentences[i] for i in sorted(closest)])
        
    except Exception as e:
        st.error(f"Extractive summarization failed: {str(e)}")
        return text[:500]  # Fallback