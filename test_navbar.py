import streamlit as st
import av
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase # Import VideoTransformerBase if you use it
# --- Page Functions ---
def home_page():
    st.title("🏡 Welcome to AsanaSense!")
    st.write(
        """
        This is the main page of your future Yoga Pose Recognition app.
        Use the navigation bar above to explore different sections.
        """
    )
    st.image("https://via.placeholder.com/700x250?text=Your+App+Banner+Here", use_column_width=True)
    st.info("You're currently testing the new top navigation bar feature in Streamlit 1.47!")

def webcam_test_page():
    st.title("🎥 Webcam Test Area")
    st.write(
        """
        This page will eventually house your live webcam feed for pose detection.
        For now, imagine your 'AsanaSense' magic happening here!
        """
    )

    class VideoProcessor(VideoTransformerBase):
        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            image = frame.to_ndarray(format="bgr24")
            flipped_image = cv2.flip(image, 1)  # Flip the image horizontally
            return av.VideoFrame.from_ndarray(flipped_image, format="bgr24")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2: # Place the webcam streamer inside the middle column
        st.write("Your Live Webcam Feed:") # Optional label
        webrtc_streamer(
            key="resizable-demo",
            video_processor_factory=VideoProcessor,
            media_stream_constraints={
                "video": {
                    "width": {"ideal": 640}, # This is the resolution for processing
                    "height": {"ideal": 480}
                },
                "audio": False
            },
            async_processing=True
        )

def about_page():
    st.title("ℹ️ About AsanaSense")
    st.write(
        """
        ### Project Goal
        Our aim is to create an interactive web application that uses AI to analyze
        and provide feedback on yoga poses in real-time.

        ### Technologies Used (or planned!)
        * **Streamlit 1.47:** For the interactive web interface and deployment.
        * **MediaPipe:** For robust pose estimation.
        * **OpenCV:** For video processing.
        * **Python 3.10:** The core language.

        Stay tuned for more updates!
        """
    )
    st.markdown("---")
    st.write("Developed by a B.E. student in their last year, passionate about Data Science, Web Development, Cloud Computing, and AI.")


# --- Navigation Configuration ---
st.set_page_config(layout="wide", page_title="AsanaSense Preview")

pg = st.navigation(
    [
        st.Page(home_page, title="Home", icon="🏠"),
        st.Page(webcam_test_page, title="Webcam Test", icon="📹"),
        st.Page(about_page, title="About", icon="💡"),
    ],
    position="top",  # This is the magic line for the top navbar!
    # Optional: Add a logo
    # logo="https://your-logo-url.png",
    # icon_image="https://your-favicon-url.png" # App icon in browser tab
)

# --- Run the selected page ---
pg.run()