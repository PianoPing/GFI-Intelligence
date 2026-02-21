import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ============================================================================
# 页面配置
# ============================================================================
st.set_page_config(
    page_title="GFI 隐藏利润流失报告™",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🔍"
)

# ============================================================================
# STRIPE 支付链接
# ============================================================================
STRIPE_LINK_999 = "https://buy.stripe.com/8x25kFbp0dM4gQl0fB3VC00"
STRIPE_LINK_4999 = "https://buy.stripe.com/7sYcN764GdM4arX0fB3VC01"

# ============================================================================
# 自定义 CSS 样式
# ============================================================================
st.markdown("""
<style>
    /* 主标题区域 */
    .hero-section {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* 价格卡片 */
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
    
    /* CTA 按钮 */
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
    
    /* 结果展示 */
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
    
    /* 保证徽章 */
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
# 会话状态初始化
# ============================================================================
if 'assessment_complete' not in st.session_state:
    st.session_state.assessment_complete = False
if 'calculated_leak' not in st.session_state:
    st.session_state.calculated_leak = 0
if 'risk_score' not in st.session_state:
    st.session_state.risk_score = 0

# ============================================================================
# 品牌标题区域与新定位
# ============================================================================
col_logo, col_hero = st.columns([1, 3])

with col_logo:
    st.image("GFILOGO.png", width=200)

with col_hero:
    st.markdown("""
    <div style="padding: 1rem 0;">
        <h1 style="color: #1e40af; margin-bottom: 0.5rem;">GFI: 流程智能</h1>
        <h2 style="margin-top: 0.5rem; font-weight: 500; color: #1e40af; font-size: 1.3rem;">
            转型前 / 转型后执行智能量化引擎
        </h2>
        <p style="font-size: 1.1rem; margin-top: 1rem; color: #475569; line-height: 1.6;">
            <strong>转型前量化执行能力。</strong><br>
            <strong>转型后证明执行提升。</strong>
        </p>
        <p style="font-size: 1rem; margin-top: 1rem; color: #64748b;">
            免费诊断工具 → 12 分钟量化结构性摩擦
        </p>
    </div>
    """, unsafe_allow_html=True)

# 横幅图片
st.image("banner.png", use_container_width=True)

# ============================================================================
# GFI 框架定位部分
# ============================================================================
st.markdown("""
<div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); 
     padding: 2rem; border-radius: 15px; margin: 2rem 0;">
    <h3 style="color: #0c4a6e; text-align: center; margin-bottom: 1.5rem;">
        GFI = 组织转型的结构智能层
    </h3>
    <p style="color: #075985; text-align: center; font-size: 1.1rem; line-height: 1.6;">
        多数顾问专案只做到「实施完成」。<br>
        <strong>GFI 提供转型前结构风险量化与转型后结构改善验证。</strong><br>
        形成可防御的 ROI 证据链。
    </p>
</div>
""", unsafe_allow_html=True)

# 双阶段价值主张
col_pre, col_post = st.columns(2)

with col_pre:
    st.markdown("""
    <div style="background: white; border: 2px solid #3b82f6; border-radius: 12px; 
         padding: 1.5rem; height: 100%;">
        <h4 style="color: #1e40af; margin-bottom: 1rem;">
            Ⅰ. 转型前阶段
        </h4>
        <p style="color: #475569; font-weight: 600; margin-bottom: 1rem;">
            目的：在转型启动前量化结构性执行风险
        </p>
        <ul style="color: #64748b; line-height: 1.8; margin-left: 1rem;">
            <li>决策延迟密度图</li>
            <li>组织摩擦系数模型</li>
            <li>容量流失基准值</li>
            <li>执行准备度指数</li>
        </ul>
        <p style="background: #dbeafe; padding: 0.75rem; border-radius: 8px; 
             margin-top: 1rem; color: #1e40af; font-weight: 600;">
            📊 输出：董事会级「执行准备度报告」
        </p>
        <p style="color: #64748b; margin-top: 1rem; font-style: italic;">
            让转型建立在结构量化基础上，而非假设。降低资本风险暴露。
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_post:
    st.markdown("""
    <div style="background: white; border: 2px solid #10b981; border-radius: 12px; 
         padding: 1.5rem; height: 100%;">
        <h4 style="color: #059669; margin-bottom: 1rem;">
            Ⅱ. 转型后阶段
        </h4>
        <p style="color: #475569; font-weight: 600; margin-bottom: 1rem;">
            目的：量化转型是否真正提升执行能力
        </p>
        <ul style="color: #64748b; line-height: 1.8; margin-left: 1rem;">
            <li>摩擦下降幅度分析</li>
            <li>延迟压缩比例测量</li>
            <li>执行容量扩张率</li>
            <li>组织韧性指数</li>
        </ul>
        <p style="background: #d1fae5; padding: 0.75rem; border-radius: 8px; 
             margin-top: 1rem; color: #059669; font-weight: 600;">
            ✅ 输出：转型效果认证报告
        </p>
        <p style="color: #64748b; margin-top: 1rem; font-style: italic;">
            用数据证明改善幅度，而不是简报叙事。量化真实绩效提升。
        </p>
    </div>
    """, unsafe_allow_html=True)

# 在顾问体系中的定位
st.markdown("""
<div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); 
     padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #f59e0b;">
    <h4 style="color: #92400e; margin-bottom: 1rem;">
        🎯 在顾问体系中的定位
    </h4>
    <p style="color: #78350f; font-size: 1.05rem; line-height: 1.7;">
        GFI 可作为：<br>
        • <strong>前置风险扫描模组</strong> — 在转型前识别执行脆弱点<br>
        • <strong>后置成效验证层</strong> — 认证实际改善 vs. 承诺成果<br>
        • <strong>董事会级保障工具</strong> — 用量化结果提供高层信心
    </p>
    <p style="color: #92400e; margin-top: 1rem; font-weight: 600;">
        提升专案可信度与高层信任，贯穿整个转型生命周期。
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# 主要内容
# ============================================================================

# 导航标签
tab1, tab2, tab3 = st.tabs(["💰 免费评估", "📊 报告样本", "🎁 定价与套餐"])

# ============================================================================
# 标签 1: 免费评估（潜在客户生成）
# ============================================================================
with tab1:
    st.header("免费利润流失计算器")
    st.markdown("**回答 12 个快速问题，估算您的年度利润流失**")
    
    with st.form("assessment_form"):
        st.subheader("公司概况")
        
        col1, col2 = st.columns(2)
        
        with col1:
            company_name = st.text_input("公司名称", placeholder="示例公司")
            
            employee_count = st.selectbox(
                "员工数量",
                ["1-10人", "11-50人", "51-200人", "201-500人", "501-1000人", "1000人以上"]
            )
            
            industry = st.selectbox(
                "行业",
                ["科技/SaaS", "专业服务", "金融", 
                 "医疗保健", "制造业", "零售", "其他"]
            )
            
            avg_salary = st.number_input(
                "员工平均年薪 ($)",
                min_value=30000,
                value=75000,
                step=5000,
                help="所有员工的大致平均值"
            )
            
            revenue_per_employee = st.number_input(
                "每位员工年收入 ($)",
                min_value=50000,
                value=150000,
                step=10000,
                help="年总收入 / 员工总数"
            )
            
            meeting_hours_per_week = st.slider(
                "每位员工每周会议时长（小时）",
                0, 40, 15,
                help="包括所有计划会议、站会、审查会"
            )
        
        with col2:
            approval_layers = st.slider(
                "关键决策的平均审批层级",
                1, 10, 3,
                help="重要决策需要多少人批准？"
            )
            
            project_delay_pct = st.slider(
                "项目延期率 (%)",
                0, 100, 30,
                help="有多少百分比的项目会延期完成？"
            )
            
            rework_pct = st.slider(
                "因沟通不畅导致的返工 (%)",
                0, 50, 15,
                help="需要重做的工作占总工作量的百分比"
            )
            
            decision_time_days = st.slider(
                "战略决策平均所需天数",
                1, 90, 14,
                help="从提案到批准的时间"
            )
            
            turnover_rate = st.slider(
                "年度员工流失率 (%)",
                0, 50, 15,
                help="每年离职的员工占总员工的百分比"
            )
            
            customer_complaint_rate = st.slider(
                "客户投诉率（每 100 位客户）",
                0, 50, 5,
                help="有多少客户会投诉延迟或质量问题？"
            )
        
        submitted = st.form_submit_button("🔍 计算我的隐藏利润流失", use_container_width=True)
        
        if submitted:
            # ============================================================================
            # 计算引擎
            # ============================================================================
            
            # 员工数量映射
            emp_count_map = {
                "1-10人": 5,
                "11-50人": 30,
                "51-200人": 125,
                "201-500人": 350,
                "501-1000人": 750,
                "1000人以上": 1500
            }
            employees = emp_count_map[employee_count]
            
            # 计算时薪
            hourly_rate = avg_salary / 2080  # 年工作小时数
            
            # 摩擦计算
            # 1. 会议开销（假设 40% 的会议是低价值的）
            wasted_meeting_hours = meeting_hours_per_week * 0.4 * 50 * employees
            meeting_cost = wasted_meeting_hours * hourly_rate
            
            # 2. 延迟成本
            delay_factor = project_delay_pct / 100
            avg_project_value = revenue_per_employee * 0.3  # 假设 30% 的收入与项目相关
            delay_cost = delay_factor * avg_project_value * employees * 0.2
            
            # 3. 返工成本
            rework_factor = rework_pct / 100
            rework_cost = rework_factor * avg_salary * employees * 0.15
            
            # 4. 决策延迟机会成本
            decision_delay_weeks = decision_time_days / 7
            decision_opportunity_cost = (decision_delay_weeks - 1) * 500 * employees * 10
            
            # 5. 流失成本
            turnover_factor = turnover_rate / 100
            avg_turnover_cost = avg_salary * 1.5  # 替换成本 = 工资的 150%
            turnover_total_cost = turnover_factor * employees * avg_turnover_cost
            
            # 6. 客户摩擦
            complaint_factor = customer_complaint_rate / 100
            avg_customer_value = revenue_per_employee * 2
            customer_friction_cost = complaint_factor * employees * avg_customer_value * 0.1
            
            # 总年度流失
            total_leak = (
                meeting_cost + 
                delay_cost + 
                rework_cost + 
                decision_opportunity_cost + 
                turnover_total_cost + 
                customer_friction_cost
            )
            
            # 风险评分 (0-100)
            risk_factors = [
                (approval_layers - 1) * 10,
                project_delay_pct * 0.5,
                rework_pct * 1.5,
                (decision_time_days / 30) * 20,
                turnover_rate,
                customer_complaint_rate * 1.5
            ]
            risk_score = min(sum(risk_factors) / len(risk_factors), 100)
            
            # 存储在会话状态中
            st.session_state.assessment_complete = True
            st.session_state.calculated_leak = total_leak
            st.session_state.risk_score = risk_score
            st.session_state.company_name = company_name
            st.session_state.employees = employees
            
            # 细分用于显示
            st.session_state.breakdown = {
                "会议开销": meeting_cost,
                "项目延迟": delay_cost,
                "返工与沟通不畅": rework_cost,
                "决策瓶颈": decision_opportunity_cost,
                "流失成本": turnover_total_cost,
                "客户摩擦": customer_friction_cost
            }
    
    # ============================================================================
    # 结果展示
    # ============================================================================
    if st.session_state.assessment_complete:
        st.success("✅ 评估完成！")
        
        st.markdown("---")
        
        # 大数字揭示
        st.markdown(f"""
        <div style="text-align: center; background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); 
             padding: 3rem; border-radius: 15px; margin: 2rem 0;">
            <h3 style="color: #7f1d1d; margin-bottom: 1rem;">
                {st.session_state.company_name} 的估算年度利润流失
            </h3>
            <div class="big-number">
                ${st.session_state.calculated_leak:,.0f}
            </div>
            <p style="font-size: 1.2rem; color: #991b1b; margin-top: 1rem;">
                即<strong>每位员工 ${st.session_state.calculated_leak/st.session_state.employees:,.0f}</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 风险评分
        col1, col2 = st.columns(2)
        
        with col1:
            # 风险仪表盘
            risk_color = "#dc2626" if st.session_state.risk_score > 70 else "#f59e0b" if st.session_state.risk_score > 40 else "#10b981"
            
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=st.session_state.risk_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "运营摩擦风险评分"},
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
            st.markdown("### 🎯 您的风险画像")
            
            if st.session_state.risk_score > 70:
                st.error("**🔴 高风险** - 建议立即采取行动")
                st.markdown("""
                您的组织显示出严重运营摩擦的多个迹象：
                - 决策制定中的关键瓶颈
                - 高项目失败/延期率
                - 流失率升高表明系统性问题
                """)
            elif st.session_state.risk_score > 40:
                st.warning("**🟡 中等风险** - 存在优化机会")
                st.markdown("""
                几个摩擦点正在影响绩效：
                - 协调效率低下
                - 流程改进机会
                - 可预防的延迟和返工
                """)
            else:
                st.success("**🟢 低风险** - 运营管理良好")
                st.markdown("""
                您的组织展现出强大的运营健康状况：
                - 高效的决策流程
                - 工作流程中的低摩擦
                - 增量收益的机会
                """)
        
        # 细分图表
        st.markdown("### 💸 您的资金在哪里流失？")
        
        breakdown_df = pd.DataFrame({
            '类别': list(st.session_state.breakdown.keys()),
            '年度成本': list(st.session_state.breakdown.values())
        })
        
        fig = go.Bar(
            x=breakdown_df['类别'],
            y=breakdown_df['年度成本'],
            marker=dict(
                color=breakdown_df['年度成本'],
                colorscale='Reds'
            )
        )
        
        fig = go.Figure(data=fig)
        fig.update_layout(
            showlegend=False,
            height=400,
            yaxis_title="年度成本 ($)"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # 行动号召
        st.markdown("---")
        
        st.markdown("""
        <div class="insight-box">
            <h3>🎯 您刚才看到的只是开始</h3>
            <p style="font-size: 1.1rem;">
                这个免费计算器为您提供了一个<strong>粗略估算</strong>。
                但真正的利润流失隐藏在细节中：
            </p>
            <ul style="font-size: 1.05rem; margin-top: 1rem;">
                <li>哪些具体团队流失最严重？</li>
                <li>您的前 3 个可修复的瓶颈是什么？</li>
                <li>如果减少 50% 的摩擦，价值是多少？</li>
                <li>与行业同行相比，您的表现如何？</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🚀 获取完整报告")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="price-card">
                <h3>📊 专业报告</h3>
                <div class="price-tag">$999</div>
                <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                    <strong>完整的 12 页 PDF 分析</strong>
                </p>
                <ul style="text-align: left; font-size: 1rem; line-height: 1.8;">
                    <li>✅ 详细的利润流失细分</li>
                    <li>✅ 前 3 个运营瓶颈</li>
                    <li>✅ 风险暴露评估</li>
                    <li>✅ 快速改进建议</li>
                    <li>✅ 行业基准对比</li>
                    <li>✅ 30 天行动计划</li>
                </ul>
                <a href="{}" target="_blank" class="cta-button" style="margin-top: 1.5rem;">
                    获取专业报告 →
                </a>
                <p style="margin-top: 1rem; color: #64748b; font-size: 0.9rem;">
                    48 小时内交付
                </p>
            </div>
            """.format(STRIPE_LINK_999), unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="price-card price-card-premium">
                <div style="background: #fbbf24; color: #7c2d12; padding: 0.5rem; 
                     border-radius: 5px; margin-bottom: 1rem; font-weight: bold;">
                    🔥 最受欢迎
                </div>
                <h3>🎯 高管深度分析</h3>
                <div class="price-tag price-tag-premium">$4,999</div>
                <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                    <strong>综合分析 + 战略会议</strong>
                </p>
                <ul style="text-align: left; font-size: 1rem; line-height: 1.8;">
                    <li>✅ 专业报告中的所有内容</li>
                    <li>✅ 自定义摩擦热力图</li>
                    <li>✅ 团队逐一分析</li>
                    <li>✅ 干预措施 ROI 计算器</li>
                    <li>✅ 90 天实施路线图</li>
                    <li>✅ <strong>与创始人进行 2 小时战略电话</strong></li>
                    <li>✅ 30 天邮件支持</li>
                </ul>
                <a href="{}" target="_blank" class="cta-button" style="margin-top: 1.5rem; background: white; color: #7c3aed;">
                    获取高管套餐 →
                </a>
                <p style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.9;">
                    每月限 5 位客户
                </p>
            </div>
            """.format(STRIPE_LINK_4999), unsafe_allow_html=True)
        
        # 保证
        st.markdown("""
        <div class="guarantee-badge">
            <h3>💚 100% 退款保证</h3>
            <p style="margin-top: 0.5rem; font-size: 1.05rem;">
                如果您没有发现至少<strong> 5 倍</strong>于报告成本的隐藏利润流失，
                我们将全额退款。无需任何理由。
            </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# 标签 2: 报告样本
# ============================================================================
with tab2:
    st.header("📊 您将获得什么：报告样本预览")
    
    st.info("**注意：** 这是一个简化的预览。您的实际报告将根据您公司的数据完全定制。")
    
    # 报告预览部分
    with st.expander("📄 第 1 页：执行摘要", expanded=True):
        st.markdown("""
        ---
        **隐藏利润流失报告™**  
        *为以下公司准备：[您的公司名称]*  
        *日期：[报告日期]*  
        *分析师：Ping Xu，GFI 框架创建者*
        
        ---
        
        ### 执行摘要
        
        我们的分析显示，**[公司名称]** 正在经历估计每年 **$[X]** 的利润流失，
        这是由于多个维度的运营摩擦造成的。
        
        **关键发现：**
        
        🔴 **主要流失来源：** [最大成本类别]  
        💰 **总年度影响：** $[X]  
        ⚠️ **风险评分：** [X]/100 - [风险级别]  
        📈 **恢复潜力：** $[X]（前 90 天）
        
        **关键洞察：**  
        与可见成本（工资、开销）不同，这些利润流失隐藏在您的运营结构中。
        它们会悄悄地累积，侵蚀利润和竞争定位。
        
        本报告提供了恢复这些损失利润的路线图。
        """)
    
    with st.expander("💸 第 2-3 页：详细利润流失分析"):
        st.markdown("""
        ### 各类别年度利润流失
        
        | 类别 | 年度成本 | 占总数的 % | 严重程度 |
        |----------|-------------|------------|----------|
        | 会议开销 | $[X] | [X]% | 🔴 高 |
        | 项目延迟 | $[X] | [X]% | 🟡 中 |
        | 返工与错误 | $[X] | [X]% | 🔴 高 |
        | 决策瓶颈 | $[X] | [X]% | 🟡 中 |
        | 流失成本 | $[X] | [X]% | 🔴 高 |
        | 客户摩擦 | $[X] | [X]% | 🟢 低 |
        
        **详细分析：**
        
        每个类别都包含以下细分：
        - 根本原因识别
        - 成本计算方法
        - 行业基准对比
        - 来自您数据的具体示例
        """)
    
    with st.expander("🎯 第 4-5 页：前 3 个运营瓶颈"):
        st.markdown("""
        ### 瓶颈 #1：[具体问题]
        
        **描述：** [正在发生的事情]  
        **年度成本影响：** $[X]  
        **受影响的团队：** [团队]  
        **根本原因：** [结构性问题]
        
        **推荐修复：**  
        1. [具体行动]
        2. [具体行动]
        3. [具体行动]
        
        **预期恢复：** $[X] 在 [时间范围] 内
        
        ---
        
        *（瓶颈 #2 和 #3 遵循相同格式）*
        """)
    
    with st.expander("📊 第 6-7 页：风险暴露与行业基准"):
        st.markdown("""
        ### 您的风险画像 vs. 行业
        
        [显示视觉图表：]
        - 您的风险评分 vs. 行业中位数
        - 按部门划分的摩擦强度
        - 趋势分析（如果多次评估）
        
        ### 竞争定位
        
        在您的行业中，具有类似摩擦水平的公司增长速度比
        低摩擦同行慢 [X]%，并且员工流失率高 [X]%。
        """)
    
    with st.expander("✅ 第 8-9 页：快速改进建议"):
        st.markdown("""
        ### 3 个高影响、低工作量的改进
        
        **快速改进 #1：[行动]**
        - **要做什么：** [具体步骤]
        - **实施时间：** [X 天]
        - **预期节省：** $[X]/年
        - **难度：** 低/中/高
        
        **快速改进 #2：[行动]**  
        *（相同格式）*
        
        **快速改进 #3：[行动]**  
        *（相同格式）*
        
        ### 30 天行动计划
        
        第 1 周：[行动]  
        第 2 周：[行动]  
        第 3 周：[行动]  
        第 4 周：[行动]
        """)
    
    with st.expander("🚀 第 10-12 页：下一步与方法论"):
        st.markdown("""
        ### 实施路线图
        
        **第 1 阶段（0-30 天）：** 快速改进  
        **第 2 阶段（30-90 天）：** 结构性改进  
        **第 3 阶段（90-180 天）：** 文化嵌入
        
        ### 方法论与验证
        
        - 框架概述
        - 数据来源和假设
        - 计算方法
        - 限制和置信区间
        
        ### 关于 GFI 框架
        
        [框架和创建者的简要说明]
        """)
    
    st.markdown("---")
    
    st.success("""
    **👆 此预览显示了结构。** 您的实际报告将包括：
    - 您公司的具体数字
    - 定制建议
    - 行业特定洞察
    - 可操作的下一步
    """)

# ============================================================================
# 标签 3: 定价与套餐
# ============================================================================
with tab3:
    st.header("🎁 选择您的套餐")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="price-card">
            <h3>📊 专业报告</h3>
            <div class="price-tag">$999</div>
            <p style="font-size: 1.2rem; margin: 1.5rem 0; font-weight: 600;">
                完整诊断报告
            </p>
            <hr style="margin: 1.5rem 0;">
            <ul style="text-align: left; font-size: 1.05rem; line-height: 2;">
                <li>✅ 12 页 PDF 报告</li>
                <li>✅ 详细的利润流失分析</li>
                <li>✅ 前 3 个瓶颈识别</li>
                <li>✅ 风险暴露评分</li>
                <li>✅ 行业基准对比</li>
                <li>✅ 快速改进建议</li>
                <li>✅ 30 天行动计划</li>
                <li>✅ 48 小时内交付</li>
            </ul>
            <a href="{}" target="_blank" class="cta-button" style="margin-top: 2rem;">
                立即购买 →
            </a>
        </div>
        """.format(STRIPE_LINK_999), unsafe_allow_html=True)
        
        st.info("""
        **适合：**
        - 中型公司（50-500 名员工）
        - 探索效率改进的团队
        - 寻求决策数据的 CFO/COO
        """)
    
    with col2:
        st.markdown("""
        <div class="price-card price-card-premium">
            <div style="background: #fbbf24; color: #7c2d12; padding: 0.5rem; 
                 border-radius: 5px; margin-bottom: 1rem; font-weight: bold;">
                ⭐ 最佳价值
            </div>
            <h3>🎯 高管深度分析</h3>
            <div class="price-tag price-tag-premium">$4,999</div>
            <p style="font-size: 1.2rem; margin: 1.5rem 0; font-weight: 600;">
                完整分析 + 战略会议
            </p>
            <hr style="margin: 1.5rem 0; border-color: rgba(255,255,255,0.3);">
            <ul style="text-align: left; font-size: 1.05rem; line-height: 2;">
                <li>✅ 专业报告中的所有内容</li>
                <li>✅ 自定义摩擦热力图</li>
                <li>✅ 团队逐一细分</li>
                <li>✅ ROI 计算器工具</li>
                <li>✅ 90 天实施路线图</li>
                <li>✅ <strong>与创始人进行 2 小时战略电话</strong></li>
                <li>✅ 个性化行动计划</li>
                <li>✅ 30 天邮件支持</li>
                <li>✅ 优先交付（24 小时）</li>
            </ul>
            <a href="{}" target="_blank" class="cta-button" 
               style="margin-top: 2rem; background: white; color: #7c3aed;">
                预订您的名额 →
            </a>
            <p style="margin-top: 1rem; font-size: 0.95rem; opacity: 0.95;">
                ⚠️ 每月限 5 位客户
            </p>
        </div>
        """.format(STRIPE_LINK_4999), unsafe_allow_html=True)
        
        st.info("""
        **适合：**
        - 致力于转型的领导团队
        - 收入超过 $1000 万的公司
        - 计划重大运营变革的组织
        """)
    
    st.markdown("---")
    
    # 常见问题部分
    st.markdown("### ❓ 常见问题")
    
    with st.expander("这与典型的咨询服务有何不同？"):
        st.markdown("""
        **传统咨询：**
        - $50K-$200K+ 费用
        - 3-6 个月的项目周期
        - 您的团队需要大量时间投入
        - 通用框架
        
        **隐藏利润流失报告：**
        - 固定、透明的定价
        - 24-48 小时内交付
        - 最少的时间投入（12 分钟评估）
        - 专门针对运营摩擦
        - 从第一天起就可操作
        """)
    
    with st.expander("报告是如何计算的？"):
        st.markdown("""
        报告使用由 Ping Xu 通过对组织经济学和系统动力学的广泛研究
        开发的 **GFI（治理流程智能）框架**。
        
        关键输入：
        - 您的评估回答
        - 行业基准
        - 收入/成本乘数
        - 摩擦强度模型
        
        所有计算都是透明的，并在方法论部分进行了解释。
        """)
    
    with st.expander("如果我没有发现隐藏的利润流失怎么办？"):
        st.markdown("""
        **100% 退款保证**
        
        如果您的报告没有识别出至少**报告成本 5 倍**的潜在节省/恢复，
        我们将全额退款。无需任何理由。
        
        在 3 年的诊断中，我们从未收到退款请求。组织通常会发现
        报告成本的 10-50 倍的隐藏流失。
        """)
    
    with st.expander("我多快能看到结果？"):
        st.markdown("""
        **时间表：**
        - **立即：** 意识到利润流失的规模
        - **第 1 周：** 开始实施快速改进
        - **30 天：** 首次可测量的改进
        - **90 天：** 结构性变革的全面影响
        
        大多数客户报告说，仅通过快速改进就在第一个月内收回了报告成本。
        """)
    
    with st.expander("你们提供分期付款吗？"):
        st.markdown("""
        目前，我们只通过 Stripe 提供一次性付款。
        
        但是，对于**高管深度分析**套餐，我们可以根据具体情况安排付款计划。
        购买专业报告后与我们联系以讨论选项。
        """)
    
    # 保证部分
    st.markdown("""
    <div class="guarantee-badge" style="margin-top: 3rem;">
        <h3>💚 我们对您的承诺</h3>
        <p style="font-size: 1.1rem; margin-top: 1rem; line-height: 1.6;">
            我们非常确信您会发现显著的隐藏利润流失，因此我们提供
            无条件的<strong> 100% 退款保证</strong>。如果您没有发现至少
            <strong>报告成本的 5 倍</strong>的可操作节省，我们将立即退款。
        </p>
        <p style="margin-top: 1rem; font-size: 0.95rem; color: #064e3b;">
            ✅ 无风险。无麻烦。只有结果。
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# 页脚
# ============================================================================
st.markdown("---")

footer_col1, footer_col2 = st.columns([1, 3])

with footer_col1:
    st.image("GFILOGO.png", width=120)

with footer_col2:
    st.markdown("""
    <div style="padding-top: 1rem;">
        <p style="font-size: 1.1rem; font-weight: 600; color: #1e40af;">
            GFI: 流程智能
        </p>
        <p style="color: #64748b; margin-top: 0.5rem;">
            由 GFI 框架驱动
        </p>
        <p style="margin-top: 0.5rem; color: #64748b;">
            创建者：Ping Xu | 波士顿，马萨诸塞州
        </p>
        <p style="font-size: 0.9rem; margin-top: 1rem; color: #94a3b8;">
            © 2026 版权所有 | <a href="mailto:support@gfi.com" style="color: #3b82f6;">联系支持</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
