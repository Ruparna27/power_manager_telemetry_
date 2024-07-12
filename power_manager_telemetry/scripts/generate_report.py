import json

def generate_report(telemetry):
    with open('/app/telemetry_report.json', 'w') as report_file:
        json.dump(telemetry, report_file, indent=4)

if __name__ == "__main__":
    with open('/app/telemetry_data.json', 'r') as telemetry_file:
        telemetry = json.load(telemetry_file)
    generate_report(telemetry)
