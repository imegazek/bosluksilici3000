import streamlit as st

st.title("Metninizdeki boşlukları siliyoruz. Hem de ÜCRETSİZ!")
cumle = st.text_input("Buraya yazın:")
result = cumle.replace(" ","")
st.title(result)