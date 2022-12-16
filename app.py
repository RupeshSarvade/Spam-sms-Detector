import streamlit as st
import sklearn
import pickle
import nltk
from nltk.corpus import stopwords #for stopwords
import string  #for punctuation
from nltk.stem.porter import PorterStemmer #for stemming


#creating variable of tfid and random forest

tfid = pickle.load(open("tfid.pkl","rb"))
rfc = pickle.load(open("rfc.pkl","rb"))

#transformation of text function

#stemming
ps = PorterStemmer()
stopwords.words('english')
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    new_text = []
    for i in text:
        if i.isalnum():
            new_text.append(i)
    text = new_text[:]
    new_text.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            new_text.append(i)
    text = new_text[:]
    new_text.clear()
    for i in text:
        new_text.append(ps.stem(i))

    return " ".join(new_text)


st.title("SMS/Email Spam Detector")

input = st.text_input("Enter Your Text Here: ")

#preproccesing
transformed_input = transform_text(input)

#vectorization
vector_input = tfid.transform([transformed_input])

#prediction
prediction = rfc.predict(vector_input)[0]
button = st.button("predict")


if button == True:
    if prediction == 1:
        st.header("This is a Spam Message.")
    else:
        st.header("This is not a Spam Message.")


#Hide Streamlit style

hide_st_style= """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden'}
                </style>
"""

st.markdown(hide_st_style,unsafe_allow_html=True)
