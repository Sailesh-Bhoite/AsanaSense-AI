import streamlit as st
import cv2
import numpy as np
from PIL import Image
# --- Page Functions ---
def home_page():
    st.title("🏡 Welcome to AsanaSense!")
    st.write(
        """
        This is the main page of your future Yoga Pose Recognition app.
        Use the navigation bar above to explore different sections.
        """
    )

    st.title("ℹ️ About AsanaSense")
    st.write(
        """
        ### Project Goal
        Our aim is to create an interactive web application that uses AI to analyze
        and provide feedback on yoga poses in real-time.

        ### Technologies Used
        * **Streamlit 1.47:** For the interactive web interface and deployment.
        * **MediaPipe:** For robust pose estimation.
        * **OpenCV:** For video processing.
        * **Python 3.10:** The core language.

        Stay tuned for more updates!
        """
    )
    st.markdown("---")
    st.write("Developed by a B.E. student in their last year, passionate about Data Science, Web Development, Cloud Computing, and AI.")


def webcam_test_page():

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        pil_image = Image.open(uploaded_file)
        image_rgb = np.array(pil_image)
        st.image(image_rgb, caption="Uploaded Image", use_container_width=True)


# --- Navigation Configuration ---
st.set_page_config(layout="wide", page_title="AsanaSense", page_icon="images/logo.png")

pg = st.navigation(
    [
        st.Page(home_page, title="Home", icon="🏠"),
        st.Page(webcam_test_page, title="Identify Yoga Position", icon=":material/self_improvement:"),
    ],
    position="top",  # This is the magic line for the top navbar!
    # Optional: Add a logo
    # logo="logo.png",
    # icon_image="logo.png" # App icon in browser tab
)

# --- Run the selected page ---
pg.run()