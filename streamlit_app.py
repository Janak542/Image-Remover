import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Background Remover", page_icon="✨")

st.title("✨ Background Remover App")
st.write("Upload an image and remove its background instantly!")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg", "webp", "bmp"])

if uploaded_file:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(uploaded_file, use_container_width=True)
    
    image = Image.open(uploaded_file)
    output = remove(image)

    with col2:
        st.subheader("Background Removed")
        st.image(output, use_container_width=True)

    # Download button
    buf = io.BytesIO()
    output.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
        label="Download Transparent PNG",
        data=byte_im,
        file_name="output.png",
        mime="image/png"
    )

st.markdown("---")
st.caption("Built with using Streamlit and Rembg")