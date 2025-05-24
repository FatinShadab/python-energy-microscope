import csv
import os
import sys

def compute_package_avg(file_path):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        package_values = []

        for row in reader:
            try:
                val = float(row['execution_time (s)'])
                package_values.append(val)
            except (ValueError, KeyError):
                continue  # Skip invalid or missing values

        if not package_values:
            return None
        
        #print(f"{file_path} - {len(package_values)}")

        return sum(package_values) / len(package_values)

def main(folder_path, output_file):
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    if not csv_files:
        print("No CSV files found in the given folder.")
        return

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['filename', 'execution_time (s)'])

        for file_name in csv_files:
            full_path = os.path.join(folder_path, file_name)
            avg = compute_package_avg(full_path)

            if avg is not None:
                writer.writerow([file_name.split('.')[0], avg])
            else:
                print(f"Skipped {file_name} — no valid 'execution_time (s)' data.")

    print(f"Averages saved to '{output_file}'.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python average_package_time.py <folder_path> <output_csv>")
    else:
        folder_path = sys.argv[1]
        output_file = sys.argv[2]
        main(folder_path, output_file)
