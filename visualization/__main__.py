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


def main():
    parser = argparse.ArgumentParser(description="Energy Microscope Visualization Tool")
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("--output_file", help="Optional output image path", default=None)
    parser.add_argument("--evcvt", action="store_true", help="Enable Energy/Time/Carbon grouped bar chart")

    args = parser.parse_args()

    if args.evcvt:
        #metrics = ["energy_mean_μJ", "time_mean_s", "carbon_mean_gCO2eq"]
        metrics = ["energy_mean", "time_mean", "carbon_mean"]
            
        generate_grouped_bar_chart(
            csv_file=args.csv_file,
            metrics=metrics,
            x_column="method",
            title="Energy, Time, and Carbon Footprint Across Python Execution Methods",
            ylabel="Metric Values (μJ, s, gCO₂e)",
            output_file=args.output_file
        )
    else:
        print("❌ No action specified. Use --evcvt to generate grouped metric chart.")


if __name__ == "__main__":
    main()
