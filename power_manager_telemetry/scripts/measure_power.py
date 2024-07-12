import json

def measure_power_utilization(system_utilization):
    # Placeholder function, implement actual measurement logic
    power_utilization = {
        "cpu_power": 64.0,  # Example values, replace with actual measurements
        "nic_power": 40.0,
        "tdp_power": 56.0
    }
    return power_utilization

def main():
    system_utilization = 100  # Example: 100% utilization
    power_utilization = measure_power_utilization(system_utilization)
    
    with open('../telemetry_data.json', 'r+') as telemetry_file:
        telemetry_data = json.load(telemetry_file)
        telemetry_data["power_utilization"] = power_utilization
        telemetry_file.seek(0)
        json.dump(telemetry_data, telemetry_file, indent=4)
        telemetry_file.truncate()
    
    print("Power utilization measured and updated in telemetry data.")

if __name__ == "__main__":
    main()

