### LogSentinel

A Linux Log Analyzer for Detecting Suspicious Activity

LogSentinel is a powerful Linux log analyzer that detects suspicious activity, including failed login attempts, brute-force attacks, and unauthorized access attempts. It helps system administrators, security enthusiasts, and ethical hackers monitor, audit, and improve system security.

---
### Features
- Detects failed login attempts (potential brute-force attacks)
- Lists successful logins by IP 
- Detects suspicious access attempts to sensitive paths (/etc/, /admin, /root, .php)
- Supports Linux log formats (/var/log/auth.log)
- Outputs a summary of top offenders and suspicious paths 
- Lightweight Python script — no external dependencies required

---
### Requirements

Python 3.x

Linux system logs (/var/log/auth.log) or exported log files in text format

---

### Installation

Clone the repository:

git clone https://github.com/yourusername/LogSentinel.git

Navigate to the project directory:

cd LogSentinel


Run the script:

python3 log_analyzer.py

---
### Usage

Place your Linux log file somewhere accessible, e.g., ~/logs/auth.log

Run the script:

python3 log_analyzer.py


Enter the full path to your log file when prompted:

Enter path to log file: /home/user/logs/auth.log

---
### Sample Output 
📄 Log Analyzer — Suspicious Activity Detector
--------------------------------------------------
Enter path to log file: sample_auth.log

🔎 Analysis Summary
--------------------------------------------------

🚫 Top IPs with Failed Logins:
 - 203.0.113.45: 7 failed attempts
 - 185.23.91.10: 3 failed attempts
 - 192.168.1.55: 2 failed attempts

🟢 Successful Logins:
 - 192.168.1.20: 3 success
 - 10.0.0.5: 1 success

⚠ Suspicious Access Attempts:
 - GET /etc/passwd HTTP/1.1
 - POST /admin/login.php HTTP/1.1
 - GET /root/.ssh/id_rsa HTTP/1.1
---
### How it Works

 - The script reads the log file line by line.

Uses regular expressions to find:

 - Failed login attempts
 - Successful logins
 - Suspicious paths

Counts occurrences using collections.Counter and displays top offenders.

----
### Future Improvements

 - Add Windows log support
 - Export results to CSV/JSON
 - Add geolocation for suspicious IPs
 - Visualize top offenders with charts

---
### License

MIT License — feel free to use, modify, and contribute.