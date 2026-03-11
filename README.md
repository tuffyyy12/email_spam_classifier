# email_spam_classifier
A beginner-friendly machine learning project that classifies emails as spam or not spam using NLP techniques. Built with Python, Scikit learn, and  with Streamlit.

## Overview

Email inboxes are constantly flooded with unwanted messages. This project explores how **machine learning and natural language processing (NLP)** can be used to automatically identify whether an email is **Spam** or **Not Spam**.

The model is trained on email text and learns patterns that typically appear in spam messages. Once trained, it can analyze new email content and predict whether it is likely to be spam.

To make the model easy to interact with, a simple **Streamlit web interface** is included. Users can type or paste an email message into the app and instantly see the prediction.



## What This Project Does

* Takes email text as input
* Processes the text using **NLP techniques**
* Converts the text into numerical features
* Uses a trained **machine learning model** to classify the email
* Displays whether the email is **Spam** or **Not Spam**



## Technology Stack

This project was built using:

* **Python** for development
* **Scikit-learn** for training the machine learning model
* **Pandas** for data handling and preprocessing
* **Streamlit** to create a simple interactive interface
* **Natural Language Processing (NLP)** techniques for text analysis
* **CountVectorizer / TF-IDF** for converting text into machine-readable features



## Project Structure


Email-Spam-Classifier
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── dataset.csv
└── README.md


**app.py**
Contains the Streamlit application that allows users to input email text and view predictions.

**model.pkl**
The trained machine learning model used to classify emails.

**vectorizer.pkl**
The text vectorizer used to transform email text into numerical features.

**dataset.csv**
The dataset used to train the spam detection model.


## Running the Project

1. Clone the repository


git clone https://github.com/your-username/email-spam-classifier.git

2. Navigate to the project folder


cd email-spam-classifier

3. Run the Streamlit application

streamlit run app.py


After running the command, the application will open in your browser.
You can then enter email text and see the model's prediction.


## Future Improvements

Some possible improvements for this project include:

* Improving model accuracy with more training data
* Deploying the application online
* Adding more advanced NLP preprocessing techniques
* Allowing multiple emails to be analyzed at once



## About This Project

This project was created as a hands-on exploration of **machine learning, natural language processing, and building simple interactive applications with Streamlit**. It demonstrates how text classification models can be applied to solve real-world problems such as spam detection.


