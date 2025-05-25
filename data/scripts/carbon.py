import csv

INPUT_CSV = input("enter the target file path: ")  # Replace with your file name
OUTPUT_CSV = "carbon_footprint.csv"
CARBON_INTENSITY = 0.000475  # gCO₂e per J (global average)

def calculate_carbon(energy_uj):
    return energy_uj * 1e-6 * CARBON_INTENSITY  # Convert μJ to J, then multiply

def main():
    with open(INPUT_CSV, 'r') as infile, open(OUTPUT_CSV, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['algorithm'] + [f"{method}_CO2e_g" for method in reader.fieldnames[1:]]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            result = {'algorithm': row['algorithm']}
            for method in reader.fieldnames[1:]:
                try:
                    energy_uj = float(row[method])
                    co2e = calculate_carbon(energy_uj)
                    result[f"{method}_CO2e_g"] = round(co2e, 6)
                except ValueError:
                    result[f"{method}_CO2e_g"] = ''
            writer.writerow(result)

    print(f"Carbon footprint data saved to '{OUTPUT_CSV}'.")


if __name__ == "__main__":
    main()
