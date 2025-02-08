import streamlit as st
import pandas as pd

# Load dataset (replace with actual file)
df = pd.read_excel(r"C:\Users\nbhat\Downloads\city_scores_all_years (1).xlsx")


# Ensure 'NAME_CITY' is used as the city column
df.rename(columns={"NAME_CITY": "City"}, inplace=True)

# Dropdown to select city
cities = df["City"].unique()
selected_city = st.selectbox("Select a City", cities)

# Filter data for selected city
city_data = df[df["City"] == selected_city]

if not city_data.empty:
    total_score = city_data["Total_Score"].values[0]
    social_score = city_data["Social_Score"].values[0]
    political_score = city_data["Political_Score"].values[0]
    economic_score = city_data["Economic_Score"].values[0]
    environmental_score = city_data["Environmental_Score"].values[0]

    # Display results
    st.title(f"{selected_city}")
    st.metric("Total Score", f"{total_score:.2f}")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🌎 Social", f"{social_score:.2f}")
    col2.metric("🏛️ Political", f"{political_score:.2f}")
    col3.metric("💰 Economic", f"{economic_score:.2f}")
    col4.metric("🌱 Environmental", f"{environmental_score:.2f}")
else:
    st.warning("No data available for this city.")
