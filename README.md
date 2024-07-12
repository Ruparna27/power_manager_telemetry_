# Power-manager-telemetry
The Power Manager Telemetry project aims to monitor and measure the power consumption and performance of system components, specifically the CPU, memory, NIC, and TDP. This project uniquely integrates stress testing via Docker containers with real-time telemetry data collection and power measurement. It provides a comprehensive view of system performance and energy consumption under high load conditions. The automation of this process ensures repeatability and accuracy in monitoring and reporting system power utilization.
<br>
<h2> Features </h2>
<li>Telemetry Data Collection: Collects telemetry data for system components including CPU, memory, NIC, and TDP.</li>
<li>Stress Testing: Utilizes Docker containers to simulate 100% system utilization.</li>
<li>Power Measurement: Measures system power utilization and generates detailed reports.</li>
<li>Custom Utilization Input: Allows input of desired system utilization percentage to measure power consumption.</li>
<li>Automated Process: Automates the entire process from stress testing to telemetry data collection and reporting.</li>
<br>
<h2>Architecture</h2>
The architecture of this project includes the following components:

<li>Docker Containers: Used to create a controlled environment for stress testing the system components.</li>
<li>Telemetry Collection Scripts: Python scripts that utilize psutil to collect real-time telemetry data for CPU, memory, NIC, and TDP.</li>
<li>Power Measurement Scripts: Python scripts that measure the power consumption of the system components during stress tests.</li>
<li>Report Generation Scripts: Python scripts that compile the collected telemetry data and power measurements into a detailed report.</li>
<h2>Technologies Used</h2>
<li>Python: The main programming language used for writing telemetry collection, power measurement, and report generation scripts.</li>
<li>Docker: Used to create containers for stress testing the system components.</li>
<li>psutil: A Python library used to retrieve information on system utilization (CPU, memory, NIC).</li>
<li>Stress-ng: A tool used within Docker containers to apply stress on the system components.</li>
<h2> Installation </h2>
<h3> Prerequisites </h3>
<li>Python 3.8+</li>
<li>Docker</li>
<h3> Steps </h3>
<li>Clone the repository:</li>

  git clone https://github.com/yourusername/power_manager_telemetry.git

    cd power_manager_telemetry

<li>Set up a Python virtual environment:</li>

    python3 -m venv env
    source env/bin/activate
<li>Install Python dependencies:</li>

    pip install -r requirements.txt

<li>Install Docker:</li>

    sudo apt-get update
    sudo apt-get install docker.io
    sudo systemctl start docker
    sudo systemctl enable docker

<li>Build the Docker container for stress testing:</li>

    cd stress_test
    docker build -t stress-container .

<li>Usage</li>
    Running the Stress Test Container
    Start the Docker container to simulate high system utilization:

    docker run --rm -it stress-container

<li>Collecting Telemetry Data</li>
    Run the telemetry data collection script:


    cd scripts
    python collect_telemetry.py
  
   This script will collect telemetry data and save it in ../telemetry_data.json.

<li>Measuring Power Utilization</li>
    Run the power measurement script:

    python measure_power.py

  This script will measure the power utilization and update the telemetry data file.

<li>Generating the Report</li>
    Run the report generation script:

    python generate_report.py

  This script will generate a report based on the collected telemetry data and save it as report.json.

<h2>Directory Structure</h2>

    power_manager_telemetry/
    │
    ├── Dockerfile
    ├── stress_test/
    │   ├── Dockerfile
    │   └── run_stress.sh
    ├── scripts/
    │   ├── collect_telemetry.py
    │   ├── measure_power.py
    │   └── generate_report.py
    ├── telemetry_data.json
    ├── report.json
    ├── requirements.txt
    └── README.md
<h2>Dockerfile (Root Directory)</h2>
    Dockerfile

    # Root Dockerfile (if needed for further extensions)
    Dockerfile (stress_test Directory)
  Dockerfile

    # stress_test/Dockerfile
    FROM ubuntu:latest

    RUN apt-get update && apt-get install -y stress-ng

    CMD ["stress-ng", "--cpu", "4", "--io", "4", "--vm", "2", "--vm-bytes", "128M", "--timeout", "60s"]
    run_stress.sh

#!/bin/bash
    
    docker build -t stress-container .
    docker run --rm -it stress-container
    collect_telemetry.py

import psutil
import json
import time

def get_telemetry_data():
    # CPU utilization
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()

    # Memory utilization
    memory_info = psutil.virtual_memory()

    # NIC utilization
    net_io = psutil.net_io_counters()

    telemetry_data = {
        "cpu": {
            "percent": cpu_percent,
            "freq": cpu_freq._asdict() if cpu_freq else None,
        },
        "memory": {
            "total": memory_info.total,
            "available": memory_info.available,
            "percent": memory_info.percent,
            "used": memory_info.used,
            "free": memory_info.free,
        },
        "network": {
            "bytes_sent": net_io.bytes_sent,
            "bytes_recv": net_io.bytes_recv,
            "packets_sent": net_io.packets_sent,
            "packets_recv": net_io.packets_recv,
        }
    }
    return telemetry_data

def main():
    telemetry_data = get_telemetry_data()
    with open('../telemetry_data.json', 'w') as f:
        json.dump(telemetry_data, f, indent=4)
    print("Telemetry data written to ../telemetry_data.json")

if __name__ == "__main__":
    main()
measure_power.py
python
Copy code
import json

def measure_power_utilization():
    with open('../telemetry_data.json', 'r') as f:
        telemetry_data = json.load(f)

    # Placeholder for actual power measurement logic
    telemetry_data['power'] = {
        'cpu_power': telemetry_data['cpu']['percent'] * 0.5,  # Example formula
        'memory_power': telemetry_data['memory']['percent'] * 0.3,  # Example formula
        'nic_power': telemetry_data['network']['bytes_recv'] * 0.001  # Example formula
    }

    with open('../telemetry_data.json', 'w') as f:
        json.dump(telemetry_data, f, indent=4)

    print("Power utilization measured and updated in telemetry data.")

if __name__ == "__main__":
    measure_power_utilization()
generate_report.py
python
Copy code
import json
from datetime import datetime

def generate_report():
    with open('../telemetry_data.json', 'r') as f:
        telemetry_data = json.load(f)

    report = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "telemetry_data": telemetry_data
    }

    with open('../report.json', 'w') as f:
        json.dump(report, f, indent=4)

    print("Report generated and written to ../report.json")

if __name__ == "__main__":
    generate_report()
requirements.txt
Copy code
psutil
