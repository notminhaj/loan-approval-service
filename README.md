# loan-approval-service
deploying my first ML model!!

This is a Kaggle competition where I was tasked with creating a loan approval model using the data that was given to me. I used a random forest regressor to build my model. Decided not to go crazy with all the ML strategies to increase my accuracy since my main focus was to have a deployed model to which I could make api calls.


**Training Script**

This is a notebook where I trained my random forest regressor. I proceeded to generate a submission file to send to the kaggle competition. After that, I deployed my model to azure. After running the last cell, you should receive a "scoring URI" you are to copy this and paste it into the "app.py" file where indicated.


**app.py**

This is the python file where I created a basic web page interface using gradio. Make sure to paste your scoring URI from the training script notebook in the scoring_uri variable at the top.


**score.py**

This is a necessary file needed to make sure everything runs.



Unfortunately the "loan approval model.pkl" was too large to upload to github so you have to generate it using the training script by training the model on train_data (it does it for you).


**How to run**

An azure subscription will be needed to run this.

1. Navigate to the azure ML studio and create a resource. Once inside the resource head to the "data" section and import the train and test data making sure to follow the same naming convention.
2. Go to the "compute" section, then create and start a compute session. Then import the following files: "training script.ipynb", "score.py". After that, run every cell in the training script (could take ~20 mins).
3. Download the  "app.py" file to your local PC.
4. Open cmd and go to the path to your app.py file. Run the following commands:
python -m venv gradio-env
gradio-env\Scripts\activate
pip install gradio requests azure-identity
python app.py
5. After running the script, Gradio will start a local server. You’ll see a message with a URL, like: Running on local URL:  http://127.0.0.1:7860

You can open this URL in your browser to view and use the Gradio interface.
