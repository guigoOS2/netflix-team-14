README
## Project Overview
This project implements a simple ETL (Extract, Transform, Load) pipeline using Python. It processes movie watch history data to generate useful insights about movie popularity, user activity, and ratings.

## Project Structure
The pipeline is organized into four main stages:
1. Extract: Retrieves data from the movies, users, and watch history lists.
2. Transform: Processes the extracted data and calculates key metrics.
3. Load: Generates and displays a summary report.
4. Complete Pipeline: Executes all stages in sequence.

## Features
The pipeline generates the following metrics:
- Total Watch Events: Counts the total number of movie views recorded.
- Average Rating: Calculates the average rating given by users.
- Most Watched Movie: Identifies the movie with the highest number of views.
- Most Active User:  Identifies the user with the highest number of watch events.
- Movie Popularity Ranking: Ranks movies based on the number of views.

## Technologies Used
- Python
- Logging module
- Object-Oriented Programming (OOP)
- Python data structures (lists and dictionaries)

## How to Run
1. Clone this repository:

   ```bash
   git clone <https://github.com/guigoOS2/netflix-team-14>
   ```
2. Navigate to the project directory:

   ```bash
   cd <project-folder>
   ```
3. Run the Python script:

   ```bash
   python main.py
   ```
No external libraries are required.
## Example Output
```text
========== MOVIE REPORT ==========
Total Watch Events: 6
Average Rating: 4.33
Most Watched Movie: The Matrix
Most Active User: Linus

Movie Popularity Ranking
------------------------
1. The Matrix (3 views)
2. Inception (2 views)
3. Interstellar (1 views)
```


