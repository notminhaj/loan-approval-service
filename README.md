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

An azure account might be needed to run this.
