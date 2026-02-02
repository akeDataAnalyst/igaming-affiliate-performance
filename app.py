import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(page_title="Growe Affiliate Integrity Dashboard", layout="wide")

st.title("🛡️ iGaming Affiliate Integrity & ROI Tracker")
st.markdown("""
This dashboard identifies **Bonus Hunters** and **Bot Traffic** in real-time to protect marketing margins.
""")

# 1. Load Data
@st.cache_data
def load_data():
    # Using the cleaned data from our previous work
    df = pd.read_csv('cleaned_affiliate_performance.csv')
    df['reg_date'] = pd.to_datetime(df['reg_date'])
    return df

df = load_data()

# 2. Sidebar Filters
st.sidebar.header("Filter Analytics")
selected_country = st.sidebar.multiselect("Select Country", options=df['country'].unique(), default=df['country'].unique())
selected_affiliate = st.sidebar.multiselect("Select Affiliate", options=df['affiliate_name'].unique(), default=df['affiliate_name'].unique())

# Filter data based on selection
filtered_df = df[(df['country'].isin(selected_country)) & (df['affiliate_name'].isin(selected_affiliate))]

# 3. Key Metrics (KPIs)
col1, col2, col3 = st.columns(3)
with col1:
    total_ngr = filtered_df['NGR'].sum()
    st.metric("Total Net Gaming Revenue (NGR)", f"${total_ngr:,.2f}", delta=None)
with col2:
    avg_bonus_ratio = filtered_df['Bonus'].sum() / (filtered_df['Deposit'].sum() + 1)
    st.metric("Avg Bonus-to-Deposit Ratio", f"{avg_bonus_ratio:.2f}", delta="-0.05", delta_color="inverse")
with col3:
    high_risk_count = len(filtered_df[filtered_df['Bonus'] > (filtered_df['Deposit'] * 2)])
    st.metric("High-Risk Players Detected", high_risk_count)

st.divider()

# 4. Visualizations
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Profitability by Affiliate (NGR)")
    fig, ax = plt.subplots()
    aff_summary = filtered_df.groupby('affiliate_name')['NGR'].sum().sort_values()
    colors = ['#ff4b4b' if x < 0 else '#00cc96' for x in aff_summary]
    aff_summary.plot(kind='barh', color=colors, ax=ax)
    st.pyplot(fig)

with col_right:
    st.subheader("Bonus vs. Deposit Risk Map")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=filtered_df, x='Deposit', y='Bonus', hue='affiliate_name', ax=ax2)
    plt.plot([0, filtered_df['Deposit'].max()], [0, filtered_df['Deposit'].max()], 'r--')
    st.pyplot(fig2)

# 5. The "Red Flag" List
st.subheader("High-Risk Affiliate Segments (Bonus Abuse)")
# Grouping to show where bonus ratio is toxic
risk_table = filtered_df.groupby(['affiliate_name', 'country']).agg({
    'Deposit': 'sum',
    'Bonus': 'sum',
    'NGR': 'sum'
}).reset_index()
risk_table['Ratio'] = risk_table['Bonus'] / (risk_table['Deposit'] + 1)

# Display only high risk
st.dataframe(risk_table[risk_table['Ratio'] > 1.0].sort_values(by='Ratio', ascending=False), use_container_width=True)

st.success("Targeting active. Export this list to CRM for bonus capping.")

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 **Author:** Aklilu Abera")
st.sidebar.caption("Data Analyst | iGaming Intelligence")
