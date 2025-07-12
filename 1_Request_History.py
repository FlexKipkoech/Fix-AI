import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json

st.set_page_config(
    page_title="Request History - Fix Kenya",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Document Request History")

# Placeholder for demonstration
# In production, this would connect to your data store
sample_data = [
    {
        "timestamp": datetime.now() - timedelta(hours=2),
        "client": "Safari Tech Solutions",
        "document_type": "Both Documents",
        "status": "Completed",
        "requested_by": "John Doe"
    },
    {
        "timestamp": datetime.now() - timedelta(days=1),
        "client": "EcoGreen Kenya",
        "document_type": "Market Research Only",
        "status": "Completed",
        "requested_by": "Jane Smith"
    },
    {
        "timestamp": datetime.now() - timedelta(days=2),
        "client": "FinTech Innovations",
        "document_type": "Strategy Document Only",
        "status": "Completed",
        "requested_by": "Mike Johnson"
    }
]

# Convert to DataFrame
df = pd.DataFrame(sample_data)

# Add filters
col1, col2, col3 = st.columns(3)

with col1:
    date_filter = st.date_input(
        "Filter by date",
        value=(datetime.now() - timedelta(days=7), datetime.now()),
        format="YYYY-MM-DD"
    )

with col2:
    status_filter = st.selectbox(
        "Filter by status",
        ["All", "Completed", "In Progress", "Failed"]
    )

with col3:
    doc_type_filter = st.selectbox(
        "Filter by document type",
        ["All", "Market Research Only", "Strategy Document Only", "Both Documents"]
    )

# Display statistics
st.markdown("### 📈 Statistics")

col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)

with col_stat1:
    st.metric("Total Requests", len(df))

with col_stat2:
    completed = len(df[df['status'] == 'Completed'])
    st.metric("Completed", completed)

with col_stat3:
    avg_time = "8 mins"  # This would be calculated from actual data
    st.metric("Avg. Generation Time", avg_time)

with col_stat4:
    success_rate = f"{(completed/len(df)*100):.1f}%"
    st.metric("Success Rate", success_rate)

# Display table
st.markdown("### 📋 Recent Requests")

# Format the dataframe for display
df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d %H:%M')

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "timestamp": st.column_config.TextColumn("Time", width="medium"),
        "client": st.column_config.TextColumn("Client", width="large"),
        "document_type": st.column_config.TextColumn("Document Type", width="large"),
        "status": st.column_config.TextColumn("Status", width="small"),
        "requested_by": st.column_config.TextColumn("Requested By", width="medium")
    }
)

# Export functionality
if st.button("📥 Export to CSV"):
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"fix_kenya_requests_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )