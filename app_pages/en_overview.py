import streamlit as st

st.title("Overview")
st.caption("See where capacity evaporates. Fix the bottleneck. Restore institutional flow.")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Deliverable", "Diagnostic Report", "Decision-grade")
with c2:
    st.metric("Turnaround", "48 hours", "post-survey")
with c3:
    st.metric("Mode", "Non-political", "confidential")

st.divider()

left, right = st.columns([1.4, 1])
with left:
    st.subheader("What GFI Measures")
    st.write(
        "GFI measures institutional friction and execution delay—so leaders can see where throughput collapses, "
        "where rules over-constrain, and where time loss turns into hidden cost."
    )

    st.subheader("What You Get")
    st.markdown(
        "- A clear diagnostic narrative (plain English)\n"
        "- A scorecard + risk lens (what is blocking flow)\n"
        "- Prioritized fixes (what to remove, what to open)\n"
        "- Optional: PDF export for internal briefings"
    )

with right:
    st.subheader("Principles")
    st.markdown(
        "- **Independent**: no vendor lock-in\n"
        "- **Confidential**: you control distribution\n"
        "- **Non-political**: we measure execution, not ideology"
    )

st.divider()

st.subheader("Engagement Model (Plain Language)")

colA, colB = st.columns([1.2, 1])
with colA:
    st.markdown("### $999 — Self-Serve (Minimum Entry)")
    st.markdown(
        "- You run the survey on your side\n"
        "- You submit results\n"
        "- **Within 48 hours**, you receive a **$999 diagnostic report**\n"
        "- This tier is intentionally limited: it proves value fast"
    )

with colB:
    st.markdown("### Upgrade (When you want deeper work)")
    st.markdown(
        "- Upgrade is **not automatic**\n"
        "- **Deposit first ($4,999)** to unlock scoping + working sessions\n"
        "- We then define scope, timeline, and pricing based on complexity"
    )

st.info("This is designed to prevent time-wasting sales calls. Minimum entry is self-serve. Upgrades require a deposit.")

st.divider()

st.subheader("Next Step")
st.markdown(
    "- If you want the $999 report, go to **Contact** and request the survey intake.\n"
    "- If you already have survey results, submit them and we deliver in 48 hours.\n"
)

st.caption("Disclaimer: This tool provides operational diagnostics and does not constitute legal advice.")
