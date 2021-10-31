from flask import Flask,render_template,url_for,request
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		weight=request.form['weight']
		weight=float(weight)
		height=request.form['height']
		height=float(height)
		my_prediction = round(weight/((height/100)**2),2)
		type=""
		if my_prediction<=18.5:
			type="Underweight"
		if my_prediction>18.5 and my_prediction<=24.9:
			type="Normal Weight"
		if my_prediction>=25 and my_prediction<=29.9:
			type="OverWeight"
		if my_prediction>=30:
			type="Obesity"
	return render_template('result.html',prediction = my_prediction,predicttype=type)



if __name__ == '__main__':
	app.run(debug=True)