import streamlit as st
import cv2
import numpy as np
import imutils
import easyocr
from PIL import Image
import tempfile

st.set_page_config(
    page_title="Automatic Number Plate License Detection",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.header("Image Config")
    source_img = st.file_uploader(
        "Upload an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

st.title("Automatic Number Plate License Detection")
st.caption('Upload an image of a vehicle with a number plate.')
st.caption('Then click the :blue[Detect License Plate] button and check the result.')

col1, col2 = st.columns(2)

with col1:
    if source_img:
        uploaded_image = Image.open(source_img)
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

if st.sidebar.button('Detect License Plate'):
    if source_img:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(source_img.read())

        img = cv2.imread(tfile.name)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
        edged = cv2.Canny(bfilter, 30, 200)

        keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

        location = None
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break

        if location is not None:
            pass

        else:
            st.write("No license plate contour found. Please upload a clearer image.")
    else:
        st.write("Please upload an image to detect the license plate.")
