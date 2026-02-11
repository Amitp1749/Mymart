import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.product-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    text-align: center;
    margin-bottom: 20px;
}

.product-name {
    font-size: 20px;
    font-weight: bold;
}

.product-price {
    font-size: 18px;
    color: green;
    margin: 10px 0;
}

.custom-button {
    background-color: #ff4b4b;
    color: white;
    padding: 8px 15px;
    border-radius: 8px;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

st.title("🛒 Premium Product Store")

products = [
    {"name": "बासमती चावल", "price": 90},
    {"name": "अरहर दाल", "price": 140},
    {"name": "आशीर्वाद आटा", "price": 220},
    {"name": "रिफाइंड तेल", "price": 110},
]

cols = st.columns(2)

for i, product in enumerate(products):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="product-card">
            <div class="product-name">{product['name']}</div>
            <div class="product-price">₹ {product['price']}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🛒 Add to Cart", key=product["name"]):
            st.success(f"{product['name']} added to cart")
