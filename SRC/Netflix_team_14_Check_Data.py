from pathlib import Path
import pandas as pd

# Find the project root
project_root = Path(__file__).resolve().parent.parent

# Define the three datasets
data_folder = project_root / "DATA"

movies = pd.read_csv(data_folder / "movies.csv")
users = pd.read_csv(data_folder / "users.csv")
history = pd.read_csv(data_folder / "watch_history.csv")

# Check the datasets
print("MOVIES:")
print(movies.head())

print("\nUSERS:")
print(users.head())

print("\nWATCH HISTORY:")
print(history.head())