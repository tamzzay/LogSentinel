# 🛡️ LogSentinel 

### Real-Time Log Analysis & Threat Detection Dashboard

LogSentinel AI is a real-time cybersecurity monitoring system that analyzes log data to detect suspicious activities, visualize attack patterns, and provide instant threat insights through an interactive dashboard.

Built with a focus on **Security Operations Center (SOC)-style monitoring**, the system combines log parsing, anomaly detection, and real-time visualization.

---

## 🚀 Key Features

### ⚡ Real-Time Monitoring
- Live log streaming using WebSockets (no delay)
- Instant dashboard updates without refresh

### 📊 Interactive Dashboard
- Total Logs, Admin Hits, Delete Requests counters
- Status code distribution (200, 404, 500, etc.)
- Log rate trend visualization
- Clean SOC-style UI

### 🌍 Attack Visualization
- Geo-based IP tracking on world map
- Real-time attack source plotting

### 📡 Live Log Feed
- Streaming logs displayed in real time
- Highlights suspicious patterns and requests

### 🚨 Threat Detection & Alerts
- Detects:
  - Brute force attacks (/admin abuse)
  - Suspicious DELETE requests
  - Server errors (500 spikes)
- Dynamic threat classification:
  - LOW / MEDIUM / HIGH
- Real-time alert popups

### 🤖 AI-Based Analysis
- Uses anomaly detection (Isolation Forest)
- Identifies unusual traffic patterns
- Confidence scoring for detected threats

---

## 🧰 Tech Stack

- **Backend:** Python, Flask  
- **Real-Time Engine:** Flask-SocketIO (WebSockets)  
- **Frontend:** HTML, CSS, JavaScript  
- **Visualization:** Chart.js  
- **Mapping:** Folium  
- **Machine Learning:** Scikit-learn (Isolation Forest)

---

## 📦 Installation

### 1. Clone the repository
git clone https://github.com/tamzzay/LogSentinel.git
cd LogSentinel

### 2. Install dependencies
python -m pip install -r requirements.txt

### 3. Run the application
python logsentinel.py

---
## ▶️ Usage
Start the application
Enter the path to your log file when prompted:
Enter log file path: /path/to/logfile.log

## Open your browser:
http://127.0.0.1:5000

View real-time dashboard updates as logs are processed

## 📊 Dashboard Overview
- **Total Logs:** Total processed entries
- **Admin Hits:** Potential brute-force attempts
- **Delete Requests:** Suspicious destructive actions
- **Status Codes Chart:** Distribution of HTTP responses
- **Log Rate Graph:** Traffic trend over time
- **Live Logs Panel:** Streaming log activity
- **Attack Map:** Global attack sources

---
## ⚙️ How It Works
Log file is monitored in real time (file streaming)
Each log line is parsed using regex

### Key indicators are extracted:
- **IP address**
- **Request type**
- **Status code**

Data is processed and updated dynamically
WebSocket sends updates instantly to frontend
AI model analyzes patterns for anomalies
Dashboard reflects live system state

## 🧠 Threat Detection Logic
- **Indicator	Detection** 
- **High /admin requests	Brute-force attack** 
- **Frequent DELETE requests	Data manipulation attempt**
- **High 500 errors	Server exploit attempt**

----
## 📄 License
MIT License — free to use, modify, and distribute.

----
## 👩‍💻 Author
Developed as a cybersecurity project focusing on real-time threat detection, log analysis, and SOC-style monitoring systems.
