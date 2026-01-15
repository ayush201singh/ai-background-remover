import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(
    page_title="AI Background Remover - Free Tool",
    page_icon="✂️",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        height: 3em;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✂️ AI Background Remover")
st.markdown("### Remove backgrounds from images in seconds using AI")
st.markdown("Perfect for product photos, profile pictures, and design work")

col1, col2 = st.columns(2)

uploaded_file = st.file_uploader(
    "Upload your image (PNG, JPG, JPEG)", 
    type=['png', 'jpg', 'jpeg'],
    help="Maximum file size: 200MB"
)

if uploaded_file is not None:
    with col1:
        st.subheader("📷 Original")
        input_image = Image.open(uploaded_file)
        st.image(input_image, use_container_width=True)
    
    if st.button("🎨 Remove Background"):
        with st.spinner("✨ AI is working its magic... (this may take 10-30 seconds)"):
            try:
                input_bytes = uploaded_file.getvalue()
                output_bytes = remove(input_bytes)
                output_image = Image.open(io.BytesIO(output_bytes))
                
                with col2:
                    st.subheader("✨ Result")
                    st.image(output_image, use_container_width=True)
                
                buf = io.BytesIO()
                output_image.save(buf, format="PNG")
                byte_im = buf.getvalue()
                
                st.download_button(
                    label="⬇️ Download PNG",
                    data=byte_im,
                    file_name=f"no_bg_{uploaded_file.name.split('.')[0]}.png",
                    mime="image/png"
                )
                
                st.success("✅ Background removed! Download your image above.")
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.error("Please try a different image or check the file size.")

else:
    st.info("👆 Upload an image to get started")

st.markdown("---")
st.markdown("### ✨ Features")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown("**🤖 AI Powered**")
    st.write("State-of-the-art AI removes backgrounds precisely")
with col_b:
    st.markdown("**⚡ Instant**")
    st.write("Get results in seconds, not minutes")
with col_c:
    st.markdown("**🆓 Free to Use**")
    st.write("No signup required")

st.markdown("---")
st.markdown("**Made by Ayush Singh** | [GitHub](https://github.com/ayush201singh)")