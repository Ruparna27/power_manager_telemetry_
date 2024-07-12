# power-manager-telemetry
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power Manager Telemetry</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        header {
            background: #333;
            color: #fff;
            padding-top: 30px;
            min-height: 70px;
            border-bottom: #77aaff 3px solid;
        }
        header a {
            color: #fff;
            text-decoration: none;
            text-transform: uppercase;
            font-size: 16px;
        }
        header ul {
            padding: 0;
            list-style: none;
        }
        header li {
            float: right;
            display: inline;
            padding: 0 20px 0 20px;
        }
        header #branding {
            float: left;
        }
        header #branding h1 {
            margin: 0;
        }
        header nav {
            float: right;
            margin-top: 10px;
        }
        header .highlight, header .current a {
            color: #77aaff;
            font-weight: bold;
        }
        header a:hover {
            color: #77aaff;
            font-weight: bold;
        }
        .content {
            padding: 20px;
            background: #fff;
            margin-bottom: 20px;
        }
        .content h2 {
            color: #333;
        }
        .content pre {
            background: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div id="branding">
                <h1>Power Manager Telemetry</h1>
            </div>
        </div>
    </header>

    <div class="container">
        <div class="content">
            <h2>Project Overview</h2>
            <p>The Power Manager Telemetry project aims to monitor and measure the power consumption and performance of system components, specifically the CPU, memory, NIC, and TDP. This project uniquely integrates stress testing via Docker containers with real-time telemetry data collection and power measurement. It provides a comprehensive view of system performance and energy consumption under high load conditions. The automation of this process ensures repeatability and accuracy in monitoring and reporting system power utilization.</p>

            <h2>Features</h2>
            <ul>
                <li>Telemetry Data Collection: Collects telemetry data for system components including CPU, memory, NIC, and TDP.</li>
                <li>Stress Testing: Utilizes Docker containers to simulate 100% system utilization.</li>
                <li>Power Measurement: Measures system power utilization and generates detailed reports.</li>
                <li>Custom Utilization Input: Allows input of desired system utilization percentage to measure power consumption.</li>
                <li>Automated Process: Automates the entire process from stress testing to telemetry data collection and reporting.</li>
            </ul>

            <h2>Architecture</h2>
            <p>The architecture of this project includes the following components:</p>
            <ul>
                <li>Docker Containers: Used to create a controlled environment for stress testing the system components.</li>
                <li>Telemetry Collection Scripts: Python scripts that utilize <code>psutil</code> to collect real-time telemetry data for CPU, memory, NIC, and TDP.</li>
                <li>Power Measurement Scripts: Python scripts that measure the power consumption of the system components during stress tests.</li>
                <li>Report Generation Scripts: Python scripts that compile the collected telemetry data and power measurements into a detailed report.</li>
            </ul>

            <h2>Technologies Used</h2>
            <ul>
                <li>Python: The main programming language used for writing telemetry collection, power measurement, and report generation scripts.</li>
                <li>Docker: Used to create containers for stress testing the system components.</li>
                <li>psutil: A Python library used to retrieve information on system utilization (CPU, memory, NIC).</li>
                <li>Stress-ng: A tool used within Docker containers to apply stress on the system components.</li>
            </ul>

            <h2>Installation</h2>
            <h3>Prerequisites</h3>
            <ul>
                <li>Python 3.8+</li>
                <li>Docker</li>
            </ul>

            <h3>Steps</h3>
            <ol>
                <li>Clone the repository:
                    <pre><code>git clone https://github.com/yourusername/power_manager_telemetry.git
cd power_manager_telemetry</code></pre>
                </li>
                <li>Set up a Python virtual environment:
                    <pre><code>python3 -m venv env
source env/bin/activate</code></pre>
                </li>
                <li>Install Python dependencies:
                    <pre><code>pip install -r requirements.txt</code></pre>
                </li>
                <li>Install Docker:
                    <pre><code>sudo apt-get update
sudo apt-get install docker.io
sudo systemctl start docker
sudo systemctl enable docker</code></pre>
                </li>
                <li>Build the Docker container for stress testing:
                    <pre><code>cd stress_test
docker build -t stress-container .</code></pre>
                </li>
            </ol>

            <h2>Usage</h2>
            <h3>Running the Stress Test Container</h3>
            <p>Start the Docker container to simulate high system utilization:</p>
            <pre><code>docker run --rm -it stress-container</code></pre>

            <h3>Collecting Telemetry Data</h3>
            <p>Run the telemetry data collection script:</p>
            <pre><code>cd scripts
python collect_telemetry.py</code></pre>
            <p>This script will collect telemetry data and save it in <code>../telemetry_data.json</code>.</p>

            <h3>Measuring Power Utilization</h3>
            <p>Run the power measurement script:</p>
            <pre><code>python measure_power.py</code></pre>
            <p>This script will measure the power utilization and update the telemetry data file.</p>

            <h3>Generating the Report</h3>
            <p>Run the report generation script:</p>
            <pre><code>python generate_report.py</code></pre>
            <p>This script will generate a report based on the collected telemetry data and save it as <code>report.json</code>.</p>

            <h2>Directory Structure</h2>
            <pre><code>power_manager_telemetry/
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
└── README.md</code></pre>

            <h2>Contribution</h2>
            <p>Contributions are welcome! To contribute:</p>
            <ol>
                <li>Fork the repository.</li>
                <li>Create a new feature branch (<code>git checkout -b feature/YourFeature</code>).</li>
                <li>Commit your changes (<code>git commit -am 'Add new feature'</code>).</li>
                <li>Push to the branch (<code>git push origin feature/YourFeature</code>).</li>
                <li>Create a new Pull Request.</li>
            </ol>

            <h2>License</h2>
            <p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>
        </div>
    </div>
</body>
</html>

