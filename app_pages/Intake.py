import streamlit as st

st.set_page_config(page_title="AI Audit Intake", layout="wide")

st.title("AI 实施效益 Intake 表单")

org = st.text_input("组织名称")
contact = st.text_input("联系人")
email = st.text_input("联系邮箱")

st.subheader("AI 实施前")
baseline_time = st.number_input("平均处理时间（天）", min_value=0.0)
baseline_accuracy = st.number_input("完成率（%）", min_value=0.0, max_value=100.0)

st.subheader("AI 实施后")
post_time = st.number_input("平均处理时间（天）-后", min_value=0.0)
post_accuracy = st.number_input("完成率（%）-后", min_value=0.0, max_value=100.0)

if st.button("提交"):
    st.success("表单提交成功！")
