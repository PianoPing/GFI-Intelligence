import streamlit as st

st.title("概覽")
st.caption("用人話說：看見摩擦在哪裡、堵點在哪裡、吞吐量怎麼被蒸發，然後按優先順序修。")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("交付物", "診斷報告", "決策級")
with c2:
    st.metric("交付速度", "48 小時", "收到問卷後")
with c3:
    st.metric("定位", "非政治化", "保密")

st.divider()

left, right = st.columns([1.4, 1])
with left:
    st.subheader("GFI 在量什麼？")
    st.write(
        "GFI 用來量化制度執行的摩擦與延遲：哪裡卡住、哪裡漏掉、哪裡被規則過度束縛，"
        "讓決策者看見吞吐量下降與隱性成本的來源。"
    )

    st.subheader("你會拿到什麼？")
    st.markdown(
        "- 一份「講人話」的診斷敘事\n"
        "- 分數與風險視角：堵點/漏點/高風險段\n"
        "- 依影響力排序的修復建議（先修哪裡最划算）\n"
        "- 可選：輸出 PDF 用於內部簡報"
    )

with right:
    st.subheader("三個原則")
    st.markdown(
        "- **獨立**：不綁廠商\n"
        "- **保密**：資料由你掌控\n"
        "- **非政治化**：只量執行，不吵立場"
    )

st.divider()

st.subheader("合作模式（人話版）")

colA, colB = st.columns([1.2, 1])
with colA:
    st.markdown("### 999 美元 — 完全自助（最低門檻）")
    st.markdown(
        "- 你們自己跑問卷\n"
        "- 把結果提交給我們\n"
        "- **48 小時內**交付 **999 美元診斷報告**\n"
        "- 這一層就是「快速驗證價值」，故意做成輕量"
    )

with colB:
    st.markdown("### 升級（要更深的工作才進來）")
    st.markdown(
        "- 升級不是自動\n"
        "- **先付押金 4,999 美元**，才進入範疇界定與工作會議\n"
        "- 然後依複雜度談時間與報價"
    )

st.info("這套設計是為了避免浪費時間的銷售通話：最低門檻自助，升級先押金。")

st.divider()

st.subheader("下一步")
st.markdown(
    "- 要 999 報告：到 **聯絡** 頁索取問卷/提交方式\n"
    "- 已有問卷結果：提交後 48 小時交付\n"
)

st.caption("聲明：此工具提供流程/治理診斷，不構成法律意見。")
