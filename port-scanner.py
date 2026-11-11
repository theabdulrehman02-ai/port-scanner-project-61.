import socket
from datetime import datetime
import threading

print("PORT SCANNER - Project #61")
print("-" * 40)

target = input("Enter Target IP / Website: ")
start_port = int(input("Enter Starting Port: "))
end_port = int(input("Enter Ending Port: "))

try:
    target_ip = socket.gethostbyname(target)
except:
    print("Invalid target!")
    exit()

print(f"\nScanning {target} ({target_ip})...")
print(f"Time: {datetime.now()}")
print("-" * 40)

open_ports = []

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"Port {port}: OPEN")
        open_ports.append(port)
    s.close()

threads = []
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("-" * 40)
print("Scan Done!")

# result file me save karna
with open("result.txt", "w") as f:
    f.write(f"Target: {target} ({target_ip})\n")
    f.write(f"Date: {datetime.now()}\n")
    f.write(f"Open Ports: {open_ports}\n")
    
print("Result result.txt me save ho gaya!")
