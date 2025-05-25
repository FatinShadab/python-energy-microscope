import csv
import os
import sys
from collections import defaultdict

def extract_algorithm_name(full_name):
    return '_'.join(full_name.split('_')[:-1])

def main(file_paths, output_file):
    time_data = defaultdict(dict)  # {algorithm: {method: time}}

    for file_path in file_paths:
        method_name = os.path.basename(os.path.dirname(file_path))

        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                full_filename = row['filename']
                algorithm = extract_algorithm_name(full_filename)

                try:
                    exec_time = float(row['execution_time (s)'])
                    time_data[algorithm][method_name] = exec_time
                except ValueError:
                    continue

    all_methods = sorted({method for algo_data in time_data.values() for method in algo_data})

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['algorithm'] + all_methods)

        for algorithm in sorted(time_data):
            row = [algorithm] + [time_data[algorithm].get(method, '') for method in all_methods]
            writer.writerow(row)

    print(f"Combined execution time saved to '{output_file}'.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python combine_time_csvs.py <output_csv>")
    else:
        output_file = sys.argv[1]
        
        file_paths = [
            '../collection_1/cpython/time_avg.csv',
            '../collection_1/pypy/time_avg.csv',
            '../collection_1/cython/time_avg.csv',
            '../collection_1/pycompile/time_avg.csv',
            '../collection_1/ctypes/time_avg.csv',
        ]
        
        main(file_paths, output_file)
