import streamlit as st
import pandas as pd
tabel=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [11,12,13,14,15,16,17]})
st.title("Hi! I am Streamlit Web App")
st.subheader("Hi I am your subheader")
st.header("I an Header)")
st.text("Hi I am text function and programmers uses me inplace of paragraph tag")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
st.caption("Hi I am Caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
code="""
print("hello World)
def funct():
    return 0;"""
st.code(code,language="python")
st.write("## H2")
st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4ms⁻¹")
st.table(tabel)
st.dataframe(tabel)
st.image("DJI_0002.JPG", caption="This is my Image")
st.video("sawah Spyderweb.mp4")