import csv
import os
import sys
from collections import defaultdict

def extract_algorithm_name(full_name):
    # Extracts everything before the last underscore
    return '_'.join(full_name.split('_')[:-1])

def main(file_paths, output_file):
    energy_data = defaultdict(dict)  # {algorithm: {method: value}}

    for file_path in file_paths:
        method_name = os.path.basename(os.path.dirname(file_path))  # cpython, pypy, etc.

        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                full_filename = row['filename']
                algorithm = extract_algorithm_name(full_filename)

                try:
                    avg = float(row['average_package (uJ)'])
                    energy_data[algorithm][method_name] = avg
                except ValueError:
                    continue

    all_methods = sorted({method for algo_data in energy_data.values() for method in algo_data})

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['algorithm'] + all_methods)

        for algorithm in sorted(energy_data):
            row = [algorithm] + [energy_data[algorithm].get(method, '') for method in all_methods]
            writer.writerow(row)

    print(f"Combined comparison saved to '{output_file}'.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python combine_energy_csvs.py <output_csv>")
    else:
        output_file = sys.argv[1]
        
        file_paths = [
            '../collection_1/cpython/energy_avg.csv',
            '../collection_1/pypy/energy_avg.csv',
            '../collection_1/cython/energy_avg.csv',
            '../collection_1/pycompile/energy_avg.csv',
            '../collection_1/ctypes/energy_avg.csv',
        ]
        
        main(file_paths, output_file)
