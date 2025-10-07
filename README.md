# 🧩 Kafka Event Streaming Service

A lightweight and scalable **event-driven system** built using **Apache Kafka**.  
This project demonstrates how to produce and consume messages efficiently between microservices using Kafka.

---

## 🚀 Features
- Kafka **Producer** and **Consumer** implementation  
- JSON-based message serialization  
- Configurable **topics** and **brokers**  
- **Retry** and **error handling** mechanism  
- Docker Compose setup for Kafka and Kraft  
- Sample **event flow** for testing  

---

## 🏗️ Project Structure
```
📂 kafka-event-service
 ┣ 📂 producer
 ┣ 📂 consumer
 ┣ 📂 config
 ┣ 📜 docker-compose.yml
 ┗ 📜 README.md
```

---

## ⚙️ Prerequisites
Before you start, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Kafka](https://kafka.apache.org/)
- [Python](https://www.python.org/)
- Git

---

## 🧰 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/kafka-event-service.git
cd kafka-event-service
```

### 2️⃣ Start Kafka with Docker
```bash
docker compose up -d
```

### 3️⃣ Run the Producer
```bash
python producer/producer.py
```
or  
```bash
dotnet run --project Producer
```

### 4️⃣ Run the Consumer
```bash
python consumer/consumer.py
```
or  
```bash
dotnet run --project Consumer
```

---

## 🧪 Example Message
```json
{
  "order_id": "a8f2b3e1-44d6-4f29-b9ab-1a223e5cd912",
  "user_id": "Ali",
  "product": "Sokany",
  "quantity": 10
}
```

---

## 📊 Kafka Topics
| Topic Name | Description |
|-------------|-------------|
| `orders` | Handles new order messages |

---

## 🧠 Learning Goals
- Understand Kafka’s producer-consumer model  
- Learn message serialization and deserialization  
- Implement event-driven architecture patterns  

---

## 🛠️ Tech Stack
- **Language:** Python
- **Broker:** Apache Kafka  
- **Containerization:** Docker  
- **Message Format:** JSON  

---

## 🤝 Contributing
Pull requests are welcome!  
If you find a bug or have an enhancement idea, open an issue first to discuss it.

---

## 📬 Contact
**Author:** Abdulsalam Al-Shuaibi  
**LinkedIn:** [linkedin.com/in/abdulsalamalshuaibi](https://linkedin.com/in/abdulsalamalshuaibi)  
s
