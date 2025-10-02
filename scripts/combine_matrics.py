import pandas as pd

# ---------- Load Data ----------
df_carbon = pd.read_csv("..\\data\\collection_1\\combine\\carbon_footprint.csv")
df_energy = pd.read_csv("..\\data\\collection_1\\combine\\energy_com.csv")
df_time   = pd.read_csv("..\\data\\collection_1\\combine\\time_com.csv")

# ---------- Standardize column names ----------
df_carbon = df_carbon.rename(columns={"algorithm": "benchmark"})
df_energy = df_energy.rename(columns={"algorithm": "benchmark"})
df_time   = df_time.rename(columns={"algorithm": "benchmark"})

df_carbon = df_carbon.rename(columns={
    "cpython_CO2e_g": "CPython",
    "ctypes_CO2e_g": "Ctypes",
    "cython_CO2e_g": "Cython",
    "pycompile_CO2e_g": "PyCompile",
    "pypy_CO2e_g": "PyPy"
})
df_energy = df_energy.rename(columns={
    "cpython": "CPython",
    "ctypes": "Ctypes",
    "cython": "Cython",
    "pycompile": "PyCompile",
    "pypy": "PyPy"
})
df_time = df_time.rename(columns={
    "cpython": "CPython",
    "ctypes": "Ctypes",
    "cython": "Cython",
    "pycompile": "PyCompile",
    "pypy": "PyPy"
})

# ---------- Melt into long format ----------
long_carbon = df_carbon.melt(id_vars="benchmark", var_name="method", value_name="carbon_g")
long_energy = df_energy.melt(id_vars="benchmark", var_name="method", value_name="energy_uJ")
long_time   = df_time.melt(id_vars="benchmark", var_name="method", value_name="time_s")

# ---------- Convert energy from µJ to J ----------
long_energy["energy_j"] = long_energy["energy_uJ"] / 1e6
long_energy = long_energy.drop(columns=["energy_uJ"])

# ---------- Merge ----------
df_merged = long_time.merge(long_energy, on=["benchmark", "method"])
df_merged = df_merged.merge(long_carbon, on=["benchmark", "method"])

# ---------- Save ----------
df_merged.to_csv("greenscore_raw_per_benchmark.csv", index=False)

print("Saved merged file: greenscore_raw_per_benchmark.csv")
print(df_merged.head())
