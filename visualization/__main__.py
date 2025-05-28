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

def plot_execution_vs_energy_scatter(energy_file, time_file, output_file):
    import matplotlib.pyplot as plt
    import pandas as pd

    # Load and reshape data
    energy_df = pd.read_csv(energy_file)
    time_df = pd.read_csv(time_file)

    energy_long = energy_df.melt(id_vars=["algorithm"], var_name="method", value_name="energy_μJ")
    time_long = time_df.melt(id_vars=["algorithm"], var_name="method", value_name="time_s")

    merged = pd.merge(energy_long, time_long, on=["algorithm", "method"])
    merged["energy_J"] = merged["energy_μJ"] / 1e6  # Convert μJ to J

    # Plotting
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        merged["time_s"],
        merged["energy_J"],
        c=merged["method"].astype("category").cat.codes,
        cmap="tab10",
        alpha=0.8,
        edgecolors="k"
    )

    # Add algorithm labels
    for _, row in merged.iterrows():
        plt.text(row["time_s"] + 0.02, row["energy_J"], row["algorithm"], fontsize=7, alpha=0.7)

    # Add legend
    handles, _ = scatter.legend_elements(prop="colors", alpha=0.6)
    labels = merged["method"].unique()
    plt.legend(handles, labels, title="Method", bbox_to_anchor=(1.05, 1), loc="upper left")

    plt.title("Execution Time vs Energy Consumption (Per Algorithm × Method)")
    plt.xlabel("Execution Time (s)")
    plt.ylabel("Energy Consumption (J)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"✅ Saved scatter plot: {output_file}")
    plt.close()

def plot_time_vs_energy_line_chart(energy_file, time_file, output_file):
    import pandas as pd
    import matplotlib.pyplot as plt

    # Read CSVs
    energy_df = pd.read_csv(energy_file)
    time_df = pd.read_csv(time_file)

    # Convert energy to Joules
    for col in energy_df.columns[1:]:
        energy_df[col] = energy_df[col] / 1e6  # μJ → J

    algorithms = energy_df["algorithm"]
    methods = energy_df.columns[1:]

    # Set up subplots
    plt.figure(figsize=(14, 6))

    for method in methods:
        plt.plot(
            algorithms,
            energy_df[method],
            marker='o',
            label=f"{method} - Energy (J)",
            linestyle='--'
        )
        plt.plot(
            algorithms,
            time_df[method],
            marker='x',
            label=f"{method} - Time (s)",
            linestyle='-'
        )

    # Formatting
    plt.title("Execution Time and Energy Consumption Trends per Method")
    plt.xlabel("Algorithm")
    plt.ylabel("Value (Joules / Seconds)")
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    plt.savefig(output_file)
    print(f"✅ Saved line chart: {output_file}")
    plt.close()

def plot_method_metric_line_chart(csv_file, output_file):
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the CSV
    df = pd.read_csv(csv_file)

    # Convert energy from μJ to J
    df['energy_mean_J'] = df['energy_mean_μJ'] / 1e6

    # Plotting setup
    plt.figure(figsize=(10, 6))
    methods = df['method']

    # Plot energy
    plt.plot(methods, df['energy_mean_J'], marker='o', linestyle='-', label='Energy (J)', color='tab:blue')

    # Plot time
    plt.plot(methods, df['time_mean_s'], marker='s', linestyle='--', label='Time (s)', color='tab:orange')

    # Styling
    plt.title('Comparison of Energy and Time Footprint by Execution Method')
    plt.xlabel('Execution Method')
    plt.ylabel('Metric Value')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"✅ Saved line chart: {output_file}")
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Energy Microscope Visualization Tool")
    
    parser.add_argument("csv_file", nargs='?', help="Path to the CSV file (required for --evcvt)")
    parser.add_argument("--output_file", help="Optional output image path", default=None)
    parser.add_argument("--evcvt", action="store_true", help="Enable Energy/Time/Carbon grouped bar chart")
    parser.add_argument("--etc_compare", action="store_true", help="Enable Energy Time Carbon relation line chart")
    parser.add_argument("--lcpack", action="store_true", help="Generates line charts of energy, time, and carbon per algorithm")
    parser.add_argument("--scatter", nargs=2, metavar=('energy_csv', 'time_csv'), help="Generate scatter plot comparing time vs energy")
    parser.add_argument("--line_compare", nargs=2, metavar=('energy_csv', 'time_csv'),
                    help="Line chart comparing energy and time trends per method")



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
    elif args.scatter:
        energy_csv, time_csv = args.scatter
        plot_execution_vs_energy_scatter(
            energy_file=energy_csv,
            time_file=time_csv,
            output_file=args.output_file or "scatter_energy_vs_time.png"
        )
    elif args.line_compare:
        energy_csv, time_csv = args.line_compare
        plot_time_vs_energy_line_chart(
            energy_file=energy_csv,
            time_file=time_csv,
            output_file=args.output_file or "line_energy_vs_time_trends.png"
        )
    elif args.etc_compare:
        plot_method_metric_line_chart(
            csv_file='/home/eaegon/Documents/GITHUB/python-energy-microscope/data/collection_1/analysis/energy_vs_carbon_vs_time.csv',
            output_file='method_metric_comparison_linechart.png'
        )
    else:
        print("❌ No action specified. Use --evcvt to generate grouped metric chart or --lcpack to generate line plots.")


if __name__ == "__main__":
    main()
