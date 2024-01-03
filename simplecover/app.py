import pyperclip
import streamlit as st
from dotenv import load_dotenv

from .llm.generic import generate

load_dotenv()

st.set_page_config(layout="wide")

placeholder = st.empty()

cv_content = ""
jd_content = ""
if "cl_content" not in st.session_state:
    st.session_state["cl_content"] = ""
cl = st.session_state["cl_content"]


def gen_cover_letter(cv, jd):
    print(f"generate cover letter called! {cv} \n {jd}")
    st.session_state["cl_content"] = generate(cv, jd)


with placeholder.container():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.subheader("Your CV:")
        cv_content = st.text_area(
            "cv", "", height=400, label_visibility="hidden")
    with col2:
        st.subheader("Job description:")
        jd_content = st.text_area(
            "jd", "", height=400, label_visibility="hidden")
        st.button("Generate", help="click to regenerate your cover letter!",
                  on_click=gen_cover_letter, args=(cv_content, jd_content), use_container_width=True)
    with col3:
        st.subheader("Cover letter: ")
        cl_content = st.text_area(
            "cl", st.session_state["cl_content"], key="cl_content", height=400, label_visibility="hidden")
        col3_1, col3_2 = st.columns([3, 1])
        with col3_2:
            st.button("copy", on_click=pyperclip.copy, args=(
                st.session_state["cl_content"], ), use_container_width=True)
