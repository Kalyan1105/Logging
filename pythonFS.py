import re
from collections import deque, defaultdict
log_sys={
    "cap":5,
    "r_logs":deque(maxlen=5),
    "u_logs":defaultdict(list),
    "l_count":defaultdict(int)
}
# class LogSystem:
def add_log(line: str):
    match=re.match(r"\[(.*?)\] (\w+) (\w+): (.*)",line)
    if not match:
        return
    time,lev,u_id,msg=match.groups()
    log_entry={
        "time":time,
        "lev":lev,
        "u_id":u_id,
        "msg":msg
    }
    log_sys["r_logs"].append(log_entry)
    log_sys["u_logs"][u_id].append(log_entry)
    log_sys["l_count"][lev] += 1
def get_user_logs(user_id: str):
    return log_sys["u_logs"].get(user_id,[])
def get_recent_logs():
    return log_sys["r_logs"]
def count_levels():
    return dict(log_sys["l_count"])
def filter_logs(keyword:str):
    keyword=keyword.lower()
    return [log for log in log_sys["r_logs"] if keyword in log["msg"].lower()]

logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]

for log in logs:
    add_log(log)
print("User Logs (user1):", get_user_logs("user1"),"\n")
print("Level Count:", count_levels(),"\n")
print("Filter 'Timeout':", filter_logs("timeout"),"\n")
print("Recent Logs:", get_recent_logs(),"\n")


