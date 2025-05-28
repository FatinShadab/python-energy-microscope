import pandas as pd

# File paths
energy_file = input("Enter the path to the energy CSV file: ")
time_file = input("Enter the path to the time CSV file: ")
carbon_file = input("Enter the path to the carbon CSV file: ")
output_file = input("Enter the path to save the combined means CSV file: ")

# Load CSV files
df_energy = pd.read_csv(energy_file)
df_time = pd.read_csv(time_file)
df_carbon = pd.read_csv(carbon_file)

# Drop the 'algorithm' column
energy_means = df_energy.drop(columns='algorithm').mean().round(3)
time_means = df_time.drop(columns='algorithm').mean().round(3)
carbon_means = df_carbon.drop(columns='algorithm').mean().round(3)

# Create clean method names (e.g., 'cpython' instead of 'cpython_μJ')
methods = [col.split('_')[0] for col in energy_means.index]

# Combine into one DataFrame
summary_df = pd.DataFrame({
    'method': methods,
    'energy_mean_μJ': energy_means.values,
    'time_mean_s': time_means.values,
    'carbon_mean_gCO2eq': carbon_means.values
})

# Save to CSV
summary_df.to_csv(output_file, index=False)
print(f"✅ Cleaned method means saved to: {output_file}")
print(summary_df)