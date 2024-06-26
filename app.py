from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import fitz  # PyMuPDF
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    text = extract_text_from_pdf(file_path)
    sentiment = analyze_sentiment(text)
    plot_sentiment(sentiment, filename)
    return jsonify({'sentiment': sentiment})


def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    return text


def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    return sentiment_scores


def plot_sentiment(sentiment, filename):
    categories = ['Negative', 'Neutral', 'Positive']
    scores = [sentiment['neg'], sentiment['neu'], sentiment['pos']]
    colors = ['#ff4c4c', '#ffc107', '#4caf50']

    plt.figure(figsize=(8, 6))
    plt.bar(categories, scores, color=colors)
    plt.xlabel('Sentiment')
    plt.ylabel('Score')
    plt.title('Sentiment Analysis')
    plt.ylim(0, 1)

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{filename}_sentiment.png")
    plt.savefig(output_path)
    plt.close()


if __name__ == '__main__':
    app.run(debug=True)