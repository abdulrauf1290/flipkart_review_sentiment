from flask import Flask, render_template, request
import joblib
from textblob import TextBlob

app = Flask(__name__)

# Load the sentiment analysis model
model = joblib.load("xgboost.pkl")

# Function to get sentiment emoji
def get_sentiment_emoji(sentiment):
    if sentiment > 0:
        return "Positive 😊"  # Positive emoji
    elif sentiment < 0:
        return "Negative 😞"  # Negative emoji
    else:
        return "Neutral 😐"  # Neutral emoji

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        text = request.form["text"]
        # Perform sentiment analysis
        sentiment_score = TextBlob(text).sentiment.polarity
        sentiment = get_sentiment_emoji(sentiment_score)
        # Change background color based on sentiment
        if sentiment_score > 0:
            background_color = "red"
        elif sentiment_score < 0:
            background_color = "black"
        else:
            background_color = "white" 
            
        return render_template("index.html", sentiment=sentiment, background_color=background_color, text=text)
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True,host=0.0.0.0)



