import re
import csv

LOG_PATTERN = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\d{3}) (.*)$"
def parse_serverlogs(input_file="server_lod.txt", output_file="error_report.txt"):
    log = []
    error_count = {}
    try:
        with open("server_log.txt", "r") as file:
            for line in file:
                match = re.search(LOG_PATTERN, line.strip())
                if match:
                    timestamp, severity, error_code, message = match.groups()
                    log_entry = {
                        "timestamp": timestamp,
                        "severity": severity,
                        "error_code": error_code,
                        "message": message,
                    }
                    log.append(log_entry)
                    if severity == "ERROR":
                        error_count[error_code] = error_count.get(error_code, 0) + 1

        with open(output_file, "w") as file:
            file.write("==================================================\n")
            file.write("             SERVER  LOG  ANALYSIS                \n")
            file.write("==================================================\n")

            file.write(f"Total Log Entries: {len(log)}")

            file.write("-----ERROR FREQUENCY-----")
            if error_count:
                for code, count in error_count.items():
                    file.write(f"Error Code {code}: {count} occurrence(s)\n")
                else:
                    file.write("No errors recorded.\n")

            file.write("\n-----DETAILED ERROR LOGS-----\n")
            for entry in log:
                if entry["severity"] == "ERROR":
                    file.write(
                        f"[{entry['timestamp']}] Code {entry["error_code"]}:"
                        f"{entry['message']}\n"
                    )
            print(
                f'Successfully processed {len(log)} log lines and geberated'
                f"{output_file}"
            )
    except FileNotFoundError:
        print(
            f"Error: The file '{input_file} was not found. Please create it first."
        )

if __name__ == "__main__":
    parse_serverlogs()