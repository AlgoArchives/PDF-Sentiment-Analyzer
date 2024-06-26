# PDF Sentiment Analyzer

PDF Sentiment Analyzer is a simple web application that allows users to upload earnings call PDF files and get sentiment scores along with a sentiment analysis graph. The application uses Flask for the backend, NLTK's VADER for sentiment analysis, and Matplotlib for plotting the results.

## Features

- Upload PDF files for sentiment analysis.
- Extract text from PDF files.
- Perform sentiment analysis using VADER.
- Display sentiment scores and a sentiment analysis graph.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vikranth3140/PDF-Sentiment-Analyzer.git
   cd PDF-Sentiment-Analyzer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application using Gunicorn:
   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:8000/`.

3. Upload a PDF file to get the sentiment analysis results.

## Project Structure

```
PDF-Sentiment-Analyzer/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── styles.css
│   └── scripts.js
└── uploads/
```

## License

This project is licensed under the [MIT License](LICENSE).