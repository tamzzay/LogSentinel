import re
from collections import Counter

print("\n📄 Log Analyzer — Suspicious Activity Detector")
print("--------------------------------------------------")

log_file = input("Enter path to log file: ").strip()

try:
    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        logs = f.readlines()
except FileNotFoundError:
    print("❌ File not found.")
    exit()


failed_login_pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")
success_login_pattern = re.compile(r"Accepted password.*from (\d+\.\d+\.\d+\.\d+)")
suspicious_path_pattern = re.compile(r"(\/etc\/|\/admin|\/root|\.php)")

failed_attempts = Counter()
successful_attempts = Counter()
suspicious_access = []


for line in logs:
    fail = failed_login_pattern.search(line)
    success = success_login_pattern.search(line)
    suspicious = suspicious_path_pattern.search(line)

    if fail:
        failed_attempts[fail.group(1)] += 1
    if success:
        successful_attempts[success.group(1)] += 1
    if suspicious:
        suspicious_access.append(line.strip())


print("\n🔎 Analysis Summary")
print("--------------------------------------------------")

print("\n🚫 Top IPs with Failed Logins:")
for ip, count in failed_attempts.most_common(5):
    print(f" - {ip}: {count} failed attempts")

print("\n🟢 Successful Logins:")
for ip, count in successful_attempts.items():
    print(f" - {ip}: {count} success")

print("\n⚠ Suspicious Access Attempts:")
if suspicious_access:
    for entry in suspicious_access[:10]:
        print(f" - {entry}")
else:
    print("No suspicious paths accessed.")
