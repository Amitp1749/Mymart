import streamlit as st

st.set_page_config(page_title="मेरा सुपर मार्ट", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
<style>
.hero-box {
    height: 420px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #ffffff;
    border-radius: 15px;
    border: 1px solid #eee;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    padding: 15px;
}
.hero-box img {
    max-height: 380px;
    max-width: 100%;
    object-fit: contain;
}
.center-text {
    text-align: center;
}
.feature-card {
    padding: 20px;
    border-radius: 12px;
    background: #f9fafb;
    text-align: center;
    border: 1px solid #eee;
}
</style>
""", unsafe_allow_html=True)

# ----- Images -----
images = ["slide1.jpg", "slide2.jpg", "slide3.jpg", "slide4.jpg"]

if "img_index" not in st.session_state:
    st.session_state.img_index = 0

# ----- Title -----
st.markdown("""
<h1 class='center-text'>🛒 मेरा सुपर मार्ट</h1>
<h3 class='center-text'>किफायती दाम, बेहतरीन सामान!</h3>
""", unsafe_allow_html=True)

st.write("")

# ----- Image Frame (Uniform Size + Center) -----
st.markdown("<div class='hero-box'>", unsafe_allow_html=True)
st.image(images[st.session_state.img_index])
st.markdown("</div>", unsafe_allow_html=True)

# ----- Buttons -----
col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅️ Previous"):
        st.session_state.img_index = (st.session_state.img_index - 1) % len(images)

with col3:
    if st.button("Next ➡️"):
        st.session_state.img_index = (st.session_state.img_index + 1) % len(images)

st.write("")

# ----- Offers Section -----
st.header("🔥 आज के धमाकेदार ऑफर्स")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='feature-card'>
        <h4>📦 Combo Offer</h4>
        <p>5 किलो चावल पर 1 किलो चीनी फ्री!</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-card'>
        <h4>💰 Cashback Offer</h4>
        <p>₹1000 की शॉपिंग पर ₹100 की छूट।</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ----- Extra Section to fill homepage -----
st.header("⭐ हमारी खास सुविधाएँ")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='feature-card'>
        🚚 <b>Free Delivery</b><br>
        2 KM के अंदर फ्री डिलीवरी
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='feature-card'>
        💳 <b>Easy Payment</b><br>
        UPI / Cash / Card स्वीकार
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='feature-card'>
        🕒 <b>Fast Service</b><br>
        30 मिनट में सामान आपके घर
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.info("बाएं तरफ (Sidebar) से 'Products' पर जाकर सामानों की लिस्ट देखें।")
