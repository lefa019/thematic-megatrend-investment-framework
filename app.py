import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Thematic Megatrend Investment Framework",
    page_icon="📈",
    layout="wide"
)

# Title & Header
st.title("📈 Thematic Megatrend Investment Framework")
st.markdown("**Author:** Richard Baloyi | *Long-Term Capital Allocation & Asset Growth Analysis*")
st.markdown("---")

# ---------------------------------------------------------
# Sidebar Controls
# ---------------------------------------------------------
st.sidebar.header("Investment Simulator")
initial_investment = st.sidebar.number_input(
    "Base Investment Amount (R)",
    min_value=1000,
    max_value=1000000,
    value=10000,
    step=1000
)

multiplier = initial_investment / 10000.0

# ---------------------------------------------------------
# Data Preparation
# ---------------------------------------------------------
perf_data = {
    'Company': ['Facebook (Meta)', 'Nvidia', 'Tesla', 'Amazon', 'Shoprite (Safe)', 'S&P 500 (Benchmark)'],
    'IPO Year': [2012, 1999, 2010, 1997, 1986, 1923],
    '10Y Return (%)': [1200, 38000, 15000, 8500, 180, 280],
    '20Y Return (%)': [17600, 450000, 32000, 12000, 450, 650]
}
df_perf = pd.DataFrame(perf_data)

sentiment_data = {
    'Company': ['Facebook (Meta)', 'Nvidia', 'Tesla', 'Amazon'],
    'IPO Sentiment': ['Highly Skeptical', 'Very Skeptical', 'Moderate', 'Extreme Skepticism'],
    'Day 1 Return (%)': [0.6, -5.0, 10.0, -10.0],
    '10Y Return (%)': [1200, 38000, 15000, 8500]
}
df_sent = pd.DataFrame(sentiment_data)

# ---------------------------------------------------------
# Row 1 Layout
# ---------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Performance Comparison: Megatrends vs Safe Stocks")
    st.dataframe(
        df_perf,
        column_config={
            "10Y Return (%)": st.column_config.NumberColumn(format="%d%%"),
            "20Y Return (%)": st.column_config.NumberColumn(format="%d%%"),
        },
        hide_index=True,
        use_container_width=True
    )

with col2:
    st.subheader("2. Historical Returns (Logarithmic Scale)")
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=df_perf['Company'], y=df_perf['10Y Return (%)'],
        name='10 Year Return %', marker_color='#0047AB'
    ))
    fig1.add_trace(go.Bar(
        x=df_perf['Company'], y=df_perf['20Y Return (%)'],
        name='20 Year Return %', marker_color='#E25822'
    ))
    fig1.update_yaxes(type="log", title_text="Return % (Log Scale)")
    fig1.update_layout(
        height=380, barmode='group',
        margin=dict(l=20, r=20, t=30, b=20),
        legend=dict(orientation="h", y=-0.25)
    )
    st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# Row 2 Layout
# ---------------------------------------------------------
col3, col4 = st.columns(2)

with col3:
    st.subheader("3. IPO Sentiment vs Long-Term Performance")
    st.dataframe(
        df_sent,
        column_config={
            "Day 1 Return (%)": st.column_config.NumberColumn(format="%.1f%%"),
            "10Y Return (%)": st.column_config.NumberColumn(format="%d%%"),
        },
        hide_index=True,
        use_container_width=True
    )

with col4:
    st.subheader("4. Compounding Growth Comparison")
    comp_base = pd.DataFrame({
        'Strategy': ['Megatrend', 'Megatrend', 'Safe Stocks', 'Safe Stocks'],
        'Horizon': ['10 Years', '20 Years', '10 Years', '20 Years'],
        'Value': [850000 * multiplier, 12500000 * multiplier, 48000 * multiplier, 145000 * multiplier]
    })

    fig2 = px.bar(
        comp_base, x='Horizon', y='Value', color='Strategy', barmode='group',
        color_discrete_map={'Megatrend': '#0047AB', 'Safe Stocks': '#E25822'},
        text_auto='.2s'
    )
    fig2.update_yaxes(type="log", title_text="Value in ZAR (Log Scale)")
    fig2.update_layout(
        height=380,
        margin=dict(l=20, r=20, t=30, b=20),
        legend=dict(orientation="h", y=-0.25)
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# Key Insights Executive Summary Card
# ---------------------------------------------------------
st.subheader("💡 Strategic Key Insights")
m_20y = 12500000 * multiplier
s_20y = 145000 * multiplier
ratio = m_20y / s_20y

st.info(
    f"""
    * **Generational Wealth Multiplier:** An initial investment of **R{initial_investment:,.0f}** in Megatrend Leaders yields **R{m_20y:,.0f}** over a 20-year horizon.
    * **Outperformance Margin:** Megatrend strategies generate **{ratio:.1f}x more capital growth** than defensive/safe stock allocations over 20 years.
    * **Market Mispricing:** Early skepticism during IPO phases (e.g., Meta, Nvidia, Amazon) created asymmetric long-term risk-reward entry points for patient capital.
    """
)
