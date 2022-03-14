import youtube_dl
import streamlit as st
import pytube
import json

url = st.text_input(label="URL of the video", placeholder="url")
btn_push = st.button(label = "Download")
if btn_push:
    if url:
        with youtube_dl.YoutubeDL(dict(forceurl=True)) as ydl:
            result = ydl.extract_info(url, download=False)
        
        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result
            p = pytube.Playlist(url)
            st.write("# **It's a playlist**")
            st.write(p.title)
            for ele in p:
                x = pytube.YouTube(ele)
                st.write(f"Name: {x.title}  url: {ele}")        
            
        else:
            # Just a video
            
            video = result
            st.write("# **It's a video**")
            st.write(f"**Title:** {video['title']}")
            for ele in video['formats']:
                st.write(f"**Format:** {ele['format_note']} {ele['ext']}")
                st.write(f"**Url:** {ele['url']}")
    else:
        st.write("**Provide Url**")
 