import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Drag and drop an image here", type=["jpg", "jpeg", "png"])

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_uploaded_image = img.convert("L")
    st.image(gray_uploaded_image, caption="Grayscale Image", use_column_width=True)


with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_camera_image = img.convert("L")
    st.image(gray_camera_image, caption="Grayscale Image", use_column_width=True)


