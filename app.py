from flask import Flask,render_template,request
import pickle
import sklearn
import numpy


app = Flask(__name__)

model = pickle.load(open('heart_failure.pkl','rb'))

@app.route('/')
def input():
    return render_template('index.html')


@app.route('/output',methods=['GET','POST'])
def output():
    age = request.form['age']
    creatinine_phosphokinase = request.form['creatinine_phosphokinase']
    ejection_fraction = request.form['ejection_fraction']
    high_blood_pressure = request.form['high_blood_pressure']
    platelets = request.form['platelets']
    serum_creatinine = float(request.form['serum_creatinine'])
    serum_sodium = request.form['serum_sodium']
    time = request.form['time']

    input = numpy.array([[age,creatinine_phosphokinase,ejection_fraction,high_blood_pressure,platelets,
    serum_creatinine,serum_sodium,time]])
    output = model.predict(input)
    return render_template('output.html',data=output)


if __name__=='__main__':
    app.run(debug=True)



