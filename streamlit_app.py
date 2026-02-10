import streamlit as st

st.set_page_config(page_title="मेरा सुपर मार्ट", layout="wide")

# ----- Images -----
images = ["slide1.jpg", "slide2.jpg", "slide3.jpg", "slide4.jpg"]

if "img_index" not in st.session_state:
    st.session_state.img_index = 0

# ----- Center Title -----
st.markdown(
    """
    <h1 style='text-align: center;'>🛒 मेरा सुपर मार्ट</h1>
    <h3 style='text-align: center;'>किफायती दाम, बेहतरीन सामान!</h3>
    """,
    unsafe_allow_html=True
)

# ----- Image Display -----
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(images[st.session_state.img_index], width=800)
st.markdown("</div>", unsafe_allow_html=True)

# ----- Next / Previous Buttons -----
col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅️ Previous"):
        st.session_state.img_index = (st.session_state.img_index - 1) % len(images)

with col3:
    if st.button("Next ➡️"):
        st.session_state.img_index = (st.session_state.img_index + 1) % len(images)

# ----- Offers -----
st.header("🔥 आज के धमाकेदार ऑफर्स")
col1, col2 = st.columns(2)

with col1:
    st.info("📦 **Combo Offer:** 5 किलो चावल पर 1 किलो चीनी फ्री!")
with col2:
    st.success("💰 **Cashback:** ₹1000 की शॉपिंग पर ₹100 की छूट।")

st.write("बाएं तरफ (Sidebar) से 'Products' पर जाकर सामानों की लिस्ट देखें।")

