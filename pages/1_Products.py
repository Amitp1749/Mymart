import streamlit as st

st.set_page_config(layout="wide")

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
st.markdown("""
<style>
.product-card{
    border:1px solid #eee;
    border-radius:12px;
    padding:12px;
    text-align:center;
    background:white;
    margin-bottom:15px;
}
.image-box{
    height:220px;
    width:100%;
    display:flex;
    align-items:center;
    justify-content:center;
    overflow:hidden;
    margin-bottom:10px;
}
.image-box img{
    height:200px;
    width:100%;
    object-fit:contain;
}
</style>
""", unsafe_allow_html=True)

cols = st.columns(3)

for i, product in enumerate(display_list):
    with cols[i % 3]:

        st.markdown(f"""
        <div class="product-card">
            <div class="image-box">
                <img src="{product['img']}">
            </div>
            <b>{product['name']}</b><br>
            ₹ {product['price']}
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Add {product['name']}", key=product['name'], use_container_width=True):
            st.success(f"{product['name']} जोड़ा गया!")
