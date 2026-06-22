import socket
import threading
import subprocess
from queue import Queue
from datetime import datetime

#blank your screen
subprocess.call ('clear', shell=True)

# ==========================================
# Configuration
# ==========================================
NUM_THREADS = 100
TIMEOUT = 1  # seconds

# ==========================================
# Port Scanner Function
# ==========================================
def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)

        result = sock.connect_ex((host, port))

        if result == 0:
            status = "OPEN"
        elif result == 10060:
            status = "TIMEOUT"
        else:
            status = "CLOSED"

        sock.close()

    except socket.timeout:
        status = "TIMEOUT"

    except Exception as e:
        status = f"ERROR: {e}"

    print (f"Port {port:<5} : {status}")

    with open("scan_results.txt", "a") as logfile:
        logfile.write(f"Port {port:<5} : {status}\n")


# ==========================================
# Thread Worker
# ==========================================
def worker():
    while True:
        port = q.get()

        scan_port(target_ip, port)

        q.task_done()


# ==========================================
# Main Program
# ==========================================
print ("=" * 60)
print ("TCP Port Scanner")
print ("=" * 60)

host = input("Enter target host/IP: ")

try:
    target_ip = socket.gethostbyname(host)
except socket.gaierror:
    print ("Hostname could not be resolved.")
    exit()

start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

print ("\nTarget:", host)
print ("IP:", target_ip)
print (f"Scanning Ports: {start_port} - {end_port}")
print ("=" * 60)

start_time = datetime.now()

# Clear old log file
open("scan_results.txt", "w").close()

q = Queue()

# Create threads
for _ in range(NUM_THREADS):
    thread = threading.Thread(target=worker)
    thread.daemon = True
    thread.start()

# Add ports to queue
for port in range(start_port, end_port + 1):
    q.put(port)

try:
    q.join()

except KeyboardInterrupt:
    print ("\nScan interrupted by user.")
    exit()

end_time = datetime.now()

print ("\n" + "=" * 60)
print ("Scan Complete")
print ("Started :", start_time)
print ("Finished:", end_time)
print ("Duration:", end_time - start_time)
print ("Results saved to scan_results.txt")
print ("=" * 60)
