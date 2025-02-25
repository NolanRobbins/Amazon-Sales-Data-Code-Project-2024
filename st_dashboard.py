import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import os 

st.set_page_config(page_title="Amazon Sales Data Project", page_icon=":bar_chart:", layout="wide")

# Function to load data from multiple Excel files (using caching for performance)
@st.cache_data
def load_data(file_paths):
    df_top10_customers   = pd.read_excel(file_paths['top10_customers'])
    df_total_profit_cat  = pd.read_excel(file_paths['total_profit_cat'])
    df_top_cities        = pd.read_excel(file_paths['top_cities'])
    df_bottom_cities     = pd.read_excel(file_paths['bottom_cities'])
    df_rfm               = pd.read_excel(file_paths['rfm'])
    df_prof_cat_top      = pd.read_excel(file_paths['prof_cat_top'])
    df_prof_cat_bottom   = pd.read_excel(file_paths['prof_cat_bottom'])
    return df_top10_customers, df_total_profit_cat, df_top_cities, df_bottom_cities, df_rfm, df_prof_cat_top, df_prof_cat_bottom

# Load your data (update the paths as needed)
file_paths = {
    'top10_customers': os.path.join("data", "Top 10 Customers.xlsx"),
    'total_profit_cat': os.path.join("data", "Total Profit Categories.xlsx"),
    'top_cities': os.path.join("data", "Top 5 Cities.xlsx"),
    'bottom_cities': os.path.join("data", "Bottom 5 Cities.xlsx"),
    'rfm': os.path.join("data", "RFM.xlsx"),
    'prof_cat_top': os.path.join("data", "Prof Cat Top.xlsx"),
    'prof_cat_bottom': os.path.join("data", "Prof Cat Bottom.xlsx")
}

(df_top10_customers, 
 df_total_profit_cat, 
 df_top_cities, 
 df_bottom_cities, 
 df_rfm,
 df_prof_cat_top,
 df_prof_cat_bottom) = load_data(file_paths)

df_top_cities = df_top_cities.drop(columns=['Unnamed: 0']).reset_index(drop=True).round(2)
df_bottom_cities = df_bottom_cities.drop(columns=['Unnamed: 0']).reset_index(drop=True).round(2)
df_top10_customers = df_top10_customers.drop(columns=['Unnamed: 0']).reset_index(drop=True).round(2)

# Dashboard Title
st.title("Amazon Sales Data Business Analytics Dashboard")

# Create tabs for each major analysis section
tab_rfm, tab_profit, tab_cities, tab_customers = st.tabs([
    "RFM Medal Results", 
    "Total Profit by Category", 
    "City Profitability", 
    "Top 10 Profitable Customers"
])

# --- Tab 1: RFM Analysis ---
with tab_rfm:

    def create_medal_distribution(data):
        """
        Create a medal distribution bar chart using Plotly with enhanced typography
        
        Parameters:
        data (pd.Series): Medal value counts from your RFM analysis
        
        Returns:
        fig: Plotly figure object
        """
        # Create color mapping
        color_map = {
            'Gold': '#FFD700',    # Gold color
            'Silver': '#C0C0C0',  # Silver color
            'Bronze': '#CD7F32'   # Bronze color
        }
        
        # Convert series to dataframe for plotly
        df = pd.DataFrame({
            'Medal': data.index,
            'Count': data.values
        })
        
        # Create the bar chart with enhanced text styling
        fig = go.Figure(data=[
            go.Bar(
                x=df['Medal'],
                y=df['Count'],
                marker_color=[color_map.get(x, '#000000') for x in df['Medal']],
                text=df['Count'],
                textposition='auto',
                textfont=dict(
                    size=18,
                    color='black',
                    family='Arial Black'
                ),
            )
        ])
        
        # Update layout with enhanced typography
        fig.update_layout(
            title={
                'text': 'Customer Medal Distribution',
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': {'size': 28, 'family': 'Arial Black'}
            },
            xaxis_title={
                'text': 'Medal Category',
                'font': {'size': 20, 'family': 'Arial Black'}
            },
            yaxis_title={
                'text': 'Number of Customers',
                'font': {'size': 20, 'family': 'Arial Black'}
            },
            plot_bgcolor='white',
            showlegend=False,
            width=800,
            height=500,
            margin=dict(l=50, r=50, t=80, b=50)
        )
        
        # Update axes with bolder fonts
        fig.update_xaxes(
            showgrid=False,
            showline=True,
            linecolor='lightgrey',
            tickfont=dict(
                size=16,
                family='Arial Black'
            )
        )
        
        fig.update_yaxes(
            showgrid=True,
            gridcolor='lightgrey',
            showline=True,
            linecolor='lightgrey',
            tickfont=dict(
                size=16,
                family='Arial Black'
            )
        )
        
        return fig

    # Assuming you have your RFM analysis and medal_counts
    medal_counts = df_rfm['Customer Medals'].value_counts()

    # Create and display the figure
    fig = create_medal_distribution(medal_counts)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("**Insight:** This chart shows the distribution of customers based on their medal categories.")

    st.header("RFM Medal Results")
    st.markdown("This table displays the segmentation of customers based on Recency, Frequency, and Monetary values along with medal assignments for top performers.")
    st.dataframe(df_rfm, use_container_width=True)
    
# --- Tab 2: Total Profit by Category ---
with tab_profit:
    st.header("Total Profit by Category")
    fig_profit = px.bar(
        df_total_profit_cat,
        x="Category", 
        y="Profit", 
        color="Profit",
        title="Profit Contribution by Category",
        template="plotly_white",
        labels={"Profit": "Total Profit", "Category": "Product Category"}
    )
    st.plotly_chart(fig_profit, use_container_width=True)
    st.markdown("**Insight:** This chart highlights which categories drive the highest profit.")

# --- Tab 3: City Profitability ---
with tab_cities:
    st.header("City Profitability Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        # Top Cities Section
        st.subheader("Most Profitable Cities")
        st.dataframe(df_top_cities, use_container_width=True)
        fig_top_cities = px.bar(
            df_top_cities,
            x="Geography",  
            y="Profit",
            title="Top 5 Most Profitable Cities",
            template="plotly_white"
        )
        st.plotly_chart(fig_top_cities, use_container_width=True)

        # Top Cities Category Analysis
        st.title("Top 5 Cities for Profit by Category")
        st.markdown("Select a city and then a category to view the corresponding profit.")

        # Use filtered data for TOP cities only
        top_city_options = df_prof_cat_top['City'].unique()  # Should contain only top 5 cities
        selected_top_city = st.selectbox("Choose a Top City", options=top_city_options, key="top_city")
        
        # Filter data for selected top city
        top_city_data = df_prof_cat_top[df_prof_cat_top['City'] == selected_top_city]
        
        # Get categories for selected top city
        top_category_options = top_city_data['Category'].unique()
        selected_top_category = st.selectbox("Choose a Category", options=top_category_options, key="top_category")
        
        # Get profit value
        top_profit = top_city_data[top_city_data['Category'] == selected_top_category]['Profit'].values[0].round(2)
        st.metric(label=f"{selected_top_category} Profit in {selected_top_city}", value=f"${top_profit}")
    
    with col2:
        # Bottom Cities Section
        st.subheader("Least Profitable Cities")
        st.dataframe(df_bottom_cities, use_container_width=True)
        fig_bottom_cities = px.bar(
            df_bottom_cities,
            x="Geography",  
            y="Profit",
            title="Bottom 5 Least Profitable Cities",
            template="plotly_white"
        )
        st.plotly_chart(fig_bottom_cities, use_container_width=True)

        # Bottom Cities Category Analysis
        st.title("Bottom 5 Cities for Profit by Category")
        st.markdown("Select a city and then a category to view the corresponding profit.")

        # Use filtered data for BOTTOM cities only
        bottom_city_options = df_prof_cat_bottom['City'].unique()  # Should contain only bottom 5 cities
        selected_bottom_city = st.selectbox("Choose a Bottom City", options=bottom_city_options, key="bottom_city")
        
        # Filter data for selected bottom city
        bottom_city_data = df_prof_cat_bottom[df_prof_cat_bottom['City'] == selected_bottom_city]
        
        # Get categories for selected bottom city
        bottom_category_options = bottom_city_data['Category'].unique()
        selected_bottom_category = st.selectbox("Choose a Category", options=bottom_category_options, key="bottom_category")
        
        # Get profit value
        bottom_profit = bottom_city_data[bottom_city_data['Category'] == selected_bottom_category]['Profit'].values[0].round(2)
        st.metric(label=f"{selected_bottom_category} Profit in {selected_bottom_city}", value=f"${bottom_profit}")

# --- Tab 4: Top 10 Profitable Customers ---
with tab_customers:
    st.header("Top 10 Most Profitable Customers")
    st.dataframe(df_top10_customers, use_container_width=True)
    fig_customers = px.bar(
        df_top10_customers,
        x="Customer",
        y="Total_profit",
        title="Top 10 Profitable Customers",
        template="plotly_white"
    )
    st.plotly_chart(fig_customers, use_container_width=True)
    st.markdown("**Note:** These customers contribute significantly to overall profitability.")

