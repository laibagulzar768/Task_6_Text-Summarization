from transformers import pipeline
from config import ABSTRACTIVE_MODEL

# Initialize only once to save memory
_summarizer = None

def get_summarizer():
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline("summarization", model=ABSTRACTIVE_MODEL)
    return _summarizer


def abstractive_summary(text, max_length=None, min_length=30):
    if max_length is None:
        # Auto-adjust based on input length
        max_length = min(150, len(text.split()) // 2)
    try:
        # Calculate input token count (approximate)
        input_length = len(text.split())
        
        # Adjust lengths dynamically if input is too short
        if input_length < min_length:
            return text  # Return original if too short to summarize
            
        if input_length < max_length:
            # Reduce max_length proportionally for short inputs
            adjusted_max = max(min_length, int(input_length * 0.7))
        else:
            adjusted_max = max_length
            
        summarizer = get_summarizer()
        summary = summarizer(
            text,
            max_length=adjusted_max,
            min_length=min(min_length, adjusted_max-10),  # Ensure min < max
            do_sample=False
        )
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Abstractive summarization error: {e}")
        return text[:max_length]  # Fallback to truncation