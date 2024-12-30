import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
from configparser import RawConfigParser

# Set up Streamlit page configuration
st.set_page_config(layout="wide")
st.title("Cryptocurrency Prices Visualization")

# Load configuration
config_local = RawConfigParser()
config_local.read("config_local.conf")

# Connect to MongoDB
try:
    print(config_local['MongoDB']['url'])
    client = MongoClient(config_local['MongoDB']['url'])
    db = client[config_local['MongoDB']['database']]
    collection = db[config_local['MongoDB']['collection']]
    st.success("Connected to MongoDB successfully!")
except Exception as e:
    st.error(f"Failed to connect to MongoDB: {e}")
    st.stop()

# Fetch data from MongoDB
data_list = []
projection = {
    "timestamp": 1,  # Include the 'timestamp' field
    "data.name": 1,  # Include 'name' inside the 'data' array
    "data.priceUsd": 1,
    "_id": 0         # Exclude the '_id' field
}
try:
    documents = collection.find({}, projection)
    for doc in documents:
        timestamp = doc.get("timestamp")
        if "data" in doc:
            for data_item in doc["data"]:
                data_list.append({
                    "timestamp": timestamp,
                    "name": data_item["name"],
                    "price": round(float(data_item["priceUsd"]), 3)
                })
except Exception as e:
    st.error(f"Error fetching data from MongoDB: {e}")
    st.stop()

# Convert data to DataFrame
df = pd.DataFrame(data_list)
if df.empty:
    st.warning("No data found in the database.")
    st.stop()


# Extract unique cryptocurrencies for the dropdown
currencies = df['name'].unique()
selected_currency = st.selectbox("Select a cryptocurrency", currencies)

# Filter data for the selected currency
df1 = df[df['name'] == selected_currency].copy()

# Convert timestamp to datetime
df1['timestamp'] = pd.to_datetime(df1['timestamp'])

df1['time'] = df1['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')


# Plot the data
fig, ax = plt.subplots(figsize=(20, 6))
sns.lineplot(data=df1, x='time', y='price', marker='o', color='green', label=selected_currency, errorbar=None, ax=ax)

# Customize the plot
ax.legend(title="Cryptocurrency")
ax.set_xticklabels(df1['time'], rotation=45, ha='right')
ax.set_xlabel('Timestamp')
ax.set_ylabel('Price (USD)')
ax.set_title('Price of Cryptocurrency over time')

# Display the plot in Streamlit
st.pyplot(fig)

# Show a preview of the data table
st.write("Data preview:", df1.head(10))
