from crypt import methods
from flask import Flask, request, render_template
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from random import shuffle
nltk.download('vader_lexicon')

app = Flask(__name__)

def sentiment_analysis(text):
  sia = SentimentIntensityAnalyzer()
  return sia.polarity_scores(text)

@app.route('/', methods =["GET", "POST"])
def main():
    if request.method == 'POST':
        textarea = request.form.get("textarea")
        text = sentiment_analysis(textarea)
        compound = text['compound']
        if float(compound) >= 0.25:
            result = "Positive 👍 Scores: {}".format(float(compound))
        elif float(compound) <= -0.25:
            result = "Nagative 👎 Scores: {}".format(float(compound))
        else:
            result = "Neutral 😐"
        return render_template("index.html", data=result)
    else:
        return render_template("index.html", data=None)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8000)