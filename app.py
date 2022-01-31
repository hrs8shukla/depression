from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('depression.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("depression.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)

    if prediction== 1:
        return render_template('depression.html',pred='You might have depression {}'.format(prediction),bhai="kuch karna hain iska ab?")
    else:
        return render_template('depression.html',pred='You dont have depression  {}'.format(prediction),bhai="Your Forest is Safe for now")


if __name__ == '__main__':
    app.run(debug=True)
