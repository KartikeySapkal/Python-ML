# app.py
from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        # Perform sentiment analysis using TextBlob
        analysis = TextBlob(text)
        sentiment_score = analysis.sentiment.polarity
        # Determine mood based on sentiment score
        if sentiment_score > 0:
            mood = 'Happy'
        elif sentiment_score < 0:
            mood = 'Sad'
        else:
            mood = 'neutral'
        return render_template('result.html', text=text, mood=mood)

if __name__ == '__main__':
    app.run(debug=True)
