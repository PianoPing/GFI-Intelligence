
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ============================================================================
# Page Configuration
# ============================================================================
st.set_page_config(
    page_title="GFI — Pre/Post Transformation Execution Intelligence™",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🔍"
)

# ============================================================================
# STRIPE Payment Links
# ============================================================================
STRIPE_LINK_999 = "https://buy.stripe.com/8x25kFbp0dM4gQl0fB3VC00"
STRIPE_LINK_4999 = "https://buy.stripe.com/7sYcN764GdM4arX0fB3VC01"

# ============================================================================
# Custom CSS Styles
# ============================================================================
st.markdown("""
<style>
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }

    /* Price Cards */
    .price-card {
        background: white;
        border: 3px solid #3b82f6;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    .price-card-premium {
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
        border: 3px solid #7c3aed;
        color: white;
    }

    .price-tag {
        font-size: 3.5rem;
        font-weight: bold;
        color: #1e40af;
        margin: 1rem 0;
    }

    .price-tag-premium {
        color: white;
    }

    /* CTA Buttons */
    .cta-button {
        background: #10b981;
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        font-size: 1.3rem;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        margin: 1rem 0;
        transition: all 0.3s;
    }

    .cta-button:hover {
        background: #059669;
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(16, 185, 129, 0.3);
    }

    /* Results */
    .big-number {
        font-size: 4rem;
        font-weight: bold;
        color: #dc2626;
        text-align: center;
        margin: 2rem 0;
    }

    .insight-box {
        background: #fef3c7;
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
    }

    /* Guarantee Badge */
    .guarantee-badge {
        background: #dcfce7;
        border: 2px solid #10b981;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# Session State Initialization
# ============================================================================
if 'assessment_complete' not in st.session_state:
    st.session_state.assessment_complete = False
if 'calculated_leak' not in st.session_state:
    st.session_state.calculated_leak = 0
if 'risk_score' not in st.session_state:
    st.session_state.risk_score = 0

# ============================================================================
# Brand Header + Positioning
# ============================================================================
col_logo, col_hero = st.columns([1, 3])

with col_logo:
    st.image("GFILOGO.png", width=200)

with col_hero:
    st.markdown("""
    <div style="padding: 1rem 0;">
        <h1 style="color: #1e40af; margin-bottom: 0.5rem;">GFI: Flow Intelligence</h1>
        <h2 style="margin-top: 0.5rem; font-weight: 500; color: #1e40af; font-size: 1.3rem;">
            Pre-Transformation / Post-Transformation Execution Intelligence Engine
        </h2>
        <p style="font-size: 1.1rem; margin-top: 1rem; color: #475569; line-height: 1.6;">
            <strong>Measure execution capacity before transformation.</strong><br>
            <strong>Prove execution improvement after transformation.</strong>
        </p>
        <p style="font-size: 1rem; margin-top: 1rem; color: #64748b;">
            Free diagnostic → Quantify structural friction in ~12 minutes
        </p>
    </div>
    """, unsafe_allow_html=True)

# Banner Image
st.image("banner.png", use_container_width=True)

# ============================================================================
# GFI Framework Positioning
# ============================================================================
st.markdown("""
<div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
     padding: 2rem; border-radius: 15px; margin: 2rem 0;">
    <h3 style="color: #0c4a6e; text-align: center; margin-bottom: 1.5rem;">
        GFI = The Structural Intelligence Layer for Institutional Transformation
    </h3>
    <p style="color: #075985; text-align: center; font-size: 1.1rem; line-height: 1.6;">
        Most consulting engagements stop at “implementation complete.”<br>
        <strong>GFI quantifies structural execution risk before transformation and verifies structural improvement after transformation.</strong><br>
        Creating a defensible ROI evidence chain.
    </p>
</div>
""", unsafe_allow_html=True)

# Two-Stage Value Proposition
col_pre, col_post = st.columns(2)

with col_pre:
    st.markdown("""
    <div style="background: white; border: 2px solid #3b82f6; border-radius: 12px;
         padding: 1.5rem; height: 100%;">
        <h4 style="color: #1e40af; margin-bottom: 1rem;">
            I. Pre-Transformation
        </h4>
        <p style="color: #475569; font-weight: 600; margin-bottom: 1rem;">
            Purpose: Quantify structural execution risk before launch
        </p>
        <ul style="color: #64748b; line-height: 1.8; margin-left: 1rem;">
            <li>Decision latency density map</li>
            <li>Organizational friction coefficient model</li>
            <li>Baseline capacity leakage estimate</li>
            <li>Execution readiness index</li>
        </ul>
        <p style="background: #dbeafe; padding: 0.75rem; border-radius: 8px;
             margin-top: 1rem; color: #1e40af; font-weight: 600;">
            📊 Deliverable: Board-level “Execution Readiness Brief”
        </p>
        <p style="color: #64748b; margin-top: 1rem; font-style: italic;">
            Build transformation on quantified structure—not assumptions. Reduce capital risk exposure.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_post:
    st.markdown("""
    <div style="background: white; border: 2px solid #10b981; border-radius: 12px;
         padding: 1.5rem; height: 100%;">
        <h4 style="color: #059669; margin-bottom: 1rem;">
            II. Post-Transformation
        </h4>
        <p style="color: #475569; font-weight: 600; margin-bottom: 1rem;">
            Purpose: Quantify whether execution capability truly improved
        </p>
        <ul style="color: #64748b; line-height: 1.8; margin-left: 1rem;">
            <li>Friction reduction magnitude</li>
            <li>Latency compression ratio</li>
            <li>Execution capacity expansion rate</li>
            <li>Organizational resilience index</li>
        </ul>
        <p style="background: #d1fae5; padding: 0.75rem; border-radius: 8px;
             margin-top: 1rem; color: #059669; font-weight: 600;">
            ✅ Deliverable: Transformation Effectiveness Certification
        </p>
        <p style="color: #64748b; margin-top: 1rem; font-style: italic;">
            Prove improvement with data—not slide decks. Quantify real performance lift.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Positioning in the Consulting Ecosystem
st.markdown("""
<div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
     padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #f59e0b;">
    <h4 style="color: #92400e; margin-bottom: 1rem;">
        🎯 Positioning in the Consulting Ecosystem
    </h4>
    <p style="color: #78350f; font-size: 1.05rem; line-height: 1.7;">
        GFI can serve as:<br>
        • <strong>Pre-risk scanning module</strong> — identify execution vulnerabilities before transformation<br>
        • <strong>Post-outcome verification layer</strong> — certify real improvement vs. promised outcomes<br>
        • <strong>Board-level assurance tool</strong> — provide leadership confidence with quantified results
    </p>
    <p style="color: #92400e; margin-top: 1rem; font-weight: 600;">
        Increase project credibility and executive trust—across the full transformation lifecycle.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# Main Content
# ============================================================================
tab1, tab2, tab3 = st.tabs(["🔎 Executive QuickScan", "📑 Deliverable Preview", "💼 Engagement & Pricing"])

# ============================================================================
# Tab 1: Free Assessment
# ============================================================================
with tab1:
    st.header("Executive QuickScan (Free)")
    st.markdown("**Answer 12 questions to estimate annual execution-capacity leakage and friction risk.**")

    with st.form("assessment_form"):
        st.subheader("Organization Profile")

        col1, col2 = st.columns(2)

        with col1:
            company_name = st.text_input("Organization name", placeholder="Example Organization")

            employee_count = st.selectbox(
                "Headcount range",
                ["1–10", "11–50", "51–200", "201–500", "501–1000", "1000+"]
            )

            industry = st.selectbox(
                "Industry",
                ["Tech / SaaS", "Professional Services", "Financial Services",
                 "Healthcare", "Manufacturing", "Retail", "Other"]
            )

            avg_salary = st.number_input(
                "Average annual compensation per employee ($)",
                min_value=30000,
                value=75000,
                step=5000,
                help="A rough average across your organization"
            )

            revenue_per_employee = st.number_input(
                "Annual revenue per employee ($)",
                min_value=50000,
                value=150000,
                step=10000,
                help="Annual revenue / total employees"
            )

            meeting_hours_per_week = st.slider(
                "Meeting hours per employee per week",
                0, 40, 15,
                help="Includes standups, reviews, steering meetings, recurring syncs"
            )

        with col2:
            approval_layers = st.slider(
                "Average approval layers for key decisions",
                1, 10, 3,
                help="How many approvals are required for major decisions?"
            )

            project_delay_pct = st.slider(
                "Project delay rate (%)",
                0, 100, 30,
                help="What percentage of projects typically run late?"
            )

            rework_pct = st.slider(
                "Rework due to misalignment (%)",
                0, 50, 15,
                help="Percent of work that must be redone due to communication/hand-offs"
            )

            decision_time_days = st.slider(
                "Average days for strategic decisions",
                1, 90, 14,
                help="Time from proposal to approval"
            )

            turnover_rate = st.slider(
                "Annual employee turnover rate (%)",
                0, 50, 15,
                help="Percent of employees who leave annually"
            )

            customer_complaint_rate = st.slider(
                "Customer escalation rate (per 100 customers)",
                0, 50, 5,
                help="How many customers escalate issues tied to delay/quality?"
            )

        submitted = st.form_submit_button("🔍 Run Executive QuickScan", use_container_width=True)

        if submitted:
            # ============================================================================
            # Calculation Engine (UNCHANGED)
            # ============================================================================

            emp_count_map = {
                "1–10": 5,
                "11–50": 30,
                "51–200": 125,
                "201–500": 350,
                "501–1000": 750,
                "1000+": 1500
            }
            employees = emp_count_map[employee_count]

            hourly_rate = avg_salary / 2080  # Working hours per year

            # 1) Meeting overhead (assume 40% low-value)
            wasted_meeting_hours = meeting_hours_per_week * 0.4 * 50 * employees
            meeting_cost = wasted_meeting_hours * hourly_rate

            # 2) Delay cost
            delay_factor = project_delay_pct / 100
            avg_project_value = revenue_per_employee * 0.3  # assume 30% revenue project-linked
            delay_cost = delay_factor * avg_project_value * employees * 0.2

            # 3) Rework cost
            rework_factor = rework_pct / 100
            rework_cost = rework_factor * avg_salary * employees * 0.15

            # 4) Decision latency opportunity cost
            decision_delay_weeks = decision_time_days / 7
            decision_opportunity_cost = (decision_delay_weeks - 1) * 500 * employees * 10

            # 5) Turnover cost
            turnover_factor = turnover_rate / 100
            avg_turnover_cost = avg_salary * 1.5  # replacement cost = 150% of salary
            turnover_total_cost = turnover_factor * employees * avg_turnover_cost

            # 6) Customer friction cost
            complaint_factor = customer_complaint_rate / 100
            avg_customer_value = revenue_per_employee * 2
            customer_friction_cost = complaint_factor * employees * avg_customer_value * 0.1

            total_leak = (
                meeting_cost +
                delay_cost +
                rework_cost +
                decision_opportunity_cost +
                turnover_total_cost +
                customer_friction_cost
            )

            # Risk score (0-100)
            risk_factors = [
                (approval_layers - 1) * 10,
                project_delay_pct * 0.5,
                rework_pct * 1.5,
                (decision_time_days / 30) * 20,
                turnover_rate,
                customer_complaint_rate * 1.5
            ]
            risk_score = min(sum(risk_factors) / len(risk_factors), 100)

            st.session_state.assessment_complete = True
            st.session_state.calculated_leak = total_leak
            st.session_state.risk_score = risk_score
            st.session_state.company_name = company_name
            st.session_state.employees = employees

            st.session_state.breakdown = {
                "Meeting overhead": meeting_cost,
                "Project delays": delay_cost,
                "Rework & misalignment": rework_cost,
                "Decision bottlenecks": decision_opportunity_cost,
                "Turnover cost": turnover_total_cost,
                "Customer friction": customer_friction_cost
            }

    # ============================================================================
    # Results Display
    # ============================================================================
    if st.session_state.assessment_complete:
        st.success("✅ QuickScan complete.")

        st.markdown("---")

        st.markdown(f"""
        <div style="text-align: center; background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
             padding: 3rem; border-radius: 15px; margin: 2rem 0;">
            <h3 style="color: #7f1d1d; margin-bottom: 1rem;">
                Estimated Annual Execution-Capacity Leakage — {st.session_state.company_name}
            </h3>
            <div class="big-number">
                ${st.session_state.calculated_leak:,.0f}
            </div>
            <p style="font-size: 1.2rem; color: #991b1b; margin-top: 1rem;">
                Equivalent to <strong>${st.session_state.calculated_leak/st.session_state.employees:,.0f} per employee</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            risk_color = "#dc2626" if st.session_state.risk_score > 70 else "#f59e0b" if st.session_state.risk_score > 40 else "#10b981"

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=st.session_state.risk_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Operational Friction Risk Score"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': risk_color},
                    'steps': [
                        {'range': [0, 40], 'color': "#dcfce7"},
                        {'range': [40, 70], 'color': "#fef3c7"},
                        {'range': [70, 100], 'color': "#fee2e2"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 85
                    }
                }
            ))

            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("### 🎯 Executive Risk Posture")

            if st.session_state.risk_score > 70:
                st.error("**🔴 Elevated Risk** — immediate intervention recommended")
                st.markdown("""
                Your operating model shows multiple high-friction signals:
                - Decision pathways are bottlenecked
                - Delivery reliability is compromised (delays/rework)
                - Turnover pressure suggests systemic strain
                """)
            elif st.session_state.risk_score > 40:
                st.warning("**🟡 Moderate Risk** — meaningful optimization headroom")
                st.markdown("""
                Several friction points are suppressing throughput:
                - Coordination drag and approval layering
                - Preventable delays and rework
                - Clear opportunities for structural simplification
                """)
            else:
                st.success("**🟢 Low Risk** — strong baseline execution health")
                st.markdown("""
                Your organization shows solid execution fundamentals:
                - Efficient decision pathways
                - Lower workflow friction
                - Clear opportunities for incremental performance lift
                """)

        st.markdown("### 💸 Leakage Composition (Where capacity is evaporating)")

        breakdown_df = pd.DataFrame({
            'Category': list(st.session_state.breakdown.keys()),
            'Annual Cost': list(st.session_state.breakdown.values())
        })

        fig = go.Bar(
            x=breakdown_df['Category'],
            y=breakdown_df['Annual Cost'],
            marker=dict(
                color=breakdown_df['Annual Cost'],
                colorscale='Reds'
            )
        )

        fig = go.Figure(data=fig)
        fig.update_layout(
            showlegend=False,
            height=400,
            yaxis_title="Annual Cost ($)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        st.markdown("""
        <div class="insight-box">
            <h3>🎯 This is the signal—not the full diagnosis</h3>
            <p style="font-size: 1.1rem;">
                The Executive QuickScan is designed to surface the <strong>structural magnitude</strong>.
                The actionable value comes from pinpointing:
            </p>
            <ul style="font-size: 1.05rem; margin-top: 1rem;">
                <li>Which teams/functions are driving the leakage</li>
                <li>Your top 3 fixable execution bottlenecks</li>
                <li>The value-at-stake of cutting friction by 30–50%</li>
                <li>How your risk posture compares to peers</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # =====================================================================
        # Upgraded Consulting-Grade Offer Copy (links + pricing unchanged)
        # =====================================================================
        st.markdown("### 💼 Upgrade to a Board-Ready Diagnostic")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="price-card">
                <h3>📑 Professional Diagnostic (Board-Ready PDF)</h3>
                <div class="price-tag">$999</div>
                <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                    <strong>12-page executive diagnostic</strong><br>
                    Designed for CFO/COO, Transformation Leads, and Program Owners
                </p>
                <ul style="text-align: left; font-size: 1rem; line-height: 1.85;">
                    <li>✅ Quantified leakage & friction breakdown (by category)</li>
                    <li>✅ Top 3 execution bottlenecks (fixable, high-impact)</li>
                    <li>✅ Risk exposure narrative (what is failing, where, and why)</li>
                    <li>✅ Peer benchmark signals (context, not vanity metrics)</li>
                    <li>✅ 30-day stabilization plan (quick wins + sequencing)</li>
                    <li>✅ Clear assumptions & methodology summary</li>
                </ul>
                <a href="{}" target="_blank" class="cta-button" style="margin-top: 1.5rem;">
                    Purchase Professional Diagnostic →
                </a>
                <p style="margin-top: 1rem; color: #64748b; font-size: 0.92rem;">
                    Delivery: within 48 hours after intake completion
                </p>
            </div>
            """.format(STRIPE_LINK_999), unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="price-card price-card-premium">
                <div style="background: #fbbf24; color: #7c2d12; padding: 0.5rem;
                     border-radius: 5px; margin-bottom: 1rem; font-weight: bold;">
                    🔥 Most Selected by Leadership Teams
                </div>
                <h3>🧭 Executive Deep-Dive (Diagnostic + Strategy Session)</h3>
                <div class="price-tag price-tag-premium">$4,999</div>
                <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                    <strong>Decision-grade analysis with implementation sequencing</strong><br>
                    Built for executive sponsorship and board-level accountability
                </p>
                <ul style="text-align: left; font-size: 1rem; line-height: 1.85;">
                    <li>✅ Everything in the Professional Diagnostic</li>
                    <li>✅ Custom friction heatmap (where execution breaks down)</li>
                    <li>✅ Team / function-level segmentation (what to fix first)</li>
                    <li>✅ ROI sensitivity model (value of reducing friction)</li>
                    <li>✅ 90-day execution roadmap (sequenced interventions)</li>
                    <li>✅ <strong>2-hour strategy call with the founder</strong></li>
                    <li>✅ 30 days of follow-up support (email)</li>
                </ul>
                <a href="{}" target="_blank" class="cta-button"
                   style="margin-top: 1.5rem; background: white; color: #7c3aed;">
                    Reserve Executive Deep-Dive →
                </a>
                <p style="margin-top: 1rem; font-size: 0.92rem; opacity: 0.92;">
                    Capacity: limited to 5 clients/month
                </p>
            </div>
            """.format(STRIPE_LINK_4999), unsafe_allow_html=True)

        st.markdown("""
        <div class="guarantee-badge">
            <h3>✅ Value Assurance</h3>
            <p style="margin-top: 0.5rem; font-size: 1.05rem; line-height: 1.55;">
                If your diagnostic does not identify at least <strong>5×</strong> the report cost in recoverable
                execution capacity, we will issue a full refund—no questions asked.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# Tab 2: Deliverable Preview
# ============================================================================
with tab2:
    st.header("📑 Deliverable Preview (Sample Structure)")

    st.info("**Note:** This is a simplified preview. Your actual deliverable is customized to your inputs.")

    with st.expander("📄 Page 1: Executive Summary", expanded=True):
        st.markdown("""
        ---
        **GFI Executive Diagnostic — Board-Ready Brief™**  
        *Prepared for: [Organization Name]*  
        *Date: [Report Date]*  
        *Analyst: Ping Xu, creator of the GFI framework*
        ---

        ### Executive Summary

        Our analysis indicates that **[Organization Name]** is experiencing an estimated **$[X]** in annual execution-capacity leakage,
        driven by structural operational friction.

        **Key findings:**

        🔴 **Primary leakage driver:** [Largest cost category]  
        💰 **Estimated annual value-at-stake:** $[X]  
        ⚠️ **Risk score:** [X]/100 — [Risk level]  
        📈 **Near-term recovery potential:** $[X] (first 90 days)

        **Core insight:**  
        Unlike visible costs (payroll, overhead), these losses are embedded in operating structure.
        They accumulate quietly and erode margin, delivery reliability, and transformation ROI.

        This diagnostic provides a prioritized roadmap to recover execution capacity.
        """)

    with st.expander("💸 Pages 2–3: Leakage & Friction Breakdown"):
        st.markdown("""
        ### Estimated annual leakage by category

        | Category | Annual Cost | % of Total | Severity |
        |----------|-------------|------------|----------|
        | Meeting overhead | $[X] | [X]% | 🔴 High |
        | Project delays | $[X] | [X]% | 🟡 Medium |
        | Rework & errors | $[X] | [X]% | 🔴 High |
        | Decision bottlenecks | $[X] | [X]% | 🟡 Medium |
        | Turnover cost | $[X] | [X]% | 🔴 High |
        | Customer friction | $[X] | [X]% | 🟢 Low |

        **Included in the full deliverable:**
        - Root-cause framing (structural)
        - Calculation logic and assumptions
        - Peer-context signals (benchmarks)
        - Actionable interpretation tied to your inputs
        """)

    with st.expander("🎯 Pages 4–5: Top 3 Execution Bottlenecks"):
        st.markdown("""
        ### Bottleneck #1: [Specific issue]

        **Observed pattern:** [Description]  
        **Estimated annual impact:** $[X]  
        **Functions affected:** [Teams/Functions]  
        **Structural root driver:** [Operating model issue]

        **Recommended intervention:**  
        1. [Action]
        2. [Action]
        3. [Action]

        **Expected recovery:** $[X] within [Timeframe]

        ---

        *(Bottlenecks #2 and #3 follow the same structure.)*
        """)

    with st.expander("📊 Pages 6–7: Risk Exposure & Peer Context"):
        st.markdown("""
        ### Risk posture vs. peers

        [Visuals may include:]
        - Your risk score vs. industry median
        - Friction intensity by function/team
        - Trend view (if multiple scans are run over time)

        ### Competitive implications

        In your industry, organizations with comparable friction levels tend to:
        - Deliver transformation outcomes with lower ROI certainty
        - Experience elevated attrition and cycle-time inflation relative to low-friction peers
        """)

    with st.expander("✅ Pages 8–9: Rapid Stabilization Plan (30 Days)"):
        st.markdown("""
        ### Three high-impact, low-burden interventions

        **Action #1: [Intervention]**
        - **What to do:** [Steps]
        - **Time-to-implement:** [X days]
        - **Expected recovery:** $[X]/year
        - **Effort level:** Low / Medium / High

        **Action #2: [Intervention]**  
        *(same format)*

        **Action #3: [Intervention]**  
        *(same format)*

        ### 30-day execution plan

        Week 1: [Actions]  
        Week 2: [Actions]  
        Week 3: [Actions]  
        Week 4: [Actions]
        """)

    with st.expander("🚀 Pages 10–12: Sequencing, Method, and Next Steps"):
        st.markdown("""
        ### Sequenced roadmap

        **Phase 1 (0–30 days):** stabilization  
        **Phase 2 (30–90 days):** structural simplification  
        **Phase 3 (90–180 days):** embedded execution discipline

        ### Methodology

        - Framework overview
        - Data inputs and assumptions
        - Calculation mechanics
        - Interpretation guide and constraints

        ### About the GFI framework

        [Brief positioning note]
        """)

    st.markdown("---")

    st.success("""
    **👆 This preview shows the deliverable structure.** Your actual diagnostic includes:
    - Your organization’s specific numbers
    - Prioritized interventions
    - Industry/context signals
    - A sequenced plan leadership can execute
    """)

# ============================================================================
# Tab 3: Engagement & Pricing
# ============================================================================
with tab3:
    st.header("💼 Engagement Options")
    st.markdown("Transparent pricing. Board-ready deliverables. Minimal time burden.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="price-card">
            <h3>📑 Professional Diagnostic</h3>
            <div class="price-tag">$999</div>
            <p style="font-size: 1.2rem; margin: 1.5rem 0; font-weight: 600;">
                Board-ready PDF deliverable
            </p>
            <hr style="margin: 1.5rem 0;">
            <ul style="text-align: left; font-size: 1.05rem; line-height: 2;">
                <li>✅ 12-page PDF diagnostic</li>
                <li>✅ Leakage & friction breakdown</li>
                <li>✅ Top 3 execution bottlenecks</li>
                <li>✅ Risk exposure score</li>
                <li>✅ Peer context signals</li>
                <li>✅ Rapid stabilization recommendations</li>
                <li>✅ 30-day action plan</li>
                <li>✅ Delivery within 48 hours</li>
            </ul>
            <a href="{}" target="_blank" class="cta-button" style="margin-top: 2rem;">
                Purchase Professional Diagnostic →
            </a>
        </div>
        """.format(STRIPE_LINK_999), unsafe_allow_html=True)

        st.info("""
        **Best for:**
        - Mid-sized organizations (50–500 employees)
        - CFO/COO and transformation owners needing decision-grade clarity
        - Teams preparing for execution stabilization prior to major change
        """)

    with col2:
        st.markdown("""
        <div class="price-card price-card-premium">
            <div style="background: #fbbf24; color: #7c2d12; padding: 0.5rem;
                 border-radius: 5px; margin-bottom: 1rem; font-weight: bold;">
                ⭐ Leadership Choice
            </div>
            <h3>🧭 Executive Deep-Dive</h3>
            <div class="price-tag price-tag-premium">$4,999</div>
            <p style="font-size: 1.2rem; margin: 1.5rem 0; font-weight: 600;">
                Diagnostic + strategy session
            </p>
            <hr style="margin: 1.5rem 0; border-color: rgba(255,255,255,0.3);">
            <ul style="text-align: left; font-size: 1.05rem; line-height: 2;">
                <li>✅ Everything in the Professional Diagnostic</li>
                <li>✅ Custom friction heatmap</li>
                <li>✅ Function/team segmentation</li>
                <li>✅ ROI sensitivity model</li>
                <li>✅ 90-day sequencing roadmap</li>
                <li>✅ <strong>2-hour strategy call with the founder</strong></li>
                <li>✅ Personalized execution plan</li>
                <li>✅ 30 days of email support</li>
                <li>✅ Priority delivery (24 hours)</li>
            </ul>
            <a href="{}" target="_blank" class="cta-button"
               style="margin-top: 2rem; background: white; color: #7c3aed;">
                Reserve Executive Deep-Dive →
            </a>
            <p style="margin-top: 1rem; font-size: 0.95rem; opacity: 0.95;">
                ⚠️ Limited to 5 clients/month
            </p>
        </div>
        """.format(STRIPE_LINK_4999), unsafe_allow_html=True)

        st.info("""
        **Best for:**
        - Leadership teams driving transformation
        - Organizations above $10M revenue
        - Situations where sequencing and risk containment matter
        """)

    st.markdown("---")

    st.markdown("### ❓ FAQ (Scope, Method, and Delivery)")

    with st.expander("How does this compare to a consulting engagement?"):
        st.markdown("""
        **Traditional consulting:**
        - $50K–$200K+ fees
        - 3–6 month project cycles
        - Significant internal time investment
        - Broad frameworks and workshops

        **GFI Executive Diagnostic:**
        - Fixed, transparent pricing
        - Delivered in 24–48 hours
        - Minimal time burden (12-minute QuickScan)
        - Purpose-built for execution friction and leakage
        - Actionable from day one
        """)

    with st.expander("What methodology powers this diagnostic?"):
        st.markdown("""
        This diagnostic is powered by the **GFI (Governance Flow Intelligence)** framework developed by Ping Xu,
        grounded in organizational economics and system dynamics.

        Key inputs:
        - Your QuickScan responses
        - Peer context signals (benchmarks)
        - Revenue/cost multipliers
        - Friction intensity modeling

        The deliverable includes assumptions and calculation logic in plain language.
        """)

    with st.expander("What if I don’t find meaningful leakage?"):
        st.markdown("""
        **Value Assurance**

        If your diagnostic does not identify at least **5× the report cost** in recoverable execution capacity,
        we will issue a full refund—no questions asked.

        Organizations typically uncover 10–50× the diagnostic cost in preventable leakage once it is made visible.
        """)

    with st.expander("How soon will I see results?"):
        st.markdown("""
        **Timeline:**
        - **Immediately:** visibility into leakage magnitude and risk posture
        - **Week 1:** rapid stabilization actions begin
        - **30 days:** first measurable improvements
        - **90 days:** full impact of sequenced structural changes

        Many clients recover the diagnostic cost within the first month through quick wins alone.
        """)

    with st.expander("Do you offer payment plans?"):
        st.markdown("""
        We currently accept one-time payments via Stripe.

        For the **Executive Deep-Dive**, payment arrangements can be discussed on a case-by-case basis after purchase.
        """)

    st.markdown("""
    <div class="guarantee-badge" style="margin-top: 3rem;">
        <h3>✅ Value Assurance</h3>
        <p style="font-size: 1.1rem; margin-top: 1rem; line-height: 1.6;">
            If you do not identify at least <strong>5×</strong> the diagnostic cost in actionable, recoverable execution capacity,
            we will issue a full refund—no questions asked.
        </p>
        <p style="margin-top: 1rem; font-size: 0.95rem; color: #064e3b;">
            ✅ Low burden. High clarity. Decision-grade output.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# Footer
# ============================================================================
st.markdown("---")

footer_col1, footer_col2 = st.columns([1, 3])

with footer_col1:
    st.image("GFILOGO.png", width=120)

with footer_col2:
    st.markdown("""
    <div style="padding-top: 1rem;">
        <p style="font-size: 1.1rem; font-weight: 600; color: #1e40af;">
            GFI: Flow Intelligence
        </p>
        <p style="color: #64748b; margin-top: 0.5rem;">
            Powered by the GFI framework
        </p>
        <p style="margin-top: 0.5rem; color: #64748b;">
            Creator: Ping Xu | Boston, Massachusetts
        </p>
        <p style="font-size: 0.9rem; margin-top: 1rem; color: #94a3b8;">
            © 2026 All rights reserved | <a href="mailto:support@gfi.com" style="color: #3b82f6;">Contact support</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
