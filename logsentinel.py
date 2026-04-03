import re
import time
import threading
import pandas as pd
from collections import Counter, deque
from sklearn.ensemble import IsolationForest
import folium
import requests
from flask import Flask, render_template, jsonify
from datetime import datetime
import os

# --- GLOBAL VARIABLES ---
ip_counts = Counter()
status_counts = Counter()
recent_logs = deque(maxlen=20)
log_timestamps = deque(maxlen=1000)

admin_hits = 0
delete_hits = 0
total_logs = 0
error_5xx = 0
last_total_logs = 0
logs_per_sec = 0

threat_level = "✅ LOW RISK"
attack_type = "Normal Traffic"
confidence = 0
seen_ips = set()
lock = threading.Lock()

# --- CONFIG ---
app = Flask(__name__)
# Ensure static folder exists for the map
if not os.path.exists('static'):
    os.makedirs('static')

# --- REGEX ---
ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
admin_pattern = re.compile(r'/admin|admin\.php|wp-admin', re.IGNORECASE)
delete_pattern = re.compile(r'"DELETE', re.IGNORECASE)
status_pattern = re.compile(r'\s(\d{3})\s')


def init_map():
    m = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB dark_matter')
    m.save("static/attack_map.html")
    return m


world_map = init_map()


def process_log(line):
    global admin_hits, delete_hits, total_logs, error_5xx
    global threat_level, attack_type, confidence

    with lock:
        total_logs += 1

        # Extract Status Code
        status = "200"
        s_match = status_pattern.search(line)
        if s_match:
            status = s_match.group(1)
            status_counts[status] += 1
            if status.startswith('5'): error_5xx += 1

        # Extract IP
        ip_match = ip_pattern.search(line)
        ip = ip_match.group(1) if ip_match else "0.0.0.0"
        ip_counts[ip] += 1

        # Check Threats
        is_threat = False
        if admin_pattern.search(line):
            admin_hits += 1
            is_threat = True
        if delete_pattern.search(line):
            delete_hits += 1
            is_threat = True

        recent_logs.append({
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'log': line[:100] + '...',
            'threat': '💀' if is_threat else '✅'
        })

        # Calculate Threat Level
        score = (admin_hits * 5) + (delete_hits * 10) + (error_5xx * 2)
        confidence = min(100, score)
        if score > 50:
            threat_level = "🛑 HIGH RISK"
            attack_type = "Brute Force / Deletion"
        elif score > 20:
            threat_level = "⚠️ MEDIUM RISK"
            attack_type = "Suspicious Activity"
        else:
            threat_level = "✅ LOW RISK"
            attack_type = "Normal Traffic"


def monitor_log_rate():
    global last_total_logs, logs_per_sec
    while True:
        current = total_logs
        logs_per_sec = current - last_total_logs
        last_total_logs = current
        time.sleep(1)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/data")
def get_data():
    with lock:
        return jsonify({
            "total_logs": total_logs,
            "admin": admin_hits,
            "delete": delete_hits,
            "errors": error_5xx,
            "threat": threat_level,
            "confidence": confidence,
            "logs_per_sec": logs_per_sec,
            "status_codes": dict(status_counts),
            "recent_logs": list(recent_logs)
        })


if __name__ == "__main__":
    path = input("🔍Enter log file path: ").strip() or "demo.log"

    if not os.path.exists(path):
        with open(path, "w") as f: f.write("127.0.0.1 - - [01/Jan/2024] \"GET / HTTP/1.1\" 200 1024\n")


    def start_monitoring():
        # Read existing file first
        with open(path, "r") as f:
            for line in f:
                process_log(line)

            # Now wait for new lines
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                process_log(line)


    threading.Thread(target=start_monitoring, daemon=True).start()
    threading.Thread(target=monitor_log_rate, daemon=True).start()

    print(f"🚀 Dashboard: http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)