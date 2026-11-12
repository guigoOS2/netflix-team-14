#pre-code
import logging
from Netflix_team_14_Extract import extract_data
from Netflix_team_14_Transform import transform_data

# PART 3: LOAD REPORT
def load_report(data):
    logging.info("Loading report...")

    print("\n========== MOVIE REPORT ==========")
    print(f"Total Watch Events: {data['total_events']}")
    print(f"Average Rating: {data['average_rating']:.2f}")
    print(f"Most Watched Movie: {data['most_watched_movie']}")
    print(f"Most Active User: {data['most_active_user']}")

    print("\nMovie Popularity Ranking")
    print("------------------------")

    for position, (movie_id, views) in enumerate(data["ranking"], start=1):
        movie = next(
            movie for movie in data["movies"] if movie.id == movie_id
        )
        print(f"{position}. {movie.title} ({views} views)")


if __name__ == "__main__":
    movies, users, history = extract_data()
    transformed_data = transform_data(movies, users, history)
    load_report(transformed_data)