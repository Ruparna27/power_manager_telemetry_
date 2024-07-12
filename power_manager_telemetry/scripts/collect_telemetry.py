import psutil
import json

def get_telemetry_data():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    net_io = psutil.net_io_counters()
    # Add TDP measurement if applicable

    telemetry_data = {
        "cpu": {
            "percent": cpu_percent,
            "cores": psutil.cpu_count(logical=True),
            "frequency": psutil.cpu_freq().current,
        },
        "memory": {
            "total": memory_info.total,
            "available": memory_info.available,
            "percent": memory_info.percent,
        },
        "network": {
            "bytes_sent": net_io.bytes_sent,
            "bytes_recv": net_io.bytes_recv,
        }
        # Add more metrics as needed
    }
    return telemetry_data

def main():
    telemetry_data = get_telemetry_data()
    with open('../telemetry_data.json', 'w') as telemetry_file:
        json.dump(telemetry_data, telemetry_file, indent=4)
    print("Telemetry data written to ../telemetry_data.json")

if __name__ == "__main__":
    main()

