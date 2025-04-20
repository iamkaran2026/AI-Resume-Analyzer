
# 🧠 AI Resume Analyzer using NLP

A Streamlit-based AI-powered Resume Analyzer that extracts information from resumes (PDF/DOCX), evaluates skills, and matches candidates against a job description using Natural Language Processing (NLP) and Machine Learning techniques.

---

## 🚀 Demo

> Upload multiple resumes and a job description — get match scores, extracted skills, and insights in real time!

---

## 📂 Features

- 📄 Supports PDF and DOCX resumes
- 🔍 Extracts and analyzes text using spaCy NLP
- 🧠 Matches resumes to job descriptions using TF-IDF and cosine similarity
- 📊 Displays match scores and skills in a clean, interactive UI (via Streamlit)
- ✅ Easy to expand with BERT embeddings or database storage

---

## 📁 Project Structure

```
ai-resume-analyzer/
│
├── app.py                  # Main Streamlit app
├── resume_parser.py        # Extract text from resumes
├── job_matcher.py          # Resume-JD similarity engine
├── utils.py                # Skill extraction, cleaning, helpers
├── resumes/                # Folder to store uploaded resumes
├── job_description.txt     # Sample JD for testing
└── requirements.txt        # Required Python libraries
```

---

## 🛠️ Installation

1. **Clone the repo**  
```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## 🧪 Run the App

```bash
streamlit run app.py
```

Then open your browser at:  
📍 `http://localhost:8501`

---

## 📥 Sample Files

- ✅ Sample Resume (PDF)
- 🧾 Sample Job Description (Data Scientist)

---

## 🧠 Technologies Used

- Python 🐍  
- Streamlit 📊  
- spaCy 🔍  
- Scikit-learn 🔬  
- PyMuPDF + python-docx (for file parsing)

---

## 📌 Future Improvements

- ✅ Use transformer-based embeddings (e.g., BERT) for better semantic matching
- ✅ Add filtering by years of experience, education, and domain
- ✅ Export match reports to CSV/Excel
- ✅ Deploy online with Streamlit Cloud or Heroku

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss what you would like to change or improve.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 💬 Contact

Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/karan-mevada-19745527b/) or email at `karanmewada26.com`.

---

⭐ If you find this project helpful, don’t forget to give it a star!
