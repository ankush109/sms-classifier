import streamlit as st
import pickle
import string 
import nltk.corpus
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer 
ps=PorterStemmer()


import string

def transform_text(text):
 
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []

    for word in text:
     
        if word.isalnum():
            y.append(word)
    text = y[:]
    
    y.clear()
    
    for word in text:
        if word not in stopwords.words('english') and word not in string.punctuation:
            y.append(word)
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
st.title('email/sms spam classifier')
sms= st.text_input("enter the message")
if st.button('predict'):
        
        # 1. preprocess 
    tf_sms=transform_text(sms)

# 2 vectorize
    vi=tfidf.transform([tf_sms])

# 3 predict
    result=model.predict(vi)[0]
    if result == 1:
       st.header("spam")
    else:
         st.header("not spam")

  
