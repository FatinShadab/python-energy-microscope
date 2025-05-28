import pandas as pd

file_paths = [
    input("Enter the path for energy data CSV: "),
    input("Enter the path for time data CSV: "),
    input("Enter the path for carbon footprint data CSV: ")
]

df_energy = pd.read_csv(file_paths[0])
df_time = pd.read_csv(file_paths[1])
df_carbon = pd.read_csv(file_paths[2])

energy_std = df_energy.drop(columns=["algorithm"]).std()
time_std = df_time.drop(columns=["algorithm"]).std()
carbon_std = df_carbon.drop(columns=["algorithm"]).std()

summary_df = pd.DataFrame({
    "method": energy_std.index.str.replace("_μJ", "").str.replace("_s", "").str.replace("_CO2e_g", ""),
    "energy_std_μJ": energy_std.values,
    "time_std_s": time_std.values,
    "carbon_std_gCO2eq": carbon_std.values
})

summary_df.to_csv("std_summary.csv", index=False)