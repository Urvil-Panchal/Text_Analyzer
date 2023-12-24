import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def Sentiment_Analyzer(text):
    sia = SentimentIntensityAnalyzer()

    sentiment_score = sia.polarity_scores(text)

    compound_scores = sentiment_score['compound']

    if compound_scores >= 0.05:
        sentiment = 'Positive'

    elif compound_scores <= -0.05:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return sentiment , compound_scores

# if __name__ == '__main__':
#     s,c = Sentiment_Analyzer('I am not very Bad')

#     print(s,c)