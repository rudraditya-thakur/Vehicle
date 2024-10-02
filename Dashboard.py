import streamlit as st

st.set_page_config(layout="wide")

# List of video files and their corresponding camera titles
video_files = [
    "processed_videos/video1_compressed.mp4",
    "processed_videos/video2_compressed.mp4",
    "processed_videos/pedestrian_hit.mp4",
    "processed_videos/video5_compressed.mp4",
    "processed_videos/video6_compressed.mp4",
]

# Create titles for the cameras
camera_titles = [f"Camera {i + 1}" for i in range(len(video_files))]

cols = st.columns(3)

for index, video in enumerate(video_files):
    col_index = index % 3
    # Display the camera title above the video
    cols[col_index].text(camera_titles[index])
    # Display the video with autoplay and looping
    cols[col_index].video(video, loop=True, autoplay=True, muted=False)
