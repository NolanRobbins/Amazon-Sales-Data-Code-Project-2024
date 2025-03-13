# Amazon Sales Business Analytics Project

![Dashboard Screenshot](./images/dashboard.jpeg)

## Project Overview
This project analyzes the Kaggle Amazon Sales Dataset to provide business intelligence insights through exploratory data analysis (EDA) and an interactive Streamlit dashboard. The project focuses on customer segmentation, product profitability, geographical analysis, and fulfillment metrics.

## Live Demo
View the deployed Streamlit application here: [Amazon Sales Dashboard](https://amazon-sales-data-code-project-2024-nolan-robbins.streamlit.app/)

## Key Questions Explored
1. **Customer Value Analysis**: Analyzing top customers by order frequency vs. profit generation
2. **Product Profitability**: Identifying which product categories drive the highest profits
3. **Geographical Analysis**: Examining high and low-performing cities and the products driving those results
4. **Fulfillment Efficiency**: Measuring order-to-ship timeframes across product categories

## Features
- **RFM Customer Segmentation**: Classifies customers into Gold, Silver, and Bronze tiers based on Recency, Frequency, and Monetary value
- **Interactive Visualizations**: Plotly-powered charts and graphs for data exploration
- **City-Specific Product Analysis**: Dropdown selectors to analyze product performance by location
- **Cohort Analysis**: Customer retention visualization through cohort indexing

## Technologies Used
- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib/Seaborn**: Data visualization in Jupyter notebook
- **Plotly**: Interactive visualizations in Streamlit dashboard
- **Streamlit**: Web application framework for deployment
- **Google Colab**: Initial exploratory data analysis

## Project Structure
```
├── data/                     # Excel files with processed data
│   ├── RFM.xlsx
│   ├── Total Profit Categories.xlsx
│   ├── Top 5 Cities.xlsx
│   ├── Bottom 5 Cities.xlsx
│   ├── Top 10 Customers.xlsx
│   ├── Prof Cat Top.xlsx
│   └── Prof Cat Bottom.xlsx
├── Amazon_2_Raw.xlsx         # Original dataset
├── st_dashboard.py           # Streamlit dashboard code
├── requirements.txt          # Required libraries for deployment
└── README.md                 # Project documentation
```

## Key Insights

### Customer Analysis
- No correlation between customers with highest order frequency and highest profit generation
- Gold tier customers (based on RFM) show the best metrics across recency, frequency, and monetary value
- Silver tier customers are closer to Gold in purchase recency but closer to Bronze in monetary value

### Product Analysis
- "Binders" and "Copiers" are the most profitable product categories
- Top profit customers predominantly purchase from these same high-profit categories

### Geographical Analysis
- "Binders", "Copiers", and "Accessories" drive profits in top-performing cities
- "Machines", "Bookcases", and "Tablets" contribute to losses in the bottom-performing cities (with Phoenix being a notable example)

### Fulfillment Analysis
- No significant outliers in shipping times across product categories
- Consistent fulfillment performance across the product range

## Installation and Setup

1. Clone this repository:
```bash
git clone https://github.com/your-username/amazon-sales-analytics.git
cd amazon-sales-analytics
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit application locally:
```bash
streamlit run st_dashboard.py
```

## Data Processing
The project workflow included:
1. Data cleaning and formatting (including email-to-name conversion)
2. Customer segmentation using RFM analysis
3. Product and geographical profit analysis
4. Cohort analysis for retention insights
5. Export of processed data to Excel for dashboard consumption

## Dashboard Components
- **RFM Medal Results**: Distribution of customer medals with metrics
- **Total Profit by Category**: Visualization of profit by product category
- **City Profitability**: Comparative analysis of top and bottom performing cities
- **Top Customers**: Overview of the 10 most profitable customers

## Future Improvements
- Integration with real-time data sources
- Predictive analytics for customer churn and product performance
- Expanded shipping and logistics analysis
- Customer journey mapping

## Contact
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nolan-robbins-2768b2150/)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@nolanrobbins5934)

