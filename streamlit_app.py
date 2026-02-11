import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="मेरा सुपर मार्ट", layout="wide")

# ---------- Image Uniform Function ----------
def make_uniform_image(path, size=(1000, 420)):
    img = Image.open(path).convert("RGBA")
    canvas = Image.new("RGBA", size, (255, 255, 255, 255))

    img.thumbnail((size[0]-40, size[1]-40))

    x = (size[0] - img.width) // 2
    y = (size[1] - img.height) // 2

    canvas.paste(img, (x, y), img)
    return canvas

# ---------- Images ----------
images = ["slide1.jpg", "slide2.jpg", "slide3.jpg", "slide4.jpg"]

# ---------- Title ----------
st.markdown(
    """
    <h1 style='text-align:center;'>🛒 मेरा सुपर मार्ट</h1>
    <h3 style='text-align:center;'>किफायती दाम, बेहतरीन सामान!</h3>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------- Auto Image Slider ----------
placeholder = st.empty()

for img in images:
    uniform_img = make_uniform_image(img)
    placeholder.image(uniform_img, use_container_width=True)
    time.sleep(2)

st.write("")

# ---------- Offers Section ----------
st.header("🔥 आज के धमाकेदार ऑफर्स")

col1, col2 = st.columns(2)

with col1:
    st.success("📦 **Combo Offer:** 5 किलो चावल पर 1 किलो चीनी फ्री!")

with col2:
    st.info("💰 **Cashback:** ₹1000 की शॉपिंग पर ₹100 की छूट।")

st.write("")

# ---------- Features Section ----------
st.header("⭐ हमारी खास सुविधाएँ")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🚚 Free Delivery\n5 KM के अंदर फ्री डिलीवरी")

with c2:
    st.markdown("### 💳 Easy Payment\nUPI / Cash / Card स्वीकार")

with c3:
    st.markdown("### 🕒 Fast Service\n30 मिनट में सामान आपके घर")

st.write("")
st.info("बाएं तरफ (Sidebar) से **Products** पर जाकर सामानों की लिस्ट देखें।")
