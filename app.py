import os
import streamlit as st
import streamlit.components.v1 as components

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="GFI Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"  # 預設收起 sidebar，避免你看到那個「app / View HTML」
)

# =========================
# CSS (optional, keep clean)
# =========================
st.markdown("""
<style>
/* 讓主畫面貼齊，像正式網站 */
.block-container { padding-top: 0.5rem; padding-bottom: 0rem; max-width: 1200px; }

/* 把 sidebar 的 header 空白縮小 */
section[data-testid="stSidebar"] { padding-top: 0.5rem; }
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD HTML
# =========================
HTML_FILE = "index.html"  # 你要嵌入的檔案

if not os.path.exists(HTML_FILE):
    st.error(f"找不到 {HTML_FILE}。請確認它在 GitHub repo 根目錄（和 app.py 同層）。")
    st.stop()

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html_data = f.read()

# =========================
# RENDER (Homepage = HTML)
# =========================
components.html(html_data, height=1200, scrolling=True)

# =========================
# SIDEBAR (optional branding)
# =========================
with st.sidebar:
    st.markdown("### GFI Intelligence")
    st.caption("Governance Fluency Index (GFI) / Operational Flow Index (OFI)")
    st.caption("© 2026 GFI Intelligence")
