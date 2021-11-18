# import statements
import streamlit as st
import numpy as np
import pandas as pd
import pickle
import pandas as pd

def word_to_char(word):
    return list(word)


def load_vectorizer():
    #Loading vectorizer from pickle file
    file = open("tfidf_password_strength.pickle",'rb')
    saved_vectorizer = pickle.load(file)
    file.close()
    return saved_vectorizer


def load_model():
    #Loading model from pickle file
    file = open("final_model.pickle",'rb')
    final_model = pickle.load(file)
    file.close()
    return final_model

def password_strength_check(input,vectorizer,model):
    X_password=np.array([input])
    X_predict=vectorizer.transform(X_password)
    y_pred=model.predict(X_predict)
    strengh=y_pred[0]
    if strengh==0:
        return 'Weak Password'
    if strengh==1:
        return 'Medium Password'
    if strengh==2:
        return 'Strong Password'


st.title("Password strength check Application")
st.text('This application used a trained ML model to check the password strength with 98% accuracy.')

user_password=st.text_input('Enter password text to check strength',type="password")
if st.button('Check'):
    vectorizer=load_vectorizer()
    model=load_model()
    st.write(password_strength_check(user_password,vectorizer,model))


st.text('Kaggle dataset url: https://www.kaggle.com/bhavikbb/password-strength-classifier-dataset')


