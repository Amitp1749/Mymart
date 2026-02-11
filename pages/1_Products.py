import streamlit as st
from PIL import Image, ImageOps   # ✅ ये जरूरी है

st.set_page_config(layout="wide")

# ---------- Image uniform function ----------
def load_uniform_image(path, size=(300, 300)):
    img = Image.open(path).convert("RGB")
    img = ImageOps.contain(img, size)
    background = Image.new("RGB", size, (255, 255, 255))
    offset = ((size[0] - img.size[0]) // 2, (size[1] - img.size[1]) // 2)
    background.paste(img, offset)
    return background

# ---------- Products Database ----------
all_products = [
    {"name": "बासमती चावल", "cat": "Rice (चावल)", "price": 95, "img": "pages/basmati.jpg"},
    {"name": "सरसों तेल", "cat": "Oil (तेल)", "price": 186, "img": "pages/sarson.jpg"},
    {"name": "कोलम चावल", "cat": "Rice (चावल)", "price": 320, "img": "pages/kolam.jpg"},
    {"name": "रिफाइंड तेल", "cat": "Oil (तेल)", "price": 130, "img": "pages/refined.jpg"},
    {"name": "बादाम", "cat": "Dry Fruits", "price": 800/kg, "img": "pages/badam.jpg"},
    {"name": "काजू प्रीमियम", "cat": "Dry Fruits", "price": 1200/kg, "img": "pages/kaju.jpg"},
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

        uniform_img = load_uniform_image(product["img"])

        st.image(uniform_img, use_container_width=True)
        st.markdown(f"**{product['name']}**")
        st.markdown(f"₹ {product['price']}")

        if st.button(f"Add {product['name']}", key=product['name'], use_container_width=True):
            st.success(f"{product['name']} जोड़ा गया!")
