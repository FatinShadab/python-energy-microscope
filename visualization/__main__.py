import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_grouped_bar_chart(csv_file, metrics, x_column, title, ylabel, output_file=None, normalize=True):
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    df = pd.read_csv(csv_file)

    if normalize:
        df[metrics] = df[metrics] / df[metrics].max()
        fig, ax = plt.subplots()
        ax.text(1.5, 22, r"Values normalized: $x_{norm} = \frac{x}{\max(x)}$", fontsize=12, color='red')

    categories = df[x_column]
    bar_width = 0.2
    index = np.arange(len(categories))

    plt.figure(figsize=(10, 6))

    for i, metric in enumerate(metrics):
        plt.bar(index + i * bar_width, df[metric], width=bar_width, label=metric.replace('_', ' ').title())

    plt.xlabel(x_column.title())
    plt.ylabel("Normalized Value " + r" [$x_{norm} = \frac{x}{\max(x)}, x_{norm} \in [0, 1]$]" if normalize else ylabel)
    plt.title(title)
    plt.xticks(index + bar_width, categories)
    plt.legend()
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    if output_file:
        plt.tight_layout()
        plt.savefig(output_file)
        print(f"✅ Chart saved to: {output_file}")
    else:
        plt.show()

def plot_metric_line_chart(file_path, metric_unit, title, ylabel, output_file):
    df = pd.read_csv(file_path)
    algorithms = df['algorithm']
    methods = df.columns[1:]

    # Transpose for line plotting: each line is a method across algorithms
    df_transposed = df.set_index('algorithm').T

    plt.figure(figsize=(14, 6))
    for method in df_transposed.index:
        plt.plot(algorithms, df_transposed.loc[method], marker='o', label=method.replace('_', r'\_'))

    plt.title(title)
    plt.xlabel('Algorithm')
    plt.ylabel(f'{ylabel} ({metric_unit})')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(title='Method', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"✅ Saved chart: {output_file}")
    plt.close()

def main():
    parser = argparse.ArgumentParser(description="Energy Microscope Visualization Tool")
    
    parser.add_argument("csv_file", nargs='?', help="Path to the CSV file (required for --evcvt)")
    parser.add_argument("--output_file", help="Optional output image path", default=None)
    parser.add_argument("--evcvt", action="store_true", help="Enable Energy/Time/Carbon grouped bar chart")
    parser.add_argument("--lcpack", action="store_true", help="Generates line charts of energy, time, and carbon per algorithm")

    args = parser.parse_args()

    if args.evcvt:
        if not args.csv_file:
            print("❌ Error: --evcvt requires a CSV file path.")
            return
        metrics = ["energy_mean_μJ", "time_mean_s", "carbon_mean_gCO2eq"]
        generate_grouped_bar_chart(
            csv_file=args.csv_file,
            metrics=metrics,
            x_column="method",
            title="Energy, Time, and Carbon Footprint Across Python Execution Methods",
            ylabel="Metric Values (μJ, s, gCO₂e)",
            output_file=args.output_file
        )
        
    elif args.lcpack:
        plot_metric_line_chart(
            file_path="/home/eaegon/Documents/GITHUB/python-energy-microscope/data/collection_1/combine/energy_com.csv",
            metric_unit="μJ",
            title="Energy Consumption per Algorithm",
            ylabel="Energy",
            output_file="line_energy_per_algorithm.png"
        )

        plot_metric_line_chart(
            file_path="/home/eaegon/Documents/GITHUB/python-energy-microscope/data/collection_1/combine/time_com.csv",
            metric_unit="s",
            title="Execution Time per Algorithm",
            ylabel="Time",
            output_file="line_time_per_algorithm.png"
        )

        plot_metric_line_chart(
            file_path="/home/eaegon/Documents/GITHUB/python-energy-microscope/data/collection_1/combine/carbon_footprint.csv",
            metric_unit="gCO₂eq",
            title="Carbon Footprint per Algorithm",
            ylabel="Carbon Emission",
            output_file="line_carbon_per_algorithm.png"
        )
    else:
        print("❌ No action specified. Use --evcvt to generate grouped metric chart or --lcpack to generate line plots.")


if __name__ == "__main__":
    main()
