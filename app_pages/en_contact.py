import streamlit as st
import textwrap
from datetime import datetime

st.title("Contact / Submit Survey")
st.caption("Submit survey results for the $999 self-serve diagnostic report, or request an upgrade scope (deposit required).")

# -------------------------
# LINKS (edit here)
# -------------------------
GOOGLE_FORM_URL = "https://forms.gle/96rG6e4PTAJgDkcJ9"
EMAIL = "pingshyu0@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/ping-shyu/"

# -------------------------
# Top Contact Block
# -------------------------
c1, c2 = st.columns([1.2, 1])
with c1:
    st.subheader("Direct Contact")
    st.markdown(f"- Email: **{EMAIL}**")
    st.markdown(f"- LinkedIn: **{LINKEDIN}**")

with c2:
    st.subheader("Fastest Path")
    st.markdown(
        "- **Self-Serve ($999):** pay → submit survey → receive report in **48 hours**\n"
        "- **Upgrade:** deposit **$4,999** → scope call → custom engagement"
    )

st.divider()

# -------------------------
# Section 1: Submit via Google Form
# -------------------------
st.subheader("A) Submit Survey (Google Form)")
st.write("Use the form for standardized intake. This is the primary submission channel.")

st.link_button("Open Google Form — Submit Survey", GOOGLE_FORM_URL)

st.caption("Tip: If your organization restricts external forms, use the upload + email option below.")

st.divider()

# -------------------------
# Section 2: Pay $999 via Stripe Buy Button
# -------------------------
st.subheader("B) Pay $999 (Stripe)")
st.write("After payment, submit your survey results using the Google Form above (or upload + email below).")

st.markdown(
    """
<script async src="https://js.stripe.com/v3/buy-button.js"></script>

<stripe-buy-button
  buy-button-id="buy_btn_1T1sUvRw9CVw8oC7f8G5G2UR"
  publishable-key="pk_live_51SzplSRw9CVw8oC78qxLy57eZRzWrELB0tBzLJa9FWOkxijGMyDDxrr1si3LdzdOEkoNxY4k5pXwCGAshI5iJ1ul00QnZ6DdJQ"
>
</stripe-buy-button>
""",
    unsafe_allow_html=True
)

st.divider()

# -------------------------
# Section 3: Upload Strategy (Practical & safe)
# -------------------------
st.subheader("C) Upload Survey Files (Fallback)")
st.write(
    "If you cannot use the Google Form, upload files here as a **temporary fallback**. "
    "For privacy
