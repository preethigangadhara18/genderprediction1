import pandas as pd
import numpy as np
import pickle
import streamlit as st
import os
st.title('Gender Prediction')
gp1=st.sidebar.slider("nose_wide",0.0,20.0)
gp2=st.sidebar.slider("nose_long",0.0,20.0)
gp3=st.sidebar.slider("distance_nose_to_lip_long",0,20)

with open('model.pkl','rb') as f :
    model=pickle.load(f)
    f.close()
if st.button('predict') :
    data=np.array([[gp1,gp2,gp3]])
    prediction=model.predict(data)[0]

    if prediction == 0:
      st.write("Female")
      st.balloons()
    elif prediction == 1:
     st.write("Male")
     st.balloons()

st.image(r'C:\Users\preet\OneDrive\Documents\PREETHI PERSONAL\python codes\dp1111.jpg')