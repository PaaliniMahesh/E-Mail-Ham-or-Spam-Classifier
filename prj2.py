import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

st.image(r"innomatcis logo.webp")
st.title("E-mail Spam or Ham text Classification")

model=pickle.load(open(r"model.pkl",'rb'))
Vectorizer=pickle.load(open(r"model2.pkl", 'rb'))

Message=st.text_area("Enter the mail")
if Message:
    transformed_message = Vectorizer.transform([Message])
    result = model.predict(transformed_message)[0]

    if st.button("predict"):
        st.write(" Result: This is a",result.upper(),"Mail")  
        if result=="spam":
            st.image(r"spam.png")
        elif result=="ham":
            st.image(r"ham.png")
