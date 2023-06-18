import streamlit as st
from PIL import Image
import io

# Title and instructions
st.title("Image Gallery")
st.write("Upload and display images")

# Upload images
uploaded_files = st.file_uploader("Upload Images", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

def apply_sepia_filter(image):
    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Apply the sepia filter
    sepia_image = grayscale_image.copy()
    pixels = sepia_image.load()
    width, height = sepia_image.size
    depth = 30  # Adjust the depth of sepia effect

    for i in range(width):
        for j in range(height):
            r, g, b = grayscale_image.getpixel((i, j))
            sepia_r = min(int(r + depth * 2), 255)
            sepia_g = min(int(g + depth), 255)
            sepia_b = min(int(b - depth), 255)
            pixels[i, j] = (sepia_r, sepia_g, sepia_b)

    return sepia_image

# Display uploaded images
if uploaded_files:
    for file in uploaded_files:
        image = Image.open(file)
        st.image(image, caption=file.name, use_column_width=True)

        # Image operations
        if st.checkbox("Resize Image"):
            width = st.number_input("Enter width", value=image.width, min_value=1)
            height = st.number_input("Enter height", value=image.height, min_value=1)
            resized_image = image.resize((width, height))
            st.image(resized_image, caption="Resized Image", use_column_width=True)

        if st.checkbox("Apply Filter"):
            filter_type = st.selectbox("Select Filter", ["None", "Grayscale", "Sepia"])
            if filter_type == "Grayscale":
                grayscale_image = image.convert("L")
                st.image(grayscale_image, caption="Grayscale Image", use_column_width=True)
            elif filter_type == "Sepia":
                sepia_image = apply_sepia_filter(image)
                st.image(sepia_image, caption="Sepia Image", use_column_width=True)

        if st.button("Download"):
            img_bytes = io.BytesIO()
            image.save(img_bytes, format='JPEG')
            st.download_button(label='Download Image', data=img_bytes, file_name=file.name)
        if st.button("Share"):
            # Add functionality for sharing here
            pass