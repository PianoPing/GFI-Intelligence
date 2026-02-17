# app.py
# GFI Flow Intelligence — International Consulting Standard Structure
# Clean Navigation · Bilingual · No Auto pages/ Conflict · Production-Ready Layout

import streamlit as st

# -------------------------------------------------
# GLOBAL CONFIG
# -------------------------------------------------

APP_TITLE = "GFI Flow Intelligence"
TAGLINE = "Independent Diagnostic Reports · Confidential · Non-Political"

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🛡️",
    layout="wide"
)

# -------------------------------------------------
# GLOBAL STYLE (Consulting-grade minimalism)
# -------------------------------------------------

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

h1 { font-size: 32px; font-weight: 800; letter-spacing: -0.02em; }
h2 { font-size: 22px; font-weight: 700; margin-top: 1.2rem; }
h3 { font-size: 18px; font-weight: 600; }

.gfi-banner {
    padding: 18px 22px;
    border: 1px solid rgba(49,51,63,0.12);
    border-radius: 18px;
    background: linear-gradient(180deg, rgba(49,51,63,0.05), rgba(49,51,63,0.01));
    margin-bottom: 24px;
}

.gfi-banner-title {
    font-size: 28px;
    font-weight: 800;
}

.gfi-banner-sub {
    font-size: 14px;
    color: rgba(49,51,63,0.75);
    margin-top: 6px;
}

.gfi-footer {
    margin-top: 40px;
    padding-top: 18px;
    border-top: 1px solid rgba(49,51,63,0.12);
    font-size: 13px;
    color: rgba(49,51,63,0.65);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown(f"""
<div class="gfi-banner">
  <div class="gfi-banner-title">{APP_TITLE}</div>
  <div class="gfi-banner-sub">{TAGLINE}</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# NAVIGATION STRUCTURE
# IMPORTANT: NO pages/ FOLDER — USE app_pages/
# -------------------------------------------------

NAV_STRUCTURE = {
    "EN": [
        st.Page("app_pages/en_overview.py", title="Overview", icon="🇺🇸"),
        st.Page("app_pages/en_methodology.py", title="Methodology", icon="📊"),
        st.Page("app_pages/en_case_studies.py", title="Case Studies", icon="🗂️"),
        st.Page("app_pages/en_founder.py", title="Founder", icon="👤"),
        st.Page("app_pages/en_contact.py", title="Contact", icon="✉️"),
    ],
    "中文": [
        st.Page("app_pages/cn_overview.py", title="概覽", icon="🇨🇳"),
        st.Page("app_pages/cn_methodology.py", title="方法論", icon="📊"),
        st.Page("app_pages/cn_case_studies.py", title="案例研究", icon="🗂️"),
        st.Page("app_pages/cn_founder.py", title="創辦人", icon="👤"),
        st.Page("app_pages/cn_contact.py", title="聯絡", icon="✉️"),
    ],
}

pg = st.navigation(NAV_STRUCTURE)
pg.run()

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.markdown("""
<div class="gfi-footer">
© GFI Flow Intelligence · Execution Diagnostics · Governance Flow Index (GFI)
</div>
""", unsafe_allow_html=True)
