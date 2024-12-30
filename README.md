# Real-Time Cryptocurrency Data Analysis

## 📄 Project Overview

This project focuses on real-time cryptocurrency data analysis using **Apache Kafka**, **MongoDB**, and **Streamlit** for data visualization. The system fetches live cryptocurrency data from the CoinCap public [API](https://api.coincap.io/v2/assets), processes it using Kafka, stores it in MongoDB, and visualizes the data to observe price fluctuations over time.

## 🛠️ Architecture
The project follows a **Producer-Consumer** pattern:
- **Producer**: Continuously fetches cryptocurrency data from the API and publishes it to a Kafka topic.
- **Consumer**: Consumes data from the Kafka topic, processes it using Apache Spark, and stores the processed data in MongoDB for further visualization.

![Architecture](Architecture.png)

---

## 🛠️ Technologies Used

- **Python**: Data fetching, processing, and programming.
- **Apache Kafka**: Real-time data streaming.
- **MongoDB**: NoSQL database for storing historical data.
- **CoinCap API**: Source for live cryptocurrency data.
- **Pandas**: Data analysis and manipulation.
- **Streamlit**: Data visualization and plotting using Matplotlib.
- **Docker**: For containerization of the application

---

## ⚙️ Setup with Docker
Run ``docker-compose up`` to start the services defined in the compose file

## ⚙️ Setup without Docker

Follow the steps below to set up the project on your local system:

### Step 1: Download and Extract Kafka
```
wget https://downloads.apache.org/kafka/3.8.1/kafka_2.12-3.8.1.tgz
tar -xvf kafka_2.12-3.8.1.tgz
cd kafka_2.12-3.8.1
```

### Step 2: Start Zookeeper Server
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Step 3: Start Kafka Server
```
bin/kafka-server-start.sh config/server.properties
```

### Step 4: Create a Kafka Topic
```
bin/kafka-topics.sh --create --topic crypto-currency --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### Step 5: Start Producer
```
bin/kafka-console-producer.sh --topic crypto-currency --bootstrap-server localhost:9092
```

### Step 6: Start Consumer
```
bin/kafka-console-consumer.sh --topic crypto-currency --bootstrap-server localhost:9092 --from-beginning
```

### Step 7: Install MongoDB
```
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb/brew/mongodb-community
```

### Step 8: Streamlit
```
pip install streamlit
streamlit run streamlit_crypto_data_visualization.py
```


  