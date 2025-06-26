import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Clean text and split into sentences"""
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents if sent.text.strip()]

def clean_text(text):
    """Remove stopwords and punctuation"""
    doc = nlp(text)
    return ' '.join([token.text for token in doc if not token.is_stop and not token.is_punct])