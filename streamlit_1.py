import streamlit as st
import pytube

url = st.text_input(label="URL of the video", placeholder="url",key="1")
btn_push = st.button(label = "List the streams")

if btn_push and url:
    yt = pytube.YouTube(url)
    st.write(f"# **{yt.title}**")
    for i in yt.streams:
        st.write(f"##### {i}")
        st.write(i.url)