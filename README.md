# power-manager-telemetry
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
