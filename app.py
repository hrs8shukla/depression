from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("dep.pkl", 'rb'))


@app.route('/')
def hello_world():
    return render_template("depression.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)
    if output > str(0.5):
        return render_template('depression.html', pred='\nProbability of depression is {} Please Consult with a Psychiatrist'.format(output), bhai="Unsafe")
    else:
        return render_template('depression.html', pred='You are safe.\n Probability of depression is {}'.format(output), bhai="Safe")


if __name__ == '__main__':
    app.run(debug=True)
