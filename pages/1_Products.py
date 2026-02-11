import streamlit as st

st.set_page_config(layout="wide")

# --- सुंदर दिखने के लिए CSS ---
st.markdown("""
<style>
.product-card {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    text-align: center;
    margin-bottom: 15px;
    border: 1px solid #eee;
}
.product-image {
    width: 100%;
    height: 120px;
    object-fit: contain;
}
.product-name {
    font-size: 16px;
    font-weight: bold;
    margin-top: 10px;
}
.product-price {
    color: #2e7d32;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --- डेटाबेस (सभी सामान यहाँ हैं) ---
# --- डेटाबेस (इंटरनेट फोटो लिंक के साथ) ---
all_products = [
    {
        "name": "बासमती चावल", 
        "cat": "Rice (चावल)", 
        "price": 90, 
        "img": "C:\Users\asus-pc\Documents\Mymart\बासमती चावल.jpg"
    },
    {
        "name": "सरसों तेल", 
        "cat": "Oil (तेल)", 
        "price": 160, 
        "img": "C:\Users\asus-pc\Documents\Mymart\सरसों तेल .jpg"
    },
   {
        "name": "कोलम चावल", 
        "cat": "Oil (तेल)", 
        "price": 160, 
        "img": "C:\Users\asus-pc\Documents\Mymart\कोलम चावल.jpg"
    }, 
    {
        "name": "रिफाइंड तेल", 
        "cat": "Oil (तेल)", 
        "price": 160, 
        "img": "C:\Users\asus-pc\Documents\Mymart\रिफाइंड तेल.jpg"
    },
    {
        "name": "बादाम", 
        "cat": "Oil (तेल)", 
        "price": 160, 
        "img": "C:\Users\asus-pc\Documents\Mymart\बादाम.jpg"
    },
    {
        "name": "काजू प्रीमियम", 
        "cat": "Dry Fruits", 
        "price": 800, 
        "img": "C:\Users\asus-pc\Documents\Mymart\काजू प्रीमियम.jpg"
    }
]

# --- डिस्प्ले वाला हिस्सा (HTML में सुधार) ---
for i, product in enumerate(display_list):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="product-card">
            <img src="{product['img']}" class="product-image">
            <div class="product-name">{product['name']}</div>
            <div class="product-price">₹ {product['price']}</div>
        </div>
        """, unsafe_allow_html=True)

# --- साइडबार (Shop by Category) ---
st.sidebar.title("📁 Shop by Category")
category = st.sidebar.radio(
    "सामान चुनें:",
    ["All Products", "Rice (चावल)", "Oil (तेल)", "Dry Fruits"]
)

st.title(f"🛒 {category}")

# --- कैटेगरी के हिसाब से सामान को फिल्टर करना ---
if category == "All Products":
    display_list = all_products
else:
    display_list = [p for p in all_products if p['cat'] == category]

# --- ग्रिड में दिखाना (3 कॉलम) ---
cols = st.columns(3)

for i, product in enumerate(display_list):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="product-card">
            <img src="https://raw.githubusercontent.com/आपका-नाम/रिपो/main/{product['img']}" class="product-image">
            <div class="product-name">{product['name']}</div>
            <div class="product-price">₹ {product['price']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Add {product['name']}", key=product['name'], use_container_width=True):
            st.success(f"{product['name']} जोड़ा गया!")
