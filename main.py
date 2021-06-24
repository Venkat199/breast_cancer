from flask import Flask,redirect,url_for,render_template,request
import pickle
from sklearn.neighbors import KNeighborsClassifier
app=Flask(__name__)
model = pickle.load(open('breastcancer_model.sav','rb'))

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict/<result>')
def predict(result):
    return 'The tumor is {}'.format(result)


@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        val1=float(request.form['val1'])
        val2=float(request.form['val2'])
        val3=float(request.form['val3'])
        val4=float(request.form['val4'])
        val5=float(request.form['val5'])
        inp = [[val1,val2,val3,val4,val5]]
        pred = model.predict(inp)
        if pred[0] == 0:
            res = 'benign'
        else:
            res = 'cancer'

    return redirect(url_for('predict', result=res))


if __name__=='__main__':
    app.run(debug=True)