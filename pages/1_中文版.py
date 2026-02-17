# pages/1_中文版.py
import streamlit as st

st.set_page_config(page_title="GFI｜中文版", layout="wide")

st.title("治理流程診斷（GFI）")
st.subheader("停止制度摩擦｜恢復機構流動")
st.caption("獨立診斷報告（政府與大型機構適用）")

st.divider()

st.markdown("## $999 自助式流程診斷")
st.markdown("""
這是**完全自助產品**。

員工填寫標準化問卷後，  
**48 小時內交付診斷報告。**

**不開會｜不諮詢｜不客製**
""")

st.markdown("### 你會拿到什麼？")
st.markdown("""
- 摩擦集中圖  
- 延遲累積指標  
- 結構過載訊號  
- 風險暴露估算  
""")

st.info("這是**訊號報告**，不是完整審計。")

st.divider()

st.markdown("## 升級合作")
st.markdown("""
若需進一步深度建模與制度分析：

需先支付 **$4,999 押金**，才啟動完整診斷合作。
""")
st.warning("不提供免費策略會議。只與願意真正改善結構的單位合作。")
