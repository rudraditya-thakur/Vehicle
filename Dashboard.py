import streamlit as st

st.set_page_config(layout="wide")

video_files = [
    "processed_videos/video1_compressed.mp4",
    "processed_videos/video2_compressed.mp4",
    "processed_videos/video3_compressed.mp4",
    "processed_videos/pedestrian_hit.mp4",
    "processed_videos/video5_compressed.mp4",
    "processed_videos/video6_compressed.mp4",
]

cols = st.columns(2)

for index, video in enumerate(video_files):
    col_index = index % 2
    cols[col_index].video(video, loop=True, autoplay=True, muted=False)
