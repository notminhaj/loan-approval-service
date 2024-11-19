
import gradio as gr
import requests
import json
from azure.identity import DefaultAzureCredential

# Set up Azure ML model endpoint details
scoring_uri = "YOUR SCORING URI"  # Replace with your model's scoring URI

# Function to get the AAD token for authentication
def get_auth_token():
    credential = DefaultAzureCredential()
    token = credential.get_token("https://ml.azure.com/.default").token
    return token

def predict(
    person_age, person_income, person_emp_length, loan_amnt, loan_int_rate, loan_percent_income,
    cb_person_default_on_file, cb_person_cred_hist_length,
    person_home_ownership_OTHER, person_home_ownership_OWN, person_home_ownership_RENT,
    loan_intent_EDUCATION, loan_intent_HOMEIMPROVEMENT, loan_intent_MEDICAL,
    loan_intent_PERSONAL, loan_intent_VENTURE,
    loan_grade_B, loan_grade_C, loan_grade_D, loan_grade_E, loan_grade_F, loan_grade_G
):
    # Prepare input data for the model
    input_data = json.dumps({
        "data": [[
            person_age, person_income, person_emp_length, loan_amnt, loan_int_rate, loan_percent_income,
            cb_person_default_on_file, cb_person_cred_hist_length,
            person_home_ownership_OTHER, person_home_ownership_OWN, person_home_ownership_RENT,
            loan_intent_EDUCATION, loan_intent_HOMEIMPROVEMENT, loan_intent_MEDICAL,
            loan_intent_PERSONAL, loan_intent_VENTURE,
            loan_grade_B, loan_grade_C, loan_grade_D, loan_grade_E, loan_grade_F, loan_grade_G
        ]]
    })
    
    # Set headers and authenticate with AAD token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_auth_token()}"
    }
    
    # Send request to the model endpoint and capture response
    response = requests.post(scoring_uri, data=input_data, headers=headers)
    
    # Parse the response and directly extract the prediction
    response_data = json.loads(response.text)
    
    # Return "Approved" or "Rejected" based on the prediction
    return "Approved" if response_data == '{"predictions": [1]}' else "Rejected"

# Define Gradio interface with appropriate inputs for each feature
inputs = [
    gr.components.Number(label="Person Age"),
    gr.components.Number(label="Person Income"),
    gr.components.Number(label="Person Employment Length"),
    gr.components.Number(label="Loan Amount"),
    gr.components.Number(label="Loan Interest Rate"),
    gr.components.Number(label="Loan Percent Income"),
    gr.components.Checkbox(label="CB Person Default on File"),
    gr.components.Number(label="CB Person Credit History Length"),
    
    # One-hot encoded features for person_home_ownership
    gr.components.Checkbox(label="Person Home Ownership OTHER"),
    gr.components.Checkbox(label="Person Home Ownership OWN"),
    gr.components.Checkbox(label="Person Home Ownership RENT"),
    
    # One-hot encoded features for loan_intent
    gr.components.Checkbox(label="Loan Intent EDUCATION"),
    gr.components.Checkbox(label="Loan Intent HOMEIMPROVEMENT"),
    gr.components.Checkbox(label="Loan Intent MEDICAL"),
    gr.components.Checkbox(label="Loan Intent PERSONAL"),
    gr.components.Checkbox(label="Loan Intent VENTURE"),
    
    # One-hot encoded features for loan_grade
    gr.components.Checkbox(label="Loan Grade B"),
    gr.components.Checkbox(label="Loan Grade C"),
    gr.components.Checkbox(label="Loan Grade D"),
    gr.components.Checkbox(label="Loan Grade E"),
    gr.components.Checkbox(label="Loan Grade F"),
    gr.components.Checkbox(label="Loan Grade G"),
]

# Define the output
outputs = gr.components.Textbox(label="Prediction")

# Create the Gradio interface
interface = gr.Interface(fn=predict, inputs=inputs, outputs=outputs, title="Loan Approval Prediction")

# Launch the Gradio app
interface.launch(share=True)