from rouge import Rouge

rouge = Rouge()

def evaluate_summary(generated, reference):
    try:
        return rouge.get_scores(generated, reference)[0]
    except:
        return {"rouge-1": {"f": 0}, "rouge-2": {"f": 0}, "rouge-l": {"f": 0}}