import streamlit as st

from file_size import format_file_size
from tensorix_client import (
    TensorixError,
    extract_text_from_image,
    mime_from_filename,
)

st.title("Image Text Extraction")
st.caption("Upload an image and extract visible text using Tensorix.")

uploaded = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"],
)

if uploaded is None:
    st.info("Upload an image to get started.")
else:
    size_bytes = len(uploaded.getvalue())
    human = format_file_size(size_bytes)
    st.write(f"**File:** {uploaded.name}")
    st.write(f"**Size:** {size_bytes:,} bytes ({human})")

if st.button("Extract text", type="primary"):
    if uploaded is None:
        st.warning("Upload an image first.")
    else:
        try:
            with st.spinner("Extracting text from image..."):
                text = extract_text_from_image(
                    uploaded.getvalue(),
                    mime_from_filename(uploaded.name),
                )
            st.subheader("Extracted text")
            st.text_area(
                "Extracted text",
                value=text,
                height=300,
                label_visibility="collapsed",
            )
        except TensorixError as exc:
            st.error(str(exc))
