import joblib
import json
import pandas as pd
from azureml.core.model import Model

def init():
    global model
    # Load the model from the registered model
    model_path = Model.get_model_path("loan_approval_model")
    model = joblib.load(model_path)

def run(raw_data):
    try:
        # Convert raw data to a pandas DataFrame
        data = pd.DataFrame(json.loads(raw_data)["data"])
        
        # Make predictions
        predictions = model.predict(data)
        
        # Return predictions as JSON
        return json.dumps({"predictions": predictions.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})
