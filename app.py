from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model_pipeline.joblib')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    if request.method == 'POST':
        Month= request.form['Month']
        Age=request.form['Age']
        Occupation= request.form['Occupation']
        Annual_Income= request.form['Annual_Income']
        Monthly_Inhand_Salary= int(request.form['Monthly_Inhand_Salary'])
        Num_Bank_Accounts= int(request.form['Num_Bank_Accounts'])
        Num_Credit_Card= int(request.form['Num_Credit_Card'])
        Interest_Rate= int(request.form['Interest_Rate'])
        Num_of_Loan= request.form['Num_of_Loan']
        Type_of_Loan= request.form['Type_of_Loan']
        Delay_from_due_date= int(request.form['Delay_from_due_date'])
        Num_of_Delayed_Payment= request.form['Num_of_Delayed_Payment']
        Changed_Credit_Limit= request.form['Changed_Credit_Limit']
        Num_Credit_Inquiries= int(request.form['Num_Credit_Inquiries'])
        Credit_Mix= request.form['Credit_Mix']
        Outstanding_Debt= request.form['Outstanding_Debt']
        Credit_Utilization_Ratio= float(request.form['Credit_Utilization_Ratio'])
        Credit_History_Age= int(request.form['Credit_History_Age'])
        Payment_of_Min_Amount= request.form['Payment_of_Min_Amount']
        Total_EMI_per_month= float(request.form['Total_EMI_per_month'])
        Amount_invested_monthly= request.form['Amount_invested_monthly']
        Payment_Behaviour= request.form['Payment_Behaviour']
        Monthly_Balance= float(request.form['Monthly_Balance'])
    
    
    # Convert form data to DataFrame for prediction
        features = pd.DataFrame({
            'Month':[Month], 
            'Age':[Age],
            'Occupation': [Occupation],
            'Annual_Income': [Annual_Income],
            'Monthly_Inhand_Salary':[Monthly_Inhand_Salary], 
            'Num_Bank_Accounts': [Num_Bank_Accounts],
            'Num_Credit_Card':[Num_Credit_Card], 
            'Interest_Rate': [Interest_Rate],
            'Num_of_Loan':[Num_of_Loan], 
            'Type_of_Loan': [Type_of_Loan],
            'Delay_from_due_date':[Delay_from_due_date],
            'Num_of_Delayed_Payment': [Num_of_Delayed_Payment],
            'Changed_Credit_Limit': [Changed_Credit_Limit],
            'Num_Credit_Inquiries': [Num_Credit_Inquiries],
            'Credit_Mix':[Credit_Mix],
            'Outstanding_Debt': [Outstanding_Debt],
            'Credit_Utilization_Ratio': [Credit_Utilization_Ratio],
            'Credit_History_Age': [Credit_History_Age],
            'Payment_of_Min_Amount':[Payment_of_Min_Amount], 
            'Total_EMI_per_month': [Total_EMI_per_month],
            'Amount_invested_monthly':[Amount_invested_monthly], 
            'Payment_Behaviour': [Payment_Behaviour],
            'Monthly_Balance': [Monthly_Balance]
        })
    
    # Make prediction
        prediction = model.predict(features)
        prediction=prediction[0]
        if prediction == 0:
            prediction="Good"
        elif prediction == 1:
            prediction = "Poor"
        else:
            prediction="Standard"
    
        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
