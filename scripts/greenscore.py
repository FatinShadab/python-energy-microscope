import pandas as pd

def read_csv_files():
    # Prompt user for three file paths
    # file_paths = []
    # for i in ("energy", "time", "carbon"):
    #     file_path = input(f"Enter the path for CSV file of {i}: ")
    #     file_paths.append(file_path)

    file_paths = [
        '/home/eaegon/Documents/GITHUB/python-energy-microscope/data/collection_1/combine/energy_com.csv',
        '/home/eaegon/Documents/GITHUB/python-energy-microscope/data/collection_1/combine/time_com.csv',
        '/home/eaegon/Documents/GITHUB/python-energy-microscope/data/collection_1/combine/carbon_footprint.csv'
    ]

    # Read the CSV files into DataFrames
    dataframes = []
    for path in file_paths:
        try:
            df = pd.read_csv(path)
            dataframes.append(df)
            print(f"Successfully read file: {path}")
        except Exception as e:
            print(f"Error reading file {path}: {e}")

    return dataframes

def create_nom_score_df(df: pd.DataFrame, output_path: str = None) -> pd.DataFrame:
    """
    Normalize energy usage across methods (row-wise) per algorithm.
    
    Parameters:
    - df: DataFrame with one row per algorithm, 'algorithm' column, and energy columns.
    - output_path: Optional path to save the normalized DataFrame as CSV.
    
    Returns:
    - A DataFrame with 'algorithm' and normalized method columns.
    """
    # Copy the original to avoid modifying it
    df = df.copy()

    # Extract the algorithm names
    algorithm_names = df['algorithm']

    # Select only numeric method columns
    method_cols = df.columns.drop('algorithm')
    numeric_df = df[method_cols]

    # Apply row-wise normalization (min-max per algorithm)
    normalized_df = numeric_df.apply(
        lambda row: (row - row.min()) / (row.max() - row.min())
        if row.max() != row.min() else row * 0,  # handle constant rows
        axis=1
    )

    # Add back the algorithm column
    normalized_df.insert(0, 'algorithm', algorithm_names)

    # Save to CSV if path is given
    if output_path:
        normalized_df.to_csv(output_path, index=False)
        print(f"✅ Normalized DataFrame saved to: {output_path}")

    return normalized_df

def create_mean_score_df(
    energy_df: pd.DataFrame,
    time_df: pd.DataFrame,
    carbon_df: pd.DataFrame,
    output_path: str = None
) -> pd.DataFrame:
    """
    Create a mean score DataFrame by averaging across all algorithms
    for each method from the input normalized energy, time, and carbon DataFrames.

    Parameters:
    - energy_df: DataFrame with normalized energy (µJ) per method.
    - time_df: DataFrame with normalized time per method.
    - carbon_df: DataFrame with normalized carbon per method.
    - output_path: Optional path to save the final CSV.

    Returns:
    - mean_score_df: DataFrame with method-wise mean scores.
    """

    # Drop the 'algorithm' column
    energy = energy_df.drop(columns=['algorithm'])
    time = time_df.drop(columns=['algorithm'])
    carbon = carbon_df.drop(columns=['algorithm'])

    # Compute column-wise means
    energy_mean = energy.mean()
    time_mean = time.mean()
    carbon_mean = carbon.mean()

    # Combine into a single DataFrame
    mean_score_df = pd.DataFrame({
        'method': energy_mean.index,
        'energy_mean_J': energy_mean.values,
        'time_mean': time_mean.values,
        'carbon_mean': carbon_mean.values
    })

    # Optional CSV save
    if output_path:
        mean_score_df.to_csv(output_path, index=False)
        print(f"✅ GreenScore means saved to: {output_path}")

    return mean_score_df

def calculate_greenscore(df_energy, df_time, df_carbon, alpha=0.4, beta=0.4, gamma=0.2):
    """
    Compute the Green Score for each method by combining normalized
    energy, time, and carbon scores with weighted averaging.
    
    Parameters:
    - df_energy: Raw energy DataFrame (with 'algorithm' column).
    - df_time: Raw time DataFrame.
    - df_carbon: Raw carbon DataFrame.
    - alpha, beta, gamma: Weights for energy, carbon, and time (sum must be 1.0).
    
    Returns:
    - green_score_df: DataFrame sorted by green score (ascending).
    """

    # Step 1: Normalize each DataFrame and save intermediate files
    energy_nom_score_df = create_nom_score_df(df_energy, output_path="energy_nom_score.csv")
    time_nom_score_df = create_nom_score_df(df_time, output_path="time_nom_score.csv")
    carbon_nom_score_df = create_nom_score_df(df_carbon, output_path="carbon_nom_score.csv")

    # Step 2: Calculate per-method mean scores
    mean_df = create_mean_score_df(
        energy_nom_score_df,
        time_nom_score_df,
        carbon_nom_score_df,
        output_path="green_score_components_means.csv"
    )

    # Step 3: Compute GreenScore = α·energy + β·carbon + γ·time
    mean_df["green_score"] = (
        alpha * mean_df["energy_mean_J"] +
        beta * mean_df["carbon_mean"] +
        gamma * mean_df["time_mean"]
    )

    # Step 4: Sort methods by green score (lower is better)
    green_score_df = mean_df.sort_values(by="green_score").reset_index(drop=True)

    # Step 5: Save the final ranked list
    green_score_df.to_csv("green_score_ranking.csv", index=False)
    print("✅ Final Green Score ranking saved to: green_score_ranking.csv")

    return green_score_df


# Example usage
if __name__ == "__main__":
    dfs = read_csv_files()
    for i, df in enumerate(dfs, start=1):
        print(f"\nPreview of DataFrame {i}:")
        print(df.head())
        
    calculate_greenscore(dfs[0], dfs[1], dfs[2])