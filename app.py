from flask import Flask , render_template, request
import Senti

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def Home():
    return render_template('home.html')

@app.route("/analyzer" , methods=['POST' , 'GET'])
def Analyzer():
    if request.method=='POST':
        text = request.form['txt']
    

    # print(text)
    sentiment , compoundScore = Senti.Sentiment_Analyzer(text)

    return render_template('home.html' ,text=text,  s=sentiment,c=compoundScore)

# if __name__ == '__main__':
#     app.run(debug=True,host='0.0.0.0')