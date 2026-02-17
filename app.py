import streamlit as st

# ✅ Entry point only: set_page_config should be here (not inside individual pages)
st.set_page_config(
    page_title="GFI Flow Intelligence",
    layout="wide",
)

# --- Shared header (international consulting standard) ---
st.markdown(
    """
    <style>
      .gfi-topbar {padding: 0.2rem 0 0.6rem 0; border-bottom: 1px solid rgba(49,51,63,0.2);}
      .gfi-brand {font-size: 1.15rem; font-weight: 700;}
      .gfi-tagline {opacity: 0.75; margin-top: 0.15rem;}
      .gfi-footer {opacity: 0.6; font-size: 0.9rem; padding: 1.2rem 0 0.2rem 0; border-top: 1px solid rgba(49,51,63,0.2);}
    </style>
    <div class="gfi-topbar">
      <div class="gfi-brand">GFI Flow Intelligence</div>
      <div class="gfi-tagline">Independent diagnostic reports · Confidential · Non-political</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ✅ Grouped navigation: EN / 中文 sections in sidebar
pages = {
    "EN": [
        st.Page("pages/en_overview.py", title="Overview", icon="🌐", url_path="en"),
        st.Page("pages/en_methodology.py", title="Methodology", icon="🧭", url_path="en-methodology"),
        st.Page("pages/en_case_studies.py", title="Case Studies", icon="📚", url_path="en-case-studies"),
        st.Page("pages/en_founder.py", title="Founder", icon="👤", url_path="en-founder"),
        st.Page("pages/en_contact.py", title="Contact", icon="✉️", url_path="en-contact"),
    ],
    "中文": [
        st.Page("pages/cn_overview.py", title="概覽", icon="中文", url_path="cn"),
        st.Page("pages/cn_methodology.py", title="方法論", icon="🧭", url_path="cn-methodology"),
        st.Page("pages/cn_case_studies.py", title="案例", icon="📚", url_path="cn-case-studies"),
        st.Page("pages/cn_founder.py", title="創辦人", icon="👤", url_path="cn-founder"),
        st.Page("pages/cn_contact.py", title="聯絡", icon="✉️", url_path="cn-contact"),
    ],
}

pg = st.navigation(pages, position="sidebar")  # native grouped sidebar :contentReference[oaicite:1]{index=1}
pg.run()

# --- Shared footer ---
st.markdown(
    """
    <div class="gfi-footer">
      © 2026 GFI Flow Intelligence · Self-service reports + paid engagement only
    </div>
    """,
    unsafe_allow_html=True,
)
