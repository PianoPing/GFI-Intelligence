# app.py — FINAL consultant-grade site (single-file Streamlit)
# Includes: Home / Services / GFI / Case Insights / Publications / Request / Engage / About
# Stripe Buy Button embedded correctly.
# Publications UPDATED with your 3 published books.
# Copy-paste ready.

import os
import re
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="GFI Flow Intelligence",
    page_icon="🛡️",
    layout="wide",
)

# -----------------------------
# BRAND INFO
# -----------------------------
BRAND = "GFI Flow Intelligence"
FOUNDER = "Ping Xu"
CITY = "Boston, MA, USA"
EMAIL = "pingshyu0@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/ping-shyu/"

# Put your PDF in the same folder as app.py to enable download
EXEC_BRIEF_PATH = "executive_brief.pdf"

# Post-payment intake URL (also set Stripe success redirect to this)
INTAKE_URL = "https://yourdomain.com/intake"  # replace when ready

# Stripe Buy Button (your provided button)
STRIPE_BUTTON = """
<script async src="https://js.stripe.com/v3/buy-button.js"></script>
<stripe-buy-button
  buy-button-id="buy_btn_1T1sUvRw9CVw8oC7f8G5G2UR"
  publishable-key="pk_live_51SzplSRw9CVw8oC78qxLy57eZRzWrELB0tBzLJa9FWOkxijGMyDDxrr1si3LdzdOEkoNxY4k5pXwCGAshI5iJ1ul00QnZ6DdJQ">
</stripe-buy-button>
"""

# -----------------------------
# PUBLICATIONS (UPDATED)
# Add links later if you want; page renders fine without them.
# -----------------------------
PUBLICATIONS = [
    {
        "title": "The Physical Formula of Governance Legitimacy: Ending the Era of Administrative Violence",
        "subtitle": "A quantitative framework to diagnose administrative friction and legitimacy loss.",
        "link": ""  # optional: Amazon / landing page
    },
    {
        "title": "A Fluent State: Rethinking Governance Through the Lens of Flow",
        "subtitle": "Reframing execution as measurable flow — not abstract policy intent.",
        "link": ""  # optional
    },
    {
        "title": "The Physics of Governance: GDP measured production. GL will measure legitimacy.",
        "subtitle": "A measurement thesis: operational legitimacy becomes quantifiable at system level.",
        "link": ""  # optional
    },
]

# -----------------------------
# NINE INTERNATIONAL CASES (Consultant-grade summary)
# -----------------------------
CASE_OVERVIEW = [
    {"case": "Finland Education", "area": "Education", "gl": 3.13, "insight": "Trust-based architecture", "rank": "Excellent"},
    {"case": "Rwanda Health Insurance", "area": "Healthcare", "gl": 5.08, "insight": "Constraint-driven design", "rank": "Exceptional"},
    {"case": "Estonia Digital Government", "area": "Digital Services", "gl": 10.54, "insight": "Peak efficiency, fragile under outage stress", "rank": "Outstanding*"},
    {"case": "Singapore Housing", "area": "Public Housing", "gl": 0.020, "insight": "Success trap → complexity accumulation", "rank": "Policy Violence"},
    {"case": "Germany Energy Policy", "area": "Climate Policy", "gl": 0.056, "insight": "Complexity trap → permit friction escalation", "rank": "Policy Violence"},
    {"case": "New Zealand Wellbeing Metrics", "area": "Social Metrics", "gl": 0.013, "insight": "Metric overload → accountability diffusion", "rank": "Policy Violence"},
    {"case": "Brazil Bolsa Família", "area": "Social Protection", "gl": 2.64, "insight": "Scale with elegant simplicity", "rank": "Excellent"},
    {"case": "South Korea Digital Identity", "area": "Identity System", "gl": 4.12, "insight": "Hybrid resilience: digital performance + analog fallback", "rank": "Excellent"},
    {"case": "India Aadhaar", "area": "Biometric ID", "gl": 1.89, "insight": "Billion-scale: good governance under extreme diversity", "rank": "Good"},
]

FEATURED_CASES = [
    {
        "title": "Brazil — Bolsa Família (GL 2.64)",
        "bullets": [
            "High governance quality at massive scale (≈50M beneficiaries).",
            "Low citizen pain duration (Pd) and low cognitive friction (Cf) preserved throughput.",
            "Key pattern: one registry, automated reporting, infrastructure reuse.",
        ],
        "takeaway": "High-quality flow can scale if architecture prevents Pd/Cf explosion."
    },
    {
        "title": "South Korea — Digital Identity (GL 4.12)",
        "bullets": [
            "Digital performance without fragility via analog fallback pathways.",
            "Distributed verification reduces single-point failure risk.",
            "Worst-case continuity protects legitimacy under outages.",
        ],
        "takeaway": "Resilience requires designed redundancy, not just digital purity."
    },
    {
        "title": "India — Aadhaar (GL 1.89)",
        "bullets": [
            "Reasonable governance quality at unprecedented population scale.",
            "Steady-state friction constrained by infrastructure + diversity.",
            "At billion-scale, even 1% failure becomes a mass event.",
        ],
        "takeaway": "At extreme scale, “good enough” architecture can still be transformational."
    },
]

CROSS_CASE_PATTERNS = [
    ("Complexity Trap", "Success → exceptions → layers → Pd/Cf growth → performance collapse (e.g., Singapore, Germany, NZ)."),
    ("Burden Direction", "High-performing systems push burden uphill to institutions with capacity, not down to citizens."),
    ("Infrastructure Reuse", "Reuse beats rebuild: existing networks prevent Cf blow-up and accelerate adoption."),
    ("Resilience vs Peak Efficiency", "Peak GL is not the same as worst-case continuity (Estonia vs Korea pattern)."),
    ("Scale Nonlinearity", "GL does not degrade linearly with scale; architecture determines the slope."),
]

# -----------------------------
# MINIMAL CONSULTANT STYLE
# -----------------------------
st.markdown("""
<style>
.block-container {max-width: 1020px; padding-top: 2rem; padding-bottom: 4rem;}
.hr {border-top: 1px solid rgba(0,0,0,0.10); margin: 28px 0;}
.footer {color: rgba(0,0,0,0.6); font-size: 12px; margin-top: 44px; line-height: 1.55;}
.pill {display:inline-block; padding:6px 10px; border:1px solid rgba(0,0,0,0.14); border-radius:999px; font-size:12px; color:rgba(0,0,0,0.72); margin-right:8px; margin-bottom:8px;}
.card {border: 1px solid rgba(0,0,0,0.10); border-radius: 18px; padding: 16px 16px 12px 16px; background:#fff;}
.smallcaps {font-variant: small-caps; letter-spacing: 0.06em; color: rgba(0,0,0,0.62);}
</style>
""", unsafe_allow_html=True)

def hr():
    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

def pills(*items):
    st.markdown("".join([f"<span class='pill'>{i}</span>" for i in items]), unsafe_allow_html=True)

def footer():
    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
    st.markdown(f"""
<div class="footer">
<b>{BRAND}</b><br/>
AI Workflow Impact Assessment<br/><br/>
{FOUNDER} · {CITY}<br/>
{EMAIL}<br/>
linkedin.com/in/ping-shyu<br/><br/>
Independent advisory. Confidential engagements only.<br/>
© {datetime.now().year} {BRAND}. All rights reserved.
</div>
""", unsafe_allow_html=True)

# -----------------------------
# NAVIGATION
# -----------------------------
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Services", "GFI", "Case Insights", "Publications", "Request Assessment", "Engage", "About"],
    index=0
)
st.sidebar.markdown("---")
st.sidebar.markdown(f"**{FOUNDER}**")
st.sidebar.markdown(CITY)
st.sidebar.markdown(EMAIL)
st.sidebar.markdown(LINKEDIN)

# -----------------------------
# HOME
# -----------------------------
if page == "Home":
    st.markdown(f"<div class='smallcaps'>{BRAND}</div>", unsafe_allow_html=True)
    st.markdown("## AI Workflow Impact Assessment")
    st.markdown("### Measuring Operational Stability After AI Integration")

    st.markdown("""
AI increases output.  
But output is not the same as effective throughput.

We assess:

- Where correction load concentrates  
- Where review latency accumulates  
- Where throughput becomes unstable  
- Where operational drag increases
""".strip())

    pills("Independent", "Confidential", "Engineering-based")

    hr()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card'><b>14-Day Signal Window</b><br/><span class='smallcaps'>Staff-validated workflow signal</span></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><b>7-Day Executive Delivery</b><br/><span class='smallcaps'>After window close</span></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><b>5–7 Page Output</b><br/><span class='smallcaps'>Executive brief + stability profile</span></div>", unsafe_allow_html=True)

    hr()
    st.markdown("### Why this exists")
    st.markdown("""
AI does not eliminate workflow friction.  
It redistributes it — from execution to correction, from labor to oversight.

We measure that redistribution in systems already in operation.
""".strip())

    hr()
    st.markdown("### Executive Brief")
    if os.path.exists(EXEC_BRIEF_PATH):
        with open(EXEC_BRIEF_PATH, "rb") as f:
            st.download_button(
                "Download Executive Brief (PDF)",
                data=f,
                file_name="GFI_Executive_Brief.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    else:
        st.info(f"To enable download, place your PDF next to app.py as **{EXEC_BRIEF_PATH}**.")

    footer()

# -----------------------------
# SERVICES
# -----------------------------
elif page == "Services":
    st.markdown("## Services")
    st.markdown("### AI Workflow Impact Assessment")

    st.markdown("""
AI does not eliminate friction.  
It redistributes it.

We identify:

- Rework density  
- Correction latency concentration  
- Human–AI interface pressure  
- Throughput stability risk
""".strip())

    hr()
    st.markdown("### Deliverables")
    colA, colB = st.columns(2)
    with colA:
        st.markdown("""
- Workflow redistribution map  
- Friction concentration analysis  
- Throughput stability profile
""".strip())
    with colB:
        st.markdown("""
- Executive brief (5–7 pages)  
- Strategic stability assessment  
- Engagement next-step options
""".strip())

    hr()
    st.markdown("### Engagement Structure")
    g1, g2, g3 = st.columns(3)
    with g1:
        st.markdown("<div class='card'><b>Impact Scan</b><br/>Focused assessment to locate correction load and latency concentration.</div>", unsafe_allow_html=True)
    with g2:
        st.markdown("<div class='card'><b>Stability Audit</b><br/>Deep workflow analysis with stability profile and concentration mapping.</div>", unsafe_allow_html=True)
    with g3:
        st.markdown("<div class='card'><b>Enterprise Flow Review</b><br/>Full-system evaluation for organizations scaling AI across operations.</div>", unsafe_allow_html=True)

    footer()

# -----------------------------
# GFI FRAMEWORK
# -----------------------------
elif page == "GFI":
    st.markdown("## Governance Flow Index (GFI)")
    st.markdown("""
An engineering framework for diagnosing operational flow in implemented systems.

GFI is a diagnostic tool — not a prediction product.

It measures current workflow conditions:

- Latency load  
- Friction density  
- Throughput stability  
- Workflow conversion integrity
""".strip())

    hr()
    st.markdown("### Where it applies")
    st.markdown("""
- AI-assisted documentation and review loops  
- Automated intake / triage workflows  
- AI-driven compliance review systems  
- Case/claim processing with exception handling  
- Support automation with escalation congestion
""".strip())

    footer()

# -----------------------------
# CASE INSIGHTS
# -----------------------------
elif page == "Case Insights":
    st.markdown("## Case Insights")
    st.markdown("### Nine International Case Studies (Proof-of-Concept)")

    st.markdown("""
This library demonstrates how GFI-style diagnostics can be applied across diverse policy contexts.

The purpose here is architecture:  
how Pd/Cf complexity accumulates, how Fs holds or breaks, and why throughput collapses.
""".strip())

    hr()
    st.markdown("### Featured Case Studies")
    for fc in FEATURED_CASES:
        st.markdown(f"#### {fc['title']}")
        for b in fc["bullets"]:
            st.markdown(f"- {b}")
        st.markdown(f"**Key takeaway:** {fc['takeaway']}")
        st.markdown("")

    hr()
    st.markdown("### Nine Cases Overview")
    for item in CASE_OVERVIEW:
        st.markdown(
            f"**{item['case']}** · {item['area']} · **GL {item['gl']}** · {item['rank']}  \n"
            f"<span class='smallcaps'>{item['insight']}</span>",
            unsafe_allow_html=True
        )

    hr()
    st.markdown("### Cross-Case Patterns")
    for name, desc in CROSS_CASE_PATTERNS:
        st.markdown(f"**{name}:** {desc}")

    footer()

# -----------------------------
# PUBLICATIONS (UPDATED WITH YOUR 3 BOOKS)
# -----------------------------
elif page == "Publications":
    st.markdown("## Publications")
    st.markdown("### Books and related work")

    st.markdown("""
Published work signals methodological continuity — not a one-off service.

This page is intentionally concise.
""".strip())

    hr()

    for bk in PUBLICATIONS:
        st.markdown(f"#### {bk['title']}")
        if bk.get("subtitle"):
            st.markdown(f"<span class='smallcaps'>{bk['subtitle']}</span>", unsafe_allow_html=True)
        if bk.get("link"):
            st.markdown(bk["link"])
        st.markdown("")

    footer()

# -----------------------------
# REQUEST ASSESSMENT
# -----------------------------
elif page == "Request Assessment":
    st.markdown("## Request Assessment")
    st.markdown("""
Submit a short request. We will respond with scope confirmation and next steps.

Confidential engagement. No data sharing.
""".strip())

    with st.form("assessment_form"):
        org = st.text_input("Organization")
        name = st.text_input("Contact Name")
        role = st.text_input("Role / Title")
        email = st.text_input("Email")
        scope = st.selectbox(
            "AI deployment scope",
            [
                "AI-assisted documentation",
                "Automated intake / triage",
                "AI-driven compliance review",
                "Customer support automation",
                "Claims / case processing",
                "Other",
            ],
        )
        concern = st.multiselect(
            "Primary concern (select up to 2)",
            [
                "Rework / correction load rising",
                "Review latency increasing",
                "Quality / error recurrence",
                "Escalations & exception handling",
                "Throughput instability",
                "Staff overload post-AI",
            ],
            max_selections=2,
        )
        notes = st.text_area("Notes (optional)")
        submit = st.form_submit_button("Submit Request")

        if submit:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email or ""):
                st.error("Invalid email.")
            else:
                st.success("Request submitted.")

    footer()

# -----------------------------
# ENGAGE (STRIPE)
# -----------------------------
elif page == "Engage":
    st.markdown("## Initiate Engagement")
    st.markdown("""
Confidential engagement.  
Independent advisory.
""".strip())

    components.html(STRIPE_BUTTON, height=220)
    st.caption("After payment, set Stripe success redirect to your intake page.")

    hr()
    st.markdown("### Post-payment intake")
    st.markdown(INTAKE_URL)

    footer()

# -----------------------------
# ABOUT
# -----------------------------
elif page == "About":
    st.markdown(f"## {FOUNDER}")
    st.markdown(f"Founder, {BRAND}")
    st.markdown(CITY)

    hr()
    st.markdown("""
Architect of the Governance Flow Index (GFI).  
Specializing in workflow diagnostics for AI-integrated systems.

Independent advisory. Confidential engagements only.  
Not affiliated with any AI vendor.
""".strip())

    hr()
    st.markdown("### Contact")
    st.markdown(f"Email: **{EMAIL}**")
    st.markdown(f"LinkedIn: {LINKEDIN}")

    footer()
