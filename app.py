from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.route("/")
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    # return jsonify({"answer":'dada'})
    # return render_template('test.html',prediction_text='dada')
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer":response}
    # print(text,'----',message)
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug = True)