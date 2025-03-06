import streamlit as st

checkout_url = "http://google.com"
st.link_button(
    label="Click to Checkout",
    url=checkout_url,
    help="Click to visit check-out page to complete payment. Checkout will expire in 3 minutes.",
    type="secondary",
    use_container_width=False
)
st.sidebar.link_button(
    label="Click to Checkout",
    url=checkout_url,
    help="Click to visit check-out page to complete payment. Checkout will expire in 3 minutes.",
    type="secondary",
    use_container_width=False
)
