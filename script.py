import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from io import StringIO

# --- App Config ---
st.set_page_config(
    page_title="Data Cleaner Pro",
    page_icon="🧼",
    layout="wide"
)

# --- Sidebar ---
with st.sidebar:
    st.image("https://via.placeholder.com/250x80?text=Data+Cleaner+Pro", use_container_width=True)

    st.markdown("## 📁 Upload CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    st.markdown("## ⚙️ Cleaning Options")
    clean_method = st.radio(
        "Fill missing numeric values using:",
        ["Mean", "Median", "Mode"],
        index=0,
        help="Select how missing numerical values will be filled."
    )

    remove_duplicates = st.checkbox("Remove duplicate rows", value=True)
    show_3d = st.checkbox("Enable 3D Scatter Plot", value=True)

    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; font-size: 14px; color: grey;'>"
        "🔧 <strong>Made by Suyash Mukherjee</strong><br>"
        "Streamlit-based Smart Cleaner"
        "</div>",
        unsafe_allow_html=True
    )

# --- Main App Header ---
st.title("🧹 Data Cleaner & Explorer")
st.caption("Upload your CSV and explore your dataset with interactive cleaning and visualization tools.")

# --- When File is Uploaded ---
if uploaded_file:
    # Read file
    df = pd.read_csv(uploaded_file)
    original_shape = df.shape

    # Step 1: Handle duplicates
    if remove_duplicates:
        df = df.drop_duplicates()
        dropped = original_shape[0] - df.shape[0]
        if dropped > 0:
            st.success(f"✅ Removed {dropped} duplicate rows.")

    # Step 2: Overview
    st.subheader("🔍 Dataset Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Size (MB)", round(df.memory_usage(deep=True).sum() / 1e6, 2))
    st.dataframe(df.head(), use_container_width=True)

    # Step 3: Column Types
    st.subheader("📂 Column Type Breakdown")
    st.write(df.dtypes.value_counts())

    # Step 4: Missing Values
    st.subheader("🚨 Missing Values")
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        st.success("🎉 No missing values found.")
    else:
        st.warning("Missing values detected:")
        st.dataframe(missing)

        if st.button("🔧 Clean Missing Values"):
            for col in missing.index:
                if pd.api.types.is_numeric_dtype(df[col]):
                    if clean_method == "Mean":
                        df[col].fillna(df[col].mean(), inplace=True)
                    elif clean_method == "Median":
                        df[col].fillna(df[col].median(), inplace=True)
                    elif clean_method == "Mode":
                        df[col].fillna(df[col].mode()[0], inplace=True)

            st.success(f"✅ Missing numeric values filled using **{clean_method}**.")

            # ✅ Snippet after modification
            st.markdown("#### 🧽 Transformed Dataset")
            st.dataframe(df.head(), use_container_width=True)

    # Step 5: 3D Visualization
    if show_3d:
        st.subheader("📈 3D Visualization")
        numeric_cols = df.select_dtypes(include="number").columns.tolist()

        if len(numeric_cols) >= 3:
            st.markdown("Select three numeric columns for interactive 3D scatter plot:")

            x_axis = st.selectbox("X-axis", numeric_cols, index=0)
            y_axis = st.selectbox("Y-axis", numeric_cols, index=1)
            z_axis = st.selectbox("Z-axis", numeric_cols, index=2)
            color_col = st.selectbox("Color by (optional)", [None] + df.columns.tolist())

            fig = px.scatter_3d(
                df,
                x=x_axis,
                y=y_axis,
                z=z_axis,
                color=color_col if color_col else None,
                opacity=0.7,
                title="3D Scatter Plot"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Not enough numeric columns for 3D plot.")

    # Step 6: Download Cleaned Data
    st.subheader("⬇️ Download Cleaned CSV")

    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(df)

    st.download_button(
        label="📥 Download Cleaned CSV",
        data=csv,
        file_name=f"cleaned_{uploaded_file.name}",
        mime="text/csv"
    )

# --- Footer Watermark ---
st.markdown(
    "<hr style='margin-top: 40px; margin-bottom: 10px;'>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='text-align: center; color: #888888; font-size: 13px;'>"
    "© 2025 | Built with ❤️ by <strong>Suyash Mukherjee</strong> · All rights reserved."
    "</div>",
    unsafe_allow_html=True
)
