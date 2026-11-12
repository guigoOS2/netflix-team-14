
import logging
from pathlib import Path
import pandas as pd

# PART 1: EXTRACT
def extract_data():
    logging.info("Extracting data...")

    # Locate the DATA folder
    project_root = Path(__file__).resolve().parent.parent
    data_folder = project_root / "DATA"

    # Read CSV files
    movies_df = pd.read_csv(data_folder / "movies.csv")
    users_df = pd.read_csv(data_folder / "users.csv")
    history_df = pd.read_csv(data_folder / "watch_history.csv")

    # Match the column names expected by Transform
    movies_df = movies_df.rename(columns={"movie_id": "id"})
    users_df = users_df.rename(columns={"user_id": "id"})

    # Convert DataFrames into lists of named tuples
    movies = list(movies_df.itertuples(index=False))
    users = list(users_df.itertuples(index=False))
    history = list(history_df.itertuples(index=False))

    return movies, users, history

# Run it to test or debug the extraction (Main guard)
if __name__ == "__main__":
    extract_data()
