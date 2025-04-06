import os
import platform
import psutil
import json
import csv
from functools import wraps
from typing import Callable
from datetime import datetime
import time

def get_system_info(result_file_path: str):
    """
    Get system info and include the path to the result file.
    """
    return {
        "CPU": platform.processor() or "Unknown",
        "RAM_GB": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "OS": f"{platform.system()} {platform.release()}",
        "Architecture": platform.machine(),
        "Test_Result_File": result_file_path
    }

def measure_time_to_csv(n: int, csv_filename: str, folder_name: str = "time_benchmark"):
    """
    Decorator to measure execution time, store system info in a JSON file,
    and store execution time results in a CSV file.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Create the directory if it doesn't exist
            os.makedirs(folder_name, exist_ok=True)

            # Create file paths
            result_file_path = os.path.join(folder_name, f"{csv_filename}.csv")
            system_info_path = os.path.join(folder_name, "system_info.json")

            # Write system info to JSON if the file does not exist
            if not os.path.isfile(system_info_path):
                system_info = get_system_info(result_file_path)
                with open(system_info_path, "w") as json_file:
                    json.dump(system_info, json_file, indent=4)

            # Open the result CSV file and write the data
            with open(result_file_path, mode='a', newline='') as result_file:
                writer = csv.writer(result_file)

                # If file doesn't exist, write the header
                if result_file.tell() == 0:
                    writer.writerow(['timestamp', 'function', 'run', 'execution_time (s)'])

                # Run the function n times and log execution time
                for i in range(1, n + 1):
                    start_time = time.time()
                    result = func(*args, **kwargs)
                    end_time = time.time()

                    execution_time = end_time - start_time

                    writer.writerow([
                        datetime.now().isoformat(),
                        func.__name__,
                        i,
                        execution_time
                    ])
            return result
        return wrapper
    return decorator
