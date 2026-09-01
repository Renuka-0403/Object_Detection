import streamlit as st
from transformers import pipeline
from PIL import Image

st.title("Object-detection")

detector = pipeline("object-detection")

image = st.file_uploader(
    "upload an image",
    type=["jpg", "png", "jpeg"]
)

if image:
    img = Image.open(image)
    st.image(img)

    if st.button("Detect"):
        result = detector(img)
        st.write(result)