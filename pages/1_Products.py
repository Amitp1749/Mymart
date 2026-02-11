import streamlit as st

st.set_page_config(layout="wide")

# CSS में थोडा सुधार (इमेज स्टाइल जोड़ा गया है)
st.markdown("""
<style>
.product-card {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    text-align: center;
    margin-bottom: 20px;
    border: 1px solid #eee;
}

.product-image {
    width: 100%;
    height: 150px;
    object-fit: contain;
    margin-bottom: 10px;
}

.product-name {
    font-size: 18px;
    font-weight: bold;
    color: #333;
}

.product-price {
    font-size: 16px;
    color: #2e7d32;
    margin: 5px 0;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🛒 मेरा प्रीमियम सुपर मार्ट")

# डेटा में फोटो का नाम भी जोड़ें
products = [
    {"name": "बासमती चावल", "price": 90, "img": "rice.jpg"},
    {"name": "अरहर दाल", "price": 140, "img": "dal.jpg"},
    {"name": "आशीर्वाद आटा", "price": 220, "img": "atta.jpg"},
    {"name": "रिफाइंड तेल", "price": 110, "img": "oil.jpg"},
]

cols = st.columns(2)

for i, product in enumerate(products):
    with cols[i % 2]:
        # कार्ड के अंदर फोटो दिखाने के लिए HTML
        st.markdown(f"""
        <div class="product-card">
            <img src="https://raw.githubusercontent.com/आपका-यूजरनेम/रिपॉजिटरी-नाम/main/{product['img']}" class="product-image">
            <div class="product-name">{product['name']}</div>
            <div class="product-price">₹ {product['price']}</div>
        </div>
        """, unsafe_allow_html=True)

        # बटन को कार्ड के ठीक नीचे रखने के लिए
        if st.button(f"🛒 Add {product['name']}", key=product["name"], use_container_width=True):
            st.success(f"{product['name']} झोली में डाला गया")
