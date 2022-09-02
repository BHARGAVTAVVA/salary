import pickle
import streamlit as st
pickle_in=open('Salaryprediction.pkl','rb')
model=pickle.load(pickle_in)
e = st.number_input ('enter exp')
if st.button('predict'):
  r=model.predict([[e]]).squeeze()
  st.success(f'Salary is {r}')
                  
