# Task 6: Text Summarization Project
This project focuses on developing a **modular text summarization system** that includes both **extractive** and **abstractive** approaches. It's designed with flexibility and clarity for educational and real-world use.

## 🔧 Features
- 🧹 Text Preprocessing: Cleaning, tokenizing, sentence splitting
- 📊 Extractive Summarization: Using TF-IDF and clustering (KMeans)
- 🧠 Abstractive Summarization: Using Transformer-based models (e.g., BART, T5)
- 🧪 Evaluation: ROUGE score comparison
- 🌐 Input options: Direct input, file upload, or URL scraping

## 🗂️ Project Structure
text_summarizer/
├── config.py              # Configuration and constants
├── preprocess.py          # Text cleaning and sentence splitting
├── extractive.py          # Extractive summarization
├── abstractive.py         # Abstractive summarization using transformers
├── evaluate.py            # ROUGE and evaluation metrics
├── app.py or main.py      # CLI/Flask interface
└── requirements.txt       # Python dependencies

## 🚀 How to Run
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Task_6_Text_Summarization.git
cd Task_6_Text_Summarization
```
### 2. Set Up Environment
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Run the Summarizer
```bash
python main.py  # or app.py if using Flask
```

## 📄 License
This project is licensed under the [MIT License](LICENSE).
