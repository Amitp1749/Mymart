import os
import streamlit as st

st.write("Current working dir:", os.getcwd())
st.write("Repo files:", os.listdir())
st.write("Images folder exists?:", os.path.exists("images"))

if os.path.exists("images"):
    st.write("Images inside images/:", os.listdir("images"))

# ---------- Products Database ----------
all_products = [
    {"name": "बासमती चावल", "cat": "Rice (चावल)", "price": 90, "img": "pages/basmati.jpg"},
    {"name": "सरसों तेल", "cat": "Oil (तेल)", "price": 160, "img": "pages/sarson.jpg"},
    {"name": "कोलम चावल", "cat": "Rice (चावल)", "price": 70, "img": "pages/kolam.jpg"},
    {"name": "रिफाइंड तेल", "cat": "Oil (तेल)", "price": 150, "img": "pages/refined.jpg"},
    {"name": "बादाम", "cat": "Dry Fruits", "price": 600, "img": "pages/badam.jpg"},
    {"name": "काजू प्रीमियम", "cat": "Dry Fruits", "price": 800, "img": "pages/kaju.jpg"},
]

# ---------- Sidebar ----------
st.sidebar.title("📁 Shop by Category")
category = st.sidebar.radio(
    "सामान चुनें:",
    ["All Products", "Rice (चावल)", "Oil (तेल)", "Dry Fruits"]
)

st.title(f"🛒 {category}")

# ---------- Filter ----------
if category == "All Products":
    display_list = all_products
else:
    display_list = [p for p in all_products if p['cat'] == category]

# ---------- Grid ----------
cols = st.columns(3)

for i, product in enumerate(display_list):
    with cols[i % 3]:
        st.image(product["img"], use_container_width=True)
        st.markdown(f"**{product['name']}**")
        st.markdown(f"₹ {product['price']}")
        
        if st.button(f"Add {product['name']}", key=product['name'], use_container_width=True):
            st.success(f"{product['name']} जोड़ा गया!")
