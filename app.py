from flask import Flask, escape, request, render_template
import pickle

app = Flask(__name__, template_folder='templets')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
                
        RnD_Spend = float(request.form['R&D Spend'])
        Administration = float(request.form['Administration'])
        Marketing_Spend = float(request.form['Marketing Spend'])
        State = request.form['State']

        if(State=="California"):
            State=0
        elif(State=="Florida"):
            State=1
        else:
            State=2
 
        prediction = model.predict([[RnD_Spend, Administration, Marketing_Spend, State]])
     
        

        return render_template("index.html", prediction_text="The company profit is {}".format(prediction))


    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


