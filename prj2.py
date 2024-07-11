import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

st.image(r"C:\Users\mahes\OneDrive\Pictures\innomatcis logo.webp")
st.title("E-mail Spam or Ham Classifier")

model=pickle.load(open(r"C:\Users\mahes\machine learning\model.pkl",'rb'))
Vectorizer=pickle.load(open(r"C:\Users\mahes\machine learning\model2.pkl", 'rb'))

Message=st.text_input("Enter the mail")
if Message:
    transformed_message = Vectorizer.transform([Message])
    result = model.predict(transformed_message)[0]

    if st.button("predict"):
        st.write(" Result: This is a",result.upper(),"Mail")  
        if result=="spam":
            st.image(r"C:\Users\mahes\OneDrive\Pictures\Download\Downloads\spam.png")
        elif result=="ham":
            st.image(r"C:\Users\mahes\OneDrive\Pictures\Download\Downloads\ham.png")