<p align="center"> <img width='400' height='300' src="https://github.com/SinghPriya5/Credit_Score_Classification/blob/main/static/images/giphy.webp"></p> 
<div style="text-align: center; color: #2c3e50; font-family: 'Trebuchet MS', sans-serif;"> <h1 style='color:#3498db; font-size: 3em; letter-spacing: 2px;'>💳 𝕮𝖗𝖊𝖉𝖎𝖙 𝕾𝖈𝖔𝖗𝖊 𝕮𝖑𝖆𝖘𝖘𝖎𝖋𝖎𝖈𝖆𝖙𝖎𝖔𝖓 💳</h1> </div> 
<img align="right" width="500" height="600" src="https://github.com/SinghPriya5/Credit_Score_Classification/blob/main/static/images/pin.webp"> 
<h3>📊 Table of Content</h3>

* [Problem Statement](#Problem-Statement)
* [Goal](#Goal)
* [Approach](#Approach)
* [Data Collection](#Data-Collection)
* [Project Various Step](#project-various-step)
    * [Data Visualization](#Data-Visualization)
    * [Model Training](#Model-Training)
    * [Model Evalution](#Model-Evaluation)
    * [Model Selection](#Model-Selection)
    * [Model Dump](#Model-Dump)
* [Idel used](#Idel-used)
* [Model Accuracy](#Model-Accuracy)
* [Continuous Improvement](#Continuous-Improvement)
* [Deployed](#Deployed)
* [Model Interpretation](#Model-Interpretation)
* [Web View](#Web-View)
* [Bug or Feature Request](#Bug-or-Feature-Request)
* [Future Scope](#Future-Scope)
* [Conclusion](#Conclusion)
<h3>💼 Problem Statement:</h3>
<ul style="font-family: 'Courier New', monospace;"> <h2>Problem Statements for Credit Score Classification</h2> <ol> <li> <h3>Feature Distribution Analysis</h3> <p><strong>Objective:</strong> Analyze the distribution of credit-related features such as <code>age</code>, <code>income</code>, and <code>credit history length</code> among customers.</p> <p><strong>Problem:</strong> How do these features vary across the dataset, and what insights can be drawn from their distribution patterns?</p> </li> <li> <h3>Credit Score Distribution</h3> <p><strong>Objective:</strong> Examine the distribution of credit scores among the dataset.</p> <p><strong>Problem:</strong> What is the distribution of credit scores, and are there significant patterns that could impact model training?</p> </li> <li> <h3>Demographic Influence on Credit Score</h3> <p><strong>Objective:</strong> Compare key demographic features with credit scores.</p> <p><strong>Problem:</strong> How do factors like <code>education level</code>, <code>employment status</code>, and <code>marital status</code> influence credit scores?</p> </li> <li> <h3>Feature Importance Analysis</h3> <p><strong>Objective:</strong> Identify which features most strongly influence credit score predictions.</p> <p><strong>Problem:</strong> Which features exhibit the highest importance in the model, and how can this be visualized?</p> </li> <li> <h3>Model Comparison</h3> <p><strong>Objective:</strong> Compare the performance of different models on credit score classification.</p> <p><strong>Problem:</strong> Which model provides the most accurate predictions, and what are the trade-offs between different approaches?</p> </li> <li> <h3>Credit Risk Segmentation</h3> <p><strong>Objective:</strong> Segment customers into different credit risk categories based on their predicted credit scores.</p> <p><strong>Problem:</strong> How can the model effectively segment customers, and what are the business implications of these segments?</p> </li> </ol>
<h3>💡 Goal:</h3>
<div style="font-family: 'Courier New', monospace; font-size: 1.1em;"> The main goals of credit score classification using machine learning are: <ul> <li><b>Accurate Credit Scoring:</b> Accurately predict credit scores based on customer attributes.</li> <li><b>Risk Assessment:</b> Identify high-risk customers for better financial management.</li> <li><b>Customer Segmentation:</b> Segment customers into different credit risk categories.</li> <li><b>Automation:</b> Automate the credit scoring process for efficiency.</li> <li><b>Financial Insights:</b> Provide insights into factors influencing credit scores.</li> </ul> </div>
<h3>🔍 Approach:</h3>
<div style="font-family: 'Courier New', monospace; font-size: 1.1em;"> The process involves Data Exploration, Data Cleaning, Feature Engineering, Model Building, and Model Testing. Various machine learning algorithms will be evaluated to determine the best model for credit score classification. </div>
<h3>📈 Data Collection:</h3>
<ul style="font-family: 'Courier New', monospace; font-size: 1.1em;">
  <li><b>Month:</b> The month of data collection.</li>
  <li><b>Name:</b> Customer's name.</li>
  <li><b>Age:</b> Customer's age.</li>
  <li><b>SSN:</b> Social Security Number of the customer.</li>
  <li><b>Occupation:</b> Customer's occupation.</li>
  <li><b>Annual_Income:</b> The annual income of the customer.</li>
  <li><b>Monthly_Inhand_Salary:</b> The monthly salary received by the customer in hand.</li>
  <li><b>Num_Bank_Accounts:</b> The number of bank accounts held by the customer.</li>
  <li><b>Num_Credit_Card:</b> The number of credit cards owned by the customer.</li>
  <li><b>Interest_Rate:</b> The average interest rate on credit cards or loans.</li>
  <li><b>Num_of_Loan:</b> The number of loans taken by the customer.</li>
  <li><b>Type_of_Loan:</b> The type of loans taken by the customer.</li>
  <li><b>Delay_from_due_date:</b> The average number of days the customer delays payment beyond the due date.</li>
  <li><b>Num_of_Delayed_Payment:</b> The number of delayed payments made by the customer.</li>
  <li><b>Changed_Credit_Limit:</b> The amount by which the credit limit was changed.</li>
  <li><b>Num_Credit_Inquiries:</b> The number of credit inquiries made for the customer.</li>
  <li><b>Credit_Mix:</b> The mix of various credit types (e.g., secured/unsecured loans).</li>
  <li><b>Outstanding_Debt:</b> The total outstanding debt of the customer.</li>
  <li><b>Credit_Utilization_Ratio:</b> The ratio of credit used to total credit available.</li>
  <li><b>Credit_History_Age:</b> The age of the customer's credit history.</li>
  <li><b>Payment_of_Min_Amount:</b> Whether the customer pays only the minimum amount due (Yes/No).</li>
  <li><b>Total_EMI_per_month:</b> The total Equated Monthly Installment (EMI) paid per month.</li>
  <li><b>Amount_invested_monthly:</b> The amount invested by the customer monthly.</li>
  <li><b>Payment_Behaviour:</b> The overall payment behavior of the customer.</li>
  <li><b>Monthly_Balance:</b> The balance left at the end of each month after expenses.</li>
  <li><b>Credit_Score:</b> The credit score of the customer (Good, Standard, or Poor).</li>
</ul>

<p style="font-family: 'Courier New', monospace; font-size: 1.1em;">
  This comprehensive dataset allows for in-depth analysis and modeling to predict credit scores accurately, helping financial institutions assess customer creditworthiness.
</p>

<h3>📊 Project Various Steps:</h3>
<ul style="font-family: 'Courier New', monospace; font-size: 1.1em;"> <li><b>Data Visualization:</b> Correlation matrices, boxplots, scatter plots, and bar charts to understand relationships between variables.</li> <li><b>Model Training:</b> <ul> <li><b>Split Data:</b> Dataset divided into training and test sets (80% training, 20% testing).</li> <li><b>Model Training:</b> Models trained using the training data.</li> <li><b>Hyperparameter Tuning:</b> Techniques like RandomizedSearchCV used to optimize model parameters.</li> </ul> </li> <li><b>Model Evaluation:</b> Performance evaluated using metrics like Accuracy, Precision, Recall, and Confusion Matrix.</li> <li><b>Model Selection:</b> Selection of the best-performing model based on evaluation metrics.</li> <li><b>Model Deployment:</b> Deploy the selected model for real-time predictions.</li> </ul>
<h3>🛠️ Tools Used:</h3>
<ul style="font-family: 'Courier New', monospace; font-size: 1.1em;"> <li>Jupyter Notebook</li> <li>VS Code</li> <li>PyCharm</li> </ul>
<h3>📉 Model Performance:</h3>
<div style="font-family: 'Courier New', monospace; font-size: 1.1em;"> The model achieved an accuracy of 80%. </div>
<h3>🔄 Continuous Improvement:</h3>
<ul style="font-family: 'Courier New', monospace; font-size: 1.1em;"> <li><b>Model Monitoring:</b> Ongoing tracking of the model’s performance to ensure accuracy.</li> <li><b>Retraining:</b> Periodic retraining with new data to adapt to changing financial trends.</li> </ul>
<h3>🚀 Deployed:</h3>
Deployed on Render -- [Link](https://github.com/SinghPriya5/Breat_Cancer_Classification/issues)

<br> the instruction given on [Render Documentation](https://docs.render.com/deploy-flask) to deploy a web app.

<br> Follow instructions on Render Documentation to deploy a web app.

<b>Model Deployment:</b> Deploy the model to a production environment for real-time credit score predictions.

<b>APIs:</b> Develop an API that allows users to input customer details and receive a predicted credit score.

<h3>📋 Model Interpretation</h3>
<b>Feature Importance:</b> Identify which features most influence the credit score predictions using techniques like feature importance scores in tree-based models or SHAP values.

<h3>🌐 Web View:</h3>

**Frontend**
<p align="center">
  <img src="https://github.com/SinghPriya5/Credit_Score_Classification/blob/main/static/images/frontend.png" alt="Frontend" width="700" height="600">
</p>

**Inserting Value and Predicted Value**

<p align="center">
  <img src="https://github.com/SinghPriya5/Credit_Score_Classification/blob/main/static/images/inserting_value.png" alt="Inserting Value" width="700" height="500"> <img src="https://github.com/SinghPriya5/Credit_Score_Classification/blob/main/static/images/predicting_result.png" alt="Predicted Value" width="700" height="500">
</p>

<h3>💼 Bug or Feature Request</h3>
If you find a bug (the website couldn't handle the query and/or gave undesired results), kindly open an issue here by including your search query and the expected result.

<h3>📈 Future Scope:</h3>
<ul style="font-family: 'Courier New', monospace; font-size: 1.1em;"> <li>Explore additional machine learning algorithms to enhance predictive performance.</li> <li>Optimize the Flask application for faster response times and better scalability.</li> <li>Enhance the frontend interface for a more user-friendly experience.</li> <li>Expand the model to include more financial indicators and risk analysis features.</li> </ul>
<h3>💡 Conclusion:</h3>
<div style="font-family: 'Courier New', monospace; font-size: 1.1em;"> Credit score classification using machine learning is a critical tool for financial institutions, enabling accurate risk assessment and customer segmentation. The project demonstrates the effectiveness of data-driven decision-making in the financial sector, helping to improve credit lending practices and customer management. </div> <div style="text-align: center; font-family: 'Trebuchet MS', sans-serif; color: #3498db; margin-top: 20px;">
<h2>🎉 Thanks!!!</h2> </div>
<p align="center"> <img width='400' height='300' src="https://github.com/SinghPriya5/Credit_Score_Classification/blob/main/static/images/credit_score.webp"></p> 
